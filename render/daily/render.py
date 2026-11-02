"""Builds 일상 수사대 shorts: per-line TTS clips -> timeline -> scene/subtitle frames -> short.mp4, subtitle.srt, cover.jpg, post.json.
usage: python render.py <tts_root> <out_root> [ids...]
tts_root/daily-<id>/Lxx.mp3 must exist (made by the tts-lines workflow).
"""
import html, json, os, re, subprocess, sys
from playwright.sync_api import sync_playwright
from episodes import EPISODES
from scenes import scene_svg, DEFS

W, H, FPS = 1080, 1920, 30
GAP = 0.12          # silence between narration lines
LEAD = 0.10         # silence before the first line
END_CARD = 1.8
COL = {'red': '#ff5a5f', 'gold': '#f0c35a', 'white': '#f4f6fb'}
GLOW = {'red': 'rgba(255,70,80,.55)', 'gold': 'rgba(240,195,90,.5)', 'white': 'rgba(255,255,255,.3)'}
MAXC = 19           # subtitle characters per line (about 18)


def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(cmd[:200] + '\n' + r.stderr[-1500:])
    return r.stdout


def dur(p):
    return float(sh(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{p}"'))


def esc(s):
    return html.escape(s)


def wrap(text):
    """Greedy wrap at spaces into lines of about MAXC characters."""
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > MAXC:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    # a 2-line subtitle reads better when it breaks right after a comma
    if len(lines) == 2:
        ws = text.split(' ')
        for i in range(1, len(ws)):
            a, b = ' '.join(ws[:i]), ' '.join(ws[i:])
            if a.endswith(',') and len(a) <= MAXC + 1 and len(b) <= MAXC + 1 and min(len(a), len(b)) >= 6:
                return [a, b]
    # avoid a tiny orphan last line when two lines would balance better
    if len(lines) == 2 and len(lines[1]) <= 4:
        ws = text.split(' '); best = None
        for i in range(1, len(ws)):
            a, b = ' '.join(ws[:i]), ' '.join(ws[i:])
            if len(a) <= MAXC + 1 and len(b) <= MAXC + 1:
                sc = abs(len(a) - len(b))
                if best is None or sc < best[0]:
                    best = (sc, [a, b])
        if best:
            lines = best[1]
    return lines


def chunks(text):
    ls = wrap(text)
    if len(ls) <= 2:
        return [ls]
    # too long for one 2-line box: split into balanced parts at word boundaries (prefer right after a comma)
    import math
    k = max(2, math.ceil(len(text) / (2 * MAXC))); ws = text.split(' '); best = None
    def parts_for(cuts):
        idx = [0] + list(cuts) + [len(ws)]
        return [' '.join(ws[idx[j]:idx[j + 1]]) for j in range(len(idx) - 1)]
    import itertools
    for cuts in itertools.combinations(range(1, len(ws)), k - 1):
        ps = parts_for(cuts)
        if any(len(wrap(p)) > 2 for p in ps):
            continue
        sc = max(len(p) for p in ps) - min(len(p) for p in ps) - 6 * sum(p.endswith(',') for p in ps[:-1])
        if best is None or sc < best[0]:
            best = (sc, ps)
    if not best:
        return [ls[i:i + 2] for i in range(0, len(ls), 2)]
    return [wrap(p) for p in best[1]]


def weight(s):
    return len(re.sub(r'\s', '', s)) + 2 * s.count(',')


BASE_CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:"Noto Sans CJK KR",sans-serif;color:#f4f6fb}
.bg{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,#1d3466 0%,#13234a 45%,#0a1530 100%)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(120,150,210,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(120,150,210,.08) 2px,transparent 2px);background-size:120px 120px}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 55%,rgba(0,0,0,.45) 100%)}
.mono{font-family:"DejaVu Sans Mono",monospace;letter-spacing:6px}
.serif{font-family:"Noto Serif CJK KR",serif;font-weight:900}
'''


def page_bg(inner):
    return f'<html><head><style>{BASE_CSS}</style></head><body><div class="bg"></div><div class="grid"></div><div class="vig"></div>{inner}</body></html>'


def scene_html(ep, key, kw):
    inner = ''
    if key == 'number':
        t, c = kw
        inner += (f'<div style="position:absolute;left:0;right:0;top:620px;text-align:center;font-size:{300 if len(t) <= 4 else 220}px;font-weight:900;'
                  f'color:{COL[c]};text-shadow:0 0 80px {GLOW[c]},0 0 160px {GLOW[c]}">{esc(t)}</div>')
        return page_bg(inner)
    if kw:
        t, c = kw
        inner += f'<div style="position:absolute;left:0;right:0;top:300px;text-align:center;font-size:76px;font-weight:900;color:{COL[c]};text-shadow:0 0 40px {GLOW[c]}">{esc(t)}</div>'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="900" viewBox="0 0 1080 900">{DEFS}{scene_svg(key, ep)}</svg>'
    inner += f'<div style="position:absolute;left:0;top:{440 if kw else 400}px">{svg}</div>'
    return page_bg(inner)


def intro_html(ep):
    c = ep['big_c']
    return page_bg(
        f'<div class="mono" style="position:absolute;left:0;right:0;top:250px;text-align:center;font-size:36px;color:#9aa6ba">MYSTERY {ep["id"]}</div>'
        f'<div class="serif" style="position:absolute;left:0;right:0;top:320px;text-align:center;font-size:100px;line-height:130px;text-shadow:0 6px 24px rgba(0,0,0,.5)">'
        f'{esc(ep["q1"])}<br><span style="color:#f0c35a">{esc(ep["q2"])}</span></div>'
        f'<div style="position:absolute;left:0;right:0;top:690px;text-align:center;font-size:{280 if len(ep["big"]) <= 4 else 230}px;font-weight:900;color:{COL[c]};'
        f'text-shadow:0 0 80px {GLOW[c]},0 0 170px {GLOW[c]}">{esc(ep["big"])}</div>'
        f'<div style="position:absolute;left:0;right:0;top:1080px;text-align:center;font-size:50px;font-weight:700;color:#c9d2e3">{esc(ep["big_sub"])}</div>')


def end_html(ep):
    return page_bg(
        f'<div style="position:absolute;left:470px;top:640px;width:140px;height:180px;border:12px solid #f0c35a;border-radius:70px;box-shadow:0 0 40px rgba(240,195,90,.5)"></div>'
        f'<div class="mono" style="position:absolute;left:0;right:0;top:900px;text-align:center;font-size:36px;color:#c9d2e3;font-weight:700">MYSTERY {ep["id"]} · CASE CLOSED</div>'
        f'<div class="serif" style="position:absolute;left:0;right:0;top:960px;text-align:center;font-size:150px">일상 수사대</div>'
        f'<div style="position:absolute;left:0;right:0;top:1170px;text-align:center;font-size:48px;font-weight:700;color:#f0c35a">다음 미스터리는 댓글로 제보해 주세요</div>')


def header_html(ep):
    return (f'<html><head><style>{BASE_CSS} body{{background:transparent}}</style></head><body>'
            f'<div style="position:absolute;left:0;top:0;width:1080px;height:260px;background:linear-gradient(rgba(5,10,22,.92),rgba(5,10,22,.75) 70%,rgba(5,10,22,0))"></div>'
            f'<div class="mono" style="position:absolute;left:0;right:0;top:62px;text-align:center;font-size:32px;color:#f0c35a;font-weight:700">MYSTERY {ep["id"]}</div>'
            f'<div style="position:absolute;left:0;right:0;top:108px;text-align:center;font-size:58px;font-weight:900">{esc(ep["q1"] + " " + ep["q2"])}</div>'
            f'</body></html>')


def sub_html(lines):
    t = '<br>'.join(esc(l) for l in lines)
    return (f'<html><head><style>{BASE_CSS} body{{background:transparent}}</style></head><body>'
            f'<div style="position:absolute;left:0;right:0;top:1390px;text-align:center">'
            f'<span style="display:inline-block;max-width:980px;padding:20px 40px;border-radius:22px;background:rgba(0,0,0,.62);'
            f'font-size:58px;line-height:82px;font-weight:700;color:#ffffff">{t}</span></div></body></html>')


def cover_html(ep):
    c = ep['big_c']
    return (f'<html><head><style>{BASE_CSS}</style></head><body>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,#0a1530 0%,#16295a 50%,#0a1530 100%)"></div><div class="grid"></div>'
            f'<div class="serif" style="position:absolute;left:0;right:0;top:250px;text-align:center;font-size:112px;line-height:148px;text-shadow:0 6px 24px rgba(0,0,0,.5)">'
            f'{esc(ep["q1"])}<br><span style="color:#f0c35a">{esc(ep["q2"])}</span></div>'
            f'<div style="position:absolute;left:0;right:0;top:640px;text-align:center;font-size:{340 if len(ep["big"]) <= 4 else 260}px;font-weight:900;color:{COL[c]};'
            f'text-shadow:0 0 90px {GLOW[c]},0 0 200px {GLOW[c]},0 0 300px {GLOW[c]}">{esc(ep["big"])}</div>'
            f'<div style="position:absolute;left:0;right:0;top:1130px;text-align:center;font-size:62px;font-weight:700;color:#e6ebf4">{esc(ep["cover_sub"])}</div>'
            f'<div style="position:absolute;left:0;right:0;top:1560px;text-align:center"><span style="display:inline-block;padding:18px 54px;border-radius:60px;'
            f'border:4px solid #f0c35a;color:#f0c35a;font-size:52px;font-weight:900;background:rgba(240,195,90,.12)">일상 수사대</span></div>'
            f'</body></html>')


def shot(pg, htmlsrc, path, transparent=False):
    pg.set_content(htmlsrc)
    pg.wait_for_timeout(60)
    pg.screenshot(path=path, omit_background=transparent)


def srt_time(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'


def build(ep, tts_dir, out, pg):
    os.makedirs(out, exist_ok=True); work = os.path.join(out, '_w'); os.makedirs(work, exist_ok=True)
    # 1) audio clips, trimmed like the channel's other shorts
    clips = []
    for i, (text, key, kw) in enumerate(ep['lines']):
        src = os.path.join(tts_dir, f'L{i + 1:02d}.mp3'); wav = os.path.join(work, f'L{i + 1:02d}.wav')
        sh(f'ffmpeg -v error -y -i "{src}" -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,'
           f'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse,aresample=48000" -ac 1 "{wav}"')
        clips.append((wav, dur(wav)))
    # 2) timeline
    t = LEAD; segs = []
    for i, ((text, key, kw), (wav, d)) in enumerate(zip(ep['lines'], clips)):
        segs.append(dict(i=i, text=text, key=key, kw=kw, wav=wav, a=t, b=t + d)); t += d + GAP
    total_voice = segs[-1]['b']
    end_start = total_voice + 0.25; total = end_start + END_CARD
    # subtitle cues: split long lines into 2-line chunks, timed by syllable weight inside the spoken clip
    cues = []
    for s in segs:
        ch = chunks(s['text']); ws = [weight(' '.join(c)) for c in ch]; tw = sum(ws); a = s['a']
        for c, w in zip(ch, ws):
            b = a + (s['b'] - s['a']) * w / tw
            cues.append(dict(seg=s['i'], lines=c, a=a, b=b)); a = b
    # check: subtitle text == narration exactly
    for s in segs:
        joined = ' '.join(' '.join(c['lines']) for c in cues if c['seg'] == s['i'])
        assert joined == s['text'], (joined, s['text'])
    # 3) frames
    shot(pg, header_html(ep), f'{work}/header.png', True)
    for s in segs:
        shot(pg, intro_html(ep) if s['key'] == 'intro' else scene_html(ep, s['key'], s['kw']), f'{work}/bg{s["i"]:02d}.png')
    shot(pg, end_html(ep), f'{work}/end.png')
    for k, c in enumerate(cues):
        shot(pg, sub_html(c['lines']), f'{work}/sub{k:02d}.png', True)
        c['png'] = f'{work}/sub{k:02d}.png'
    shot(pg, cover_html(ep), f'{work}/cover.png')
    sh(f'ffmpeg -v error -y -i {work}/cover.png -q:v 2 {out}/cover.jpg')
    # 4) video segments: scene i spans from its line start to the next line start (first one from 0)
    parts = []
    bounds = [0.0] + [s['a'] for s in segs[1:]] + [end_start, total]
    for i in range(len(segs) + 1):
        st, en = bounds[i], bounds[i + 1]; D = en - st
        bg = f'{work}/bg{i:02d}.png' if i < len(segs) else f'{work}/end.png'
        inputs = f'-loop 1 -framerate {FPS} -t {D:.3f} -i {bg}'
        fc = (f'[0]scale=2160:3840,zoompan=z=\'1+0.035*on/{max(1, int(D * FPS))}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=1:s={W}x{H}:fps={FPS},'
              f'fade=t=in:st=0:d=0.18:color=0x0a1530[v0]')
        last, n = 'v0', 1
        if segs[i]['key'] != 'intro' if i < len(segs) else True:
            inputs += f' -loop 1 -framerate {FPS} -t {D:.3f} -i {work}/header.png'
            fc += f';[{last}][{n}]overlay=0:0[v{n}]'; last = f'v{n}'; n += 1
        if i < len(segs) and segs[i]['key'] != 'intro':  # first screen: the big question is on screen, no bottom subtitle box (user 2026-11-02)
            for c in cues:
                if c['seg'] != i:
                    continue
                inputs += f' -loop 1 -framerate {FPS} -t {D:.3f} -i {c["png"]}'
                fc += f';[{last}][{n}]overlay=0:0:enable=\'between(t,{c["a"] - st:.3f},{c["b"] - st - 0.001:.3f})\'[v{n}]'; last = f'v{n}'; n += 1
        p = f'{work}/part{i:02d}.mp4'
        if os.environ.get('REUSE_PARTS') and i > 0 and os.path.exists(p):
            parts.append(p); continue
        sh(f'ffmpeg -v error -y {inputs} -filter_complex "{fc}" -map "[{last}]" -frames:v {int(round(en * FPS)) - int(round(st * FPS))} '
           f'-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r {FPS} {p}')
        parts.append(p)
    open(f'{work}/parts.txt', 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in parts))
    sh(f'ffmpeg -v error -y -f concat -safe 0 -i {work}/parts.txt -c copy {work}/video.mp4')
    # 5) audio track
    ins = ' '.join(f'-i {s["wav"]}' for s in segs)
    mix = ';'.join(f'[{k}]adelay={int(s["a"] * 1000)}:all=1[a{k}]' for k, s in enumerate(segs))
    mix += ';' + ''.join(f'[a{k}]' for k in range(len(segs))) + f'amix=inputs={len(segs)}:normalize=0,apad=whole_dur={total:.3f},atrim=0:{total:.3f},loudnorm=I=-14:TP=-1.5:LRA=11[aout]'
    sh(f'ffmpeg -v error -y {ins} -filter_complex "{mix}" -map "[aout]" -ar 48000 -ac 2 {work}/audio.wav')
    sh(f'ffmpeg -v error -y -i {work}/video.mp4 -i {work}/audio.wav -c:v copy -c:a aac -b:a 160k -ar 48000 -shortest -movflags +faststart {out}/short.mp4')
    # 6) SRT (same text, same timing as the burned-in subtitles)
    srt = ''.join(f'{k + 1}\n{srt_time(c["a"])} --> {srt_time(c["b"])}\n' + '\n'.join(c['lines']) + '\n\n' for k, c in enumerate(cues))
    open(f'{out}/subtitle.srt', 'w', encoding='utf-8').write(srt)
    # 7) post.json
    tags = ['일상수사대', '생활미스터리', '알쓸신잡', '상식'] + ep['tags']
    ht = ' '.join('#' + x for x in tags)
    post = {'id': ep['id'], 'video': 'short.mp4', 'cover': 'cover.jpg', 'subtitle': 'subtitle.srt', 'post': {
        'reel_caption': f'{ep["hook"]}\n\n궁금한 미스터리는 댓글로 제보해 주세요 📮\n\n{ht}',
        'threads_video_caption': f'{ep["hook"]}\n\n#일상수사대',
        'yt_title': ep['yt_title'],
        'yt_description': f'{ep["hook"]}\n\n매일 지나치던 것들에 숨은 이유를 수사합니다.\n궁금한 미스터리는 댓글로 제보해 주세요.\n\n※ 내레이션과 그래픽은 AI 도구로 제작했어요.\n\n{ht} #shorts',
        'yt_tags': ','.join(tags + ['shorts'])}}
    json.dump(post, open(f'{out}/post.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    meta = dict(id=ep['id'], seconds=round(dur(f'{out}/short.mp4'), 2), cues=[{k: v for k, v in c.items() if k != 'png'} for c in cues], segs=[{k: v for k, v in s.items() if k != 'wav'} for s in segs])
    json.dump(meta, open(f'{work}/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return meta


if __name__ == '__main__':
    tts_root, out_root, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = br.new_page(viewport={'width': W, 'height': H})
        for ep in EPISODES:
            if ids and ep['id'] not in ids:
                continue
            m = build(ep, os.path.join(tts_root, 'daily-' + ep['id']), os.path.join(out_root, ep['id']), pg)
            print(ep['id'], m['seconds'], 's', len(m['cues']), 'cues', flush=True)
        br.close()
