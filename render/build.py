"""Builds one '뉴스 뒤의 주식' 3-second quiz short from a JSON payload.

Steps: OpenAI TTS (fixed voice) -> trim + pitch/tempo -> timeline -> frames (Playwright) -> audio mix -> MP4.
usage: python build.py payload.json out_dir
env:   OPENAI_API_KEY
"""
import json, os, re, subprocess, sys, urllib.error, urllib.request

VOICE = {
    'model': 'gpt-4o-mini-tts',
    'voice': 'verse',
    'pitch': 1.06,   # +6 %
    'tempo': 1.25,   # x1.25 after the pitch step (about x1.3 overall)
    'style': '아주 하이톤의 20대 초반 남성 숏폼 크리에이터. 높고 밝은 목소리, 잔뜩 흥분한 말투, 말 속도는 아주 빠르게, 문장 사이 쉼 거의 없이. '
             '질문은 궁금해 죽겠다는 듯 끌어올리고, 정답 공개는 놀라운 비밀을 폭로하듯. 친구에게 말하듯 자연스러운 반말, 발음은 또렷하게.',
}
CLOSING = '댓글로 달아봐'
OPENING = ('역발상으로 보면', '숨은 연결고리로 보면')
HERE = os.path.dirname(os.path.abspath(__file__))


def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        fail('STEP_FAILED: ' + cmd.split()[0] + ' -> ' + (r.stderr or r.stdout).strip()[-600:])
    return r.stdout


def fail(msg):
    # one line, readable from the GitHub annotations API and the Telegram failure notice
    msg = ' '.join(str(msg).split())
    msg = re.sub(r'sk-[A-Za-z0-9_*\-]{4,}', 'sk-…(hidden)', msg)  # never echo key fragments
    print('::error::' + msg[:900], flush=True)
    open('error.txt', 'w', encoding='utf-8').write(msg[:900])
    raise SystemExit(1)


def duration(path):
    return float(sh(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{path}"'))


def tts(text, out_mp3, clip_id=''):
    mock = os.environ.get('MOCK_TTS_DIR')  # local test only: reuse saved clips instead of calling the API
    if mock:
        import shutil; shutil.copy(os.path.join(mock, clip_id + '.mp3'), out_mp3); return
    body = json.dumps({'model': VOICE['model'], 'voice': VOICE['voice'], 'input': text,
                       'instructions': VOICE['style'], 'response_format': 'mp3'}).encode()
    req = urllib.request.Request('https://api.openai.com/v1/audio/speech', data=body, method='POST', headers={
        'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY'], 'Content-Type': 'application/json'})
    # a short must always come out (user rule 2026-10-24): transient TTS errors are retried before giving up
    last = ''
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r, open(out_mp3, 'wb') as f:
                f.write(r.read())
            return
        except urllib.error.HTTPError as e:
            last = f'TTS_HTTP_{e.code} ({clip_id}): ' + e.read().decode('utf-8', 'replace')[:400]
            if e.code in (400, 401, 403):
                break
        except Exception as e:
            last = f'TTS_FAILED ({clip_id}): {type(e).__name__} {e}'
        import time; time.sleep(5 * (attempt + 1))
    fail(last)


def split_caption(text):
    parts = [p.strip() for p in re.split(r'(?<=[.!?])\s+|,\s+(?=\d번)', text) if p.strip()]
    return parts or [text]


def main():
    payload, out = json.load(open(sys.argv[1], encoding='utf-8')), sys.argv[2]
    os.makedirs(out, exist_ok=True)
    v = payload['voice']
    # fixed lines are repaired, never a reason to drop the short (user rule 2026-10-24)
    if not v['c5'].lstrip().startswith(OPENING):
        print('::warning::answer clip did not start with the opening line; added', flush=True)
        v['c5'] = OPENING[0] + '! ' + v['c5'].strip()
    if not v['c5'].rstrip(' !.').endswith(CLOSING):
        v['c5'] = v['c5'].rstrip() + ' 너의 생각은 어때? 댓글로 달아봐!'
    d = {}
    for c in ['c1', 'c2', 'c4', 'c5']:
        raw, wav = f'{out}/{c}.mp3', f'{out}/{c}.wav'
        tts(v[c], raw, c)
        af = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,'
              'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,'
              f"aresample=44100,asetrate={int(44100 * VOICE['pitch'])},aresample=44100,atempo={VOICE['tempo']}")
        sh(f'ffmpeg -y -loglevel error -i "{raw}" -af "{af}" -ar 44100 -ac 2 "{wav}"')
        d[c] = duration(wav)
    # the closing line must really be spoken: a clip far shorter than its text means the voice was cut off
    if d['c5'] < len(v['c5']) / 14.0:
        tts(v['c5'], f'{out}/c5.mp3', 'c5')
        sh(f'ffmpeg -y -loglevel error -i "{out}/c5.mp3" -af "{af}" -ar 44100 -ac 2 "{out}/c5.wav"')
        d['c5'] = duration(f'{out}/c5.wav')
        if d['c5'] < len(v['c5']) / 14.0:
            print(f"::warning::VOICE_SHORT: answer clip {d['c5']:.1f}s for {len(v['c5'])} chars; kept so the short still goes out", flush=True)
    T = {'c1': 0.2}
    T['c2'] = T['c1'] + d['c1'] + 0.12
    T['o1'] = T['c2']; T['o2'] = T['c2'] + d['c2'] * 0.33; T['o3'] = T['c2'] + d['c2'] * 0.74
    T['count'] = T['c2'] + d['c2'] + 0.2
    T['news'] = T['count'] + 3.0
    T['c4'] = T['news'] + 0.3
    # the answer screen and the line '역발상으로 보면 …' start right after the news narration ends (no silent gap)
    T['ans'] = T['c4'] + d['c4'] + 0.3
    T['c5'] = T['ans'] + 0.1
    # follow / subscribe banner after the last spoken line (on screen only; the voice still ends with the closing line)
    T['cta'] = T['c5'] + d['c5'] + 0.25
    T['end'] = T['cta'] + 2.8
    T = {k: round(x, 2) for k, x in T.items()}
    caps = []
    for c in ['c1', 'c2', 'c4', 'c5']:
        parts = split_caption(v[c]); tot = sum(len(p) for p in parts); t = T[c]
        for p in parts:
            caps.append([round(t, 2), p]); t += d[c] * len(p) / tot
    caps.append([T['count'], '3… 2… 1…']); caps.append([T['cta'], '']); caps.sort(key=lambda x: x[0])
    T['captions'] = caps
    # page
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    inject = ('<script>window.QUIZ=' + json.dumps(payload['quiz'], ensure_ascii=False) + ';window.TL=' +
              json.dumps(T, ensure_ascii=False) + ';</script>\n<script>\n// window.QUIZ')
    page = tpl.replace('<script>\n// window.QUIZ', inject, 1)
    open(f'{out}/page.html', 'w', encoding='utf-8').write(page)
    sh(f'node "{HERE}/rec.js" "{out}/page.html" {T["end"]} "{out}/frames"')
    # audio: voice clips at their start times + 3 count beeps
    sh(f'ffmpeg -y -loglevel error -f lavfi -i "sine=frequency=880:duration=0.12" -af "volume=0.25,afade=t=out:st=0.06:d=0.06" -ar 44100 -ac 2 "{out}/beep.wav"')
    ins = [(f'{out}/c1.wav', T['c1']), (f'{out}/c2.wav', T['c2']), (f'{out}/beep.wav', T['count']), (f'{out}/beep.wav', T['count'] + 1),
           (f'{out}/beep.wav', T['count'] + 2), (f'{out}/c4.wav', T['c4']), (f'{out}/c5.wav', T['c5'])]
    args = ' '.join(f'-i "{p}"' for p, _ in ins)
    flt = ';'.join(f'[{i}]adelay={int(t * 1000)}|{int(t * 1000)}[a{i}]' for i, (_, t) in enumerate(ins))
    flt += ';' + ''.join(f'[a{i}]' for i in range(len(ins))) + f'amix=inputs={len(ins)}:normalize=0,apad=whole_dur={T["end"]}[out]'
    sh(f'ffmpeg -y -loglevel error {args} -filter_complex "{flt}" -map "[out]" -ar 44100 -ac 2 "{out}/mix.wav"')
    # first screen = the countdown scene (title, all options, big 3), held COVER seconds, so the feed preview shows the full quiz
    COVER = 0.5
    frames = sorted(f for f in os.listdir(f'{out}/frames') if f.endswith('.png'))
    cover = frames[min(len(frames) - 1, int((T['count'] + 0.45) * 30))]
    import shutil; shutil.copy(f'{out}/frames/{cover}', f'{out}/cover.png')
    ms = int(COVER * 1000)
    sh(f'ffmpeg -y -loglevel error -loop 1 -framerate 30 -t {COVER} -i "{out}/cover.png" -framerate 30 -i "{out}/frames/%05d.png" -i "{out}/mix.wav" '
       f'-filter_complex "[0:v]format=yuv420p[c];[1:v]format=yuv420p[m];[c][m]concat=n=2:v=1:a=0[v];[2:a]adelay={ms}|{ms}[a]" '
       f'-map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "{out}/short.mp4"')
    T['end'] = round(T['end'] + COVER, 2)
    meta = {'news_id': payload.get('news_id', ''), 'seconds': T['end'], 'clips': d, 'timeline': {k: x for k, x in T.items() if k != 'captions'}}
    json.dump(meta, open(f'{out}/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        fail(f'BUILD_CRASH: {type(e).__name__} {e}')
