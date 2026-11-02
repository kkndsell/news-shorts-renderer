"""Whisper verbose_json (+ manual text fixes) -> subtitle.srt in the same cue style as the new shorts.
usage: python stt2srt.py stt.json fixes.json out.srt
fixes.json: {"segments": [corrected text per segment, in order]}  (optional; whisper text used when missing)
"""
import json, sys
sys.path.insert(0, '/home/claude/dd')
from render import chunks, weight, srt_time

d = json.load(open(sys.argv[1], encoding='utf-8'))
fx = {}
try:
    fx = json.load(open(sys.argv[2], encoding='utf-8'))
except Exception:
    pass
segs = d['segments']; words = d.get('words') or []
texts = fx.get('segments') or [s['text'].strip() for s in segs]
assert len(texts) == len(segs), (len(texts), len(segs))
cues = []
for s, text in zip(segs, texts):
    if not text:
        continue
    ws = [w for w in words if w['start'] >= s['start'] - 0.05 and w['end'] <= s['end'] + 0.05]
    a = max(s['start'], ws[0]['start'] if ws else s['start'])
    b = min(s['end'], ws[-1]['end'] + 0.15) if ws else s['end']
    ch = chunks(text); wt = [weight(' '.join(c)) for c in ch]; tw = sum(wt)
    # chunk boundaries follow the spoken words: cut at the whisper word where the same share of characters is reached
    import re
    cw = [len(re.sub(r'[\s,.?!]', '', ' '.join(c))) for c in ch]; ctot = sum(cw)
    wl = [len(re.sub(r'[\s,.?!]', '', x['word'])) for x in ws]; tot = sum(wl) or 1; acc = 0
    for j, (c, w) in enumerate(zip(ch, wt)):
        acc += cw[j]
        if j == len(ch) - 1 or not ws:
            e = b if j == len(ch) - 1 else a + (b - a) * w / tw
        else:
            f, run, e = acc / ctot, 0, b
            for k, x in enumerate(ws):
                run += wl[k]
                if run / tot >= f - 1e-6:
                    e = ws[k + 1]['start'] if k + 1 < len(ws) else x['end']; break
        cues.append((a, e, c)); a = e
out = ''.join(f'{k + 1}\n{srt_time(a)} --> {srt_time(b)}\n' + '\n'.join(c) + '\n\n' for k, (a, b, c) in enumerate(cues))
open(sys.argv[3], 'w', encoding='utf-8').write(out)
print(out[:400])
