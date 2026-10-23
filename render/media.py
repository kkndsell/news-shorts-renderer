"""Puts the public media for one article on GitHub Pages: card images as JPEG (Instagram needs JPEG),
the short video (if built) and post.json (captions + file list) that the n8n publisher reads.
usage: python media.py payload.json out_dir pages_dir
"""
import json, os, subprocess, sys, urllib.request

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
