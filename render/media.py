"""Puts the public media for one article on GitHub Pages: card images as JPEG (Instagram needs JPEG),
the short video (if built) and post.json (captions + file list) that the n8n publisher reads.
usage: python media.py payload.json out_dir pages_dir
"""
import glob, json, os, subprocess, sys, urllib.request


CTA = '뉴스 뒤 숨은 종목, 매일 가장 먼저 · 팔로우하고 받아보세요'


def add_follow_line(path):
    """Last card only: one gold follow line under the footer (SNS copies; the review card in Telegram stays as rendered)."""
    from PIL import Image, ImageDraw, ImageFont
    fonts = sorted(glob.glob('/usr/share/fonts/**/NotoSansCJK-Bold.ttc', recursive=True))
    if not fonts:
        print('no CJK font, follow line skipped'); return
    im = Image.open(path).convert('RGB')
    if im.size != (1080, 1350):
        print('unexpected size, follow line skipped', im.size); return
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(fonts[0], 24, index=1)  # index 1 = Korean glyphs
    d.rectangle((0, 1304, 1080, 1350), fill=(15, 26, 44))
    d.text((70, 1309), CTA, font=f, fill=(212, 175, 55))
    im.save(path, quality=92)


payload, out, dest = json.load(open(sys.argv[1], encoding='utf-8')), sys.argv[2], sys.argv[3]
os.makedirs(dest, exist_ok=True)
images = []
for i, url in enumerate(payload.get('images') or [], 1):
    if not str(url).startswith('https://'):
        continue
    png = os.path.join(dest, f'card{i}.png')
    jpg = os.path.join(dest, f'card{i}.jpg')
    req = urllib.request.Request(url, headers={'User-Agent': 'news-shorts-bot'})
    with urllib.request.urlopen(req, timeout=60) as r, open(png, 'wb') as f:
        f.write(r.read())
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', png, '-q:v', '2', jpg], check=True)
    if i == 3:
        add_follow_line(jpg)
    os.remove(png)
    images.append(f'card{i}.jpg')
video = ''
if os.path.exists(os.path.join(out, 'short.mp4')):
    subprocess.run(['cp', os.path.join(out, 'short.mp4'), os.path.join(dest, 'short.mp4')], check=True)
    video = 'short.mp4'
meta = {}
try:
    meta = json.load(open(os.path.join(out, 'meta.json'), encoding='utf-8'))
except Exception:
    pass
post = {'news_id': payload.get('news_id', ''), 'images': images, 'video': video,
        'video_seconds': meta.get('seconds'), 'post': payload.get('post') or {}}
json.dump(post, open(os.path.join(dest, 'post.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in post.items() if k != 'post'}, ensure_ascii=False))
