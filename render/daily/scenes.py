# Flat SVG illustrations for 일상 수사대 scenes. Each returns SVG body for viewBox 0 0 1080 900.
GOLD, RED, SKY, LIGHT, MID, DARK, WHITE = '#e8b84a', '#e5484d', '#8fb8ef', '#d9dee8', '#9aa6ba', '#1b2a4a', '#f4f6fb'


def person(x, y, s=1.0, c=GOLD, head=None):
    head = head or c
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<circle cx="0" cy="-95" r="34" fill="{head}"/>'
            f'<rect x="-38" y="-52" width="76" height="120" rx="34" fill="{c}"/></g>')


def child(x, y, s=1.0, c=GOLD):
    return person(x, y, s * 0.68, c)


def flame(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M0,-120 C40,-70 70,-40 60,10 C55,50 25,70 0,70 C-25,70 -55,50 -60,10 C-65,-30 -30,-50 -20,-90 C-10,-60 5,-55 0,-120Z" fill="{RED}"/>'
            f'<path d="M0,-40 C20,-15 35,5 30,30 C25,52 12,60 0,60 C-12,60 -25,52 -30,30 C-33,10 -15,-5 0,-40Z" fill="{GOLD}"/></g>')


def cloud(x, y, s=1.0, c='#3a4256'):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{c}">'
            f'<circle cx="-60" cy="0" r="55"/><circle cx="0" cy="-30" r="70"/><circle cx="70" cy="0" r="55"/>'
            f'<rect x="-110" y="0" width="230" height="55" rx="27"/></g>')


def bench(x, y, steel=False):
    if steel:
        seats = ''.join(f'<rect x="{x + i * 140}" y="{y}" width="128" height="40" rx="12" fill="url(#steel)"/>'
                        f'<rect x="{x + i * 140}" y="{y - 150}" width="128" height="140" rx="16" fill="url(#steel)"/>'
                        f'<line x1="{x + i * 140 + 20}" y1="{y - 130}" x2="{x + i * 140 + 20}" y2="{y - 30}" stroke="#ffffff" stroke-opacity=".5" stroke-width="6"/>'
                        for i in range(5))
    else:
        seats = ''.join(f'<rect x="{x + i * 140}" y="{y - 10}" width="128" height="60" rx="26" fill="#3d6fd0"/>'
                        f'<rect x="{x + i * 140}" y="{y - 160}" width="128" height="150" rx="30" fill="#4f82e3"/>'
                        f'<path d="M{x + i * 140 + 20},{y - 120} h88 M{x + i * 140 + 20},{y - 80} h88" stroke="#7fa6f0" stroke-width="5"/>'
                        for i in range(5))
    return seats + f'<rect x="{x - 20}" y="{y + 50}" width="730" height="24" rx="8" fill="{MID}"/>'


def train(x, y, w=860, fire=False):
    win = ''.join(f'<rect x="{x + 70 + i * 190}" y="{y + 50}" width="140" height="110" rx="14" fill="{"#f2a35a" if fire else SKY}"/>' for i in range(4))
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="330" rx="40" fill="{LIGHT}"/>' + win +
           f'<rect x="{x}" y="{y + 200}" width="{w}" height="22" fill="{RED if not fire else "#b33a3e"}"/>'
           f'<circle cx="{x + 160}" cy="{y + 345}" r="30" fill="#55607a"/><circle cx="{x + w - 160}" cy="{y + 345}" r="30" fill="#55607a"/>')
    return out


def doc(x, y, stamp_txt='법', c=GOLD):
    lines = ''.join(f'<rect x="{x + 60}" y="{y + 90 + i * 60}" width="{280 - (i % 2) * 70}" height="18" rx="9" fill="{MID}"/>' for i in range(5))
    return (f'<rect x="{x}" y="{y}" width="400" height="520" rx="26" fill="{WHITE}"/>' + lines +
            f'<circle cx="{x + 330}" cy="{y + 440}" r="80" fill="none" stroke="{c}" stroke-width="14"/>'
            f'<text x="{x + 330}" y="{y + (470 if len(stamp_txt) == 1 else 460)}" font-size="{86 if len(stamp_txt) == 1 else 54}" font-weight="900" fill="{c}" text-anchor="middle" font-family="Noto Sans CJK KR">{stamp_txt}</text>')


def door(x, y, color=LIGHT, open_dir=None, bar=False, bolt=False):
    s = f'<rect x="{x - 20}" y="{y - 20}" width="340" height="600" rx="10" fill="#33415f"/>'
    s += f'<rect x="{x}" y="{y}" width="300" height="580" rx="8" fill="{color}"/>'
    if bar:
        s += f'<rect x="{x + 30}" y="{y + 300}" width="240" height="34" rx="17" fill="{GOLD}"/>'
    else:
        s += f'<circle cx="{x + 250}" cy="{y + 310}" r="18" fill="{MID}"/>'
    if bolt:
        s += f'<rect x="{x + 200}" y="{y + 160}" width="160" height="34" rx="10" fill="{RED}"/><rect x="{x + 230}" y="{y + 140}" width="30" height="74" rx="8" fill="{RED}"/>'
    if open_dir == 'in':
        s += arrow(x + 400, y + 300, x + 200, y + 300, RED)
    if open_dir == 'out':
        s += arrow(x + 150, y + 300, x + 460, y + 300, GOLD)
    return s


def arrow(x1, y1, x2, y2, c=GOLD, w=22):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 50 * math.cos(a), y2 - 50 * math.sin(a)
    p1 = (hx + 32 * math.sin(a), hy - 32 * math.cos(a)); p2 = (hx - 32 * math.sin(a), hy + 32 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx}" y2="{hy}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{c}"/>')


def fridge(x, y, handle='latch', open_=False):
    s = f'<rect x="{x}" y="{y}" width="380" height="720" rx="40" fill="{WHITE}"/>'
    s += f'<line x1="{x}" y1="{y + 250}" x2="{x + 380}" y2="{y + 250}" stroke="{MID}" stroke-width="8"/>'
    if handle == 'latch':
        s += f'<rect x="{x + 300}" y="{y + 360}" width="70" height="120" rx="14" fill="#8a94a8"/><rect x="{x + 340}" y="{y + 395}" width="70" height="40" rx="10" fill="#6c7790"/>'
    else:
        s += f'<rect x="{x + 330}" y="{y + 300}" width="22" height="200" rx="11" fill="{MID}"/>'
        s += f'<rect x="{x + 372}" y="{y + 20}" width="16" height="680" rx="8" fill="{GOLD}"/>'
    if open_:
        s += f'<polygon points="{x + 380},{y} {x + 520},{y + 70} {x + 520},{y + 650} {x + 380},{y + 720}" fill="#c8d0de"/>'
        s += arrow(x + 200, y + 480, x + 470, y + 480, GOLD)
    return s


def bottle(x, y, foil='seal'):
    s = (f'<rect x="{x - 150}" y="{y}" width="300" height="420" rx="50" fill="#e8a24a"/>'
         f'<rect x="{x - 110}" y="{y + 120}" width="220" height="180" rx="16" fill="{WHITE}"/>'
         f'<rect x="{x - 90}" y="{y - 60}" width="180" height="70" rx="14" fill="#c98a3a"/>')
    if foil == 'seal':
        s += f'<ellipse cx="{x}" cy="{y - 70}" rx="100" ry="26" fill="url(#foil)"/>'
    elif foil == 'torn':
        s += f'<path d="M{x - 100},{y - 70} q30,-40 60,-10 l30,-30 l25,35 l40,-10 z" fill="url(#foil)"/>'
    s += f'<rect x="{x - 70}" y="{y + 180}" width="140" height="22" rx="11" fill="{MID}"/><rect x="{x - 50}" y="{y + 230}" width="100" height="18" rx="9" fill="{MID}"/>'
    return s


def capsule(x, y, s=1.0, rot=-30, c2=RED):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            f'<rect x="-160" y="-60" width="160" height="120" rx="60" fill="{WHITE}"/>'
            f'<rect x="0" y="-60" width="160" height="120" rx="60" fill="{c2}"/><rect x="-10" y="-60" width="40" height="120" fill="{c2}"/></g>')


def mask(x, y, c=GOLD):
    return (f'<path d="M{x},{y - 400} L{x},{y - 90}" stroke="{MID}" stroke-width="6"/>'
            f'<path d="M{x - 70},{y - 90} Q{x},{y - 140} {x + 70},{y - 90} L{x + 50},{y} Q{x},{y + 20} {x - 50},{y} Z" fill="{c}"/>')


def stopwatch(x, y, frac=1.0, c=RED, label=''):
    import math
    a = 2 * math.pi * frac
    ex, ey = x + 190 * math.sin(a), y - 190 * math.cos(a)
    large = 1 if frac > 0.5 else 0
    wedge = (f'<path d="M{x},{y} L{x},{y - 190} A190,190 0 {large},1 {ex:.0f},{ey:.0f} Z" fill="{c}" fill-opacity=".85"/>' if frac < 0.999 else f'<circle cx="{x}" cy="{y}" r="190" fill="{c}" fill-opacity=".85"/>')
    return (f'<rect x="{x - 40}" y="{y - 300}" width="80" height="60" rx="14" fill="{LIGHT}"/>'
            f'<circle cx="{x}" cy="{y}" r="240" fill="{LIGHT}"/><circle cx="{x}" cy="{y}" r="210" fill="{DARK}"/>' + wedge +
            (f'<text x="{x}" y="{y + 30}" font-size="96" font-weight="900" fill="{WHITE}" text-anchor="middle" font-family="Noto Sans CJK KR">{label}</text>' if label else ''))


def seat_person(x, y, belt='none', lean=0):
    s = f'<rect x="{x - 180}" y="{y - 330}" width="120" height="420" rx="40" fill="#55607a"/>'  # seat back
    s += f'<rect x="{x - 180}" y="{y + 40}" width="380" height="90" rx="30" fill="#55607a"/>'
    s += f'<g transform="rotate({lean},{x - 60},{y + 60})">' + person(x - 40, y - 20, 1.6, GOLD) + '</g>'
    if belt in ('lap', '3pt'):
        s += f'<rect x="{x - 150}" y="{y + 40}" width="290" height="32" rx="14" fill="{RED if belt == "lap" else LIGHT}"/>'
    if belt == '3pt':
        s += f'<line x1="{x + 10}" y1="{y - 210}" x2="{x - 130}" y2="{y + 50}" stroke="{LIGHT}" stroke-width="32" stroke-linecap="round"/>'
    return s


def car(x, y, c='#4f82e3', s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-200,0 L-160,-80 Q-140,-110 -100,-110 L80,-110 Q120,-110 150,-70 L200,-20 L200,40 L-200,40 Z" fill="{c}"/>'
            f'<rect x="-130" y="-95" width="110" height="65" rx="10" fill="{SKY}"/><rect x="0" y="-95" width="110" height="65" rx="10" fill="{SKY}"/>'
            f'<circle cx="-120" cy="45" r="40" fill="#2b3245"/><circle cx="120" cy="45" r="40" fill="#2b3245"/></g>')


def stairs(x, y):
    return ''.join(f'<rect x="{x + i * 90}" y="{y + i * 70}" width="{600 - i * 90}" height="70" fill="{"#5c6a88" if i % 2 else "#6d7c9c"}"/>' for i in range(6))


def toybox(x, y):
    return (f'<rect x="{x - 260}" y="{y - 260}" width="520" height="440" rx="20" fill="#e3a250"/>'
            f'<rect x="{x - 260}" y="{y - 260}" width="520" height="70" fill="#cf8c3c"/>'
            f'<circle cx="{x - 90}" cy="{y - 40}" r="70" fill="{SKY}"/><rect x="{x + 20}" y="{y - 110}" width="140" height="140" rx="20" fill="{RED}"/>'
            f'<rect x="{x - 200}" y="{y + 70}" width="400" height="80" rx="16" fill="{WHITE}"/>'
            f'<text x="{x}" y="{y + 128}" font-size="52" font-weight="900" fill="{RED}" text-anchor="middle" font-family="Noto Sans CJK KR">3세 미만 금지</text>')


def cylinder(x, y, part=False, inside=False):
    s = (f'<rect x="{x - 110}" y="{y - 300}" width="220" height="420" fill="#c8d6ee" fill-opacity=".35" stroke="{LIGHT}" stroke-width="8"/>'
         f'<ellipse cx="{x}" cy="{y - 300}" rx="110" ry="30" fill="#c8d6ee" fill-opacity=".5" stroke="{LIGHT}" stroke-width="8"/>'
         f'<ellipse cx="{x}" cy="{y + 120}" rx="110" ry="30" fill="#c8d6ee" fill-opacity=".3" stroke="{LIGHT}" stroke-width="8"/>')
    if part:
        py = y - 20 if inside else y - 420
        s += f'<rect x="{x - 45}" y="{py}" width="90" height="90" rx="14" fill="{RED}"/><circle cx="{x}" cy="{py - 20}" r="22" fill="{RED}"/>'
        if not inside:
            s += arrow(x, y - 300, x, y - 120, GOLD, 16)
    s += f'<line x1="{x - 110}" y1="{y + 200}" x2="{x + 110}" y2="{y + 200}" stroke="{GOLD}" stroke-width="8"/>'
    s += f'<text x="{x}" y="{y + 270}" font-size="54" font-weight="900" fill="{GOLD}" text-anchor="middle" font-family="Noto Sans CJK KR">약 3.2cm</text>'
    return s


def house_school(x, y, glow=False):
    s = (f'<polygon points="{x - 330},{y - 180} {x},{y - 380} {x + 330},{y - 180}" fill="#b45a4a"/>'
         f'<rect x="{x - 300}" y="{y - 180}" width="600" height="380" fill="#d98b6b"/>')
    s += ''.join(f'<rect x="{x - 250 + i * 140}" y="{y - 120}" width="90" height="100" rx="8" fill="{"#f2c66a" if glow else SKY}"/>' for i in range(4))
    s += f'<rect x="{x - 50}" y="{y + 40}" width="100" height="160" fill="#7a4033"/>'
    s += f'<rect x="{x - 330}" y="{y + 200}" width="660" height="140" fill="#3b445c"/>'
    return s


def scene_svg(key, ep):
    S = ''
    if key == 'seat_soft':
        S = bench(200, 600)
    elif key == 'seat_steel':
        S = bench(200, 600, steel=True)
    elif key == 'seat_shield':
        S = bench(200, 640, steel=True) + f'<path d="M540,90 L700,150 L700,300 Q700,420 540,480 Q380,420 380,300 L380,150 Z" fill="{GOLD}"/><path d="M470,290 l50,50 l100,-110" stroke="{DARK}" stroke-width="30" fill="none" stroke-linecap="round"/>'
    elif key == 'train_fire':
        S = train(110, 300) + flame(560, 360, 1.3)
    elif key == 'train_fire2':
        S = train(110, 300, fire=True) + flame(330, 360, 1.1) + flame(560, 340, 1.4) + flame(790, 360, 1.1)
    elif key == 'smoke':
        S = train(110, 420, fire=True) + cloud(320, 260, 1.4) + cloud(700, 220, 1.6, '#2c3346') + cloud(520, 120, 1.2, '#444d63')
    elif key == 'number':
        S = ''
    elif key == 'law':
        S = doc(340, 160)
    elif key == 'thermo':
        S = (f'<rect x="490" y="120" width="100" height="560" rx="50" fill="{LIGHT}"/><circle cx="540" cy="720" r="110" fill="{LIGHT}"/>'
             f'<rect x="515" y="200" width="50" height="520" rx="25" fill="{RED}"/><circle cx="540" cy="720" r="85" fill="{RED}"/>')
    elif key == 'nose_none':
        S = (f'<path d="M560,180 Q470,420 430,520 Q420,580 500,590 L600,590" stroke="{LIGHT}" stroke-width="34" fill="none" stroke-linecap="round"/>'
             f'<circle cx="720" cy="420" r="130" fill="none" stroke="{MID}" stroke-width="20" stroke-dasharray="30 22"/>')
    elif key == 'nose_warn':
        S = (f'<path d="M420,180 Q330,420 290,520 Q280,580 360,590 L460,590" stroke="{LIGHT}" stroke-width="34" fill="none" stroke-linecap="round"/>'
             + ''.join(f'<path d="M{560 + i * 70},{560 - i * 10} q30,-60 0,-120 q-30,-60 0,-120" stroke="#9ccf6a" stroke-width="18" fill="none" stroke-linecap="round"/>' for i in range(3))
             + f'<polygon points="880,150 1010,380 750,380" fill="{RED}"/><rect x="868" y="220" width="24" height="90" rx="10" fill="{WHITE}"/><circle cx="880" cy="345" r="14" fill="{WHITE}"/>')
    elif key == 'school':
        S = house_school(540, 520)
    elif key == 'school_gas':
        S = house_school(540, 520) + ''.join(f'<circle cx="{300 + i * 95}" cy="{780 - (i % 3) * 30}" r="{22 + (i % 2) * 10}" fill="#9ccf6a" fill-opacity=".55"/>' for i in range(6))
    elif key == 'school_boom':
        S = house_school(540, 560) + flame(540, 420, 2.2) + ''.join(f'<path d="M540,420 L{540 + dx},{420 + dy}" stroke="{GOLD}" stroke-width="14" stroke-linecap="round"/>' for dx, dy in [(-380, -200), (380, -200), (-420, 40), (420, 40), (0, -380)])
    elif key == 'map_spread':
        pts = [(300, 300), (520, 220), (760, 300), (420, 520), (680, 560), (540, 400)]
        S = ''.join(f'<circle cx="{x}" cy="{y}" r="{60 if i == 5 else 40}" fill="{GOLD if i == 5 else LIGHT}"/>' for i, (x, y) in enumerate(pts))
        S += ''.join(f'<line x1="540" y1="400" x2="{x}" y2="{y}" stroke="{GOLD}" stroke-width="8" stroke-dasharray="18 14"/>' for x, y in pts[:5])
    elif key == 'valve_window':
        S = (f'<rect x="130" y="180" width="380" height="480" rx="16" fill="#33415f"/><rect x="150" y="200" width="160" height="440" fill="{SKY}"/>'
             f'<polygon points="330,200 500,170 500,670 330,640" fill="{LIGHT}"/>'
             f'<rect x="620" y="420" width="360" height="56" rx="20" fill="{MID}"/><rect x="760" y="300" width="56" height="130" rx="14" fill="{RED}"/>'
             f'<rect x="700" y="270" width="180" height="56" rx="20" fill="{RED}"/>')
    elif key == 'hall':
        S = (f'<rect x="200" y="260" width="680" height="480" fill="#8a6f5a"/><polygon points="160,260 540,80 920,260" fill="#6e5848"/>'
             + ''.join(f'<rect x="{260 + i * 150}" y="340" width="90" height="180" rx="45" fill="#f2c66a"/>' for i in range(4))
             + f'<rect x="470" y="580" width="140" height="160" rx="10" fill="#4a3a30"/>')
    elif key == 'kids_stairs':
        S = stairs(160, 300) + ''.join(child(260 + i * 85, 300 + i * 70 - 10, 0.9) for i in range(6))
    elif key == 'door_in':
        S = door(380, 160, open_dir='in')
    elif key == 'door_bolt':
        S = door(380, 160, bolt=True) + child(260, 640, 1.0)
    elif key == 'crowd_push':
        S = door(560, 160) + ''.join(child(120 + (i % 4) * 110, 380 + (i // 4) * 170, 0.8) for i in range(12)) + arrow(120, 300, 520, 300, RED)
    elif key == 'push_bar':
        S = door(380, 160, bar=True) + arrow(480, 120, 480, 300, GOLD, 18)
    elif key == 'door_out':
        S = door(220, 160, bar=True, open_dir='out') + ''.join(child(720 + i * 90, 700, 0.8) for i in range(3))
    elif key in ('fridge_latch', 'fridge_locked'):
        S = fridge(350, 90)
        if key == 'fridge_locked':
            S += f'<circle cx="540" cy="560" r="70" fill="none" stroke="{RED}" stroke-width="18"/><line x1="490" y1="610" x2="590" y2="510" stroke="{RED}" stroke-width="18"/>'
    elif key == 'kids_hide':
        S = fridge(470, 90) + child(260, 720, 1.0) + child(380, 740, 0.85) + f'<text x="300" y="380" font-size="110" font-weight="900" fill="{GOLD}" font-family="Noto Sans CJK KR">?</text>'
    elif key == 'fridge_magnet':
        S = fridge(350, 90, handle='magnet') + f'<text x="830" y="420" font-size="84" font-weight="900" fill="{GOLD}" font-family="DejaVu Sans">N S</text>'
    elif key == 'fridge_open':
        S = fridge(260, 90, handle='magnet', open_=True)
    elif key == 'fridge_shield':
        S = fridge(220, 90, handle='magnet') + f'<path d="M780,180 L930,240 L930,380 Q930,490 780,550 Q630,490 630,380 L630,240 Z" fill="{GOLD}"/><path d="M710,370 l45,45 l90,-100" stroke="{DARK}" stroke-width="28" fill="none" stroke-linecap="round"/>'
    elif key in ('bottle_foil', 'bottle_foil2'):
        S = bottle(540, 340)
        if key == 'bottle_foil2':
            S += f'<ellipse cx="540" cy="270" rx="150" ry="40" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="20 14"/>'
    elif key == 'capsule':
        S = capsule(420, 440, 1.3) + capsule(700, 360, 1.0, 20)
    elif key == 'capsule_poison':
        S = capsule(540, 480, 1.6) + f'<path d="M620,120 Q560,220 560,260 A60,60 0 0 0 680,260 Q680,220 620,120Z" fill="#9ccf6a"/>'
    elif key == 'recall':
        S = ''.join(f'<rect x="{180 + (i % 5) * 150}" y="{220 + (i // 5) * 170}" width="110" height="140" rx="22" fill="#e8a24a"/><rect x="{195 + (i % 5) * 150}" y="{195 + (i // 5) * 170}" width="80" height="34" rx="8" fill="#c98a3a"/>' for i in range(15)) + arrow(540, 760, 540, 860, GOLD)
    elif key == 'foil_torn':
        S = bottle(540, 340, foil='torn') + f'<circle cx="820" cy="260" r="90" fill="none" stroke="{RED}" stroke-width="18"/><line x1="756" y1="324" x2="884" y2="196" stroke="{RED}" stroke-width="18"/>'
    elif key in ('mask_family', 'mask_both'):
        S = mask(400, 420) + mask(700, 420) + person(400, 780, 1.6, LIGHT) + child(700, 800, 1.5, LIGHT)
        if key == 'mask_both':
            S = mask(400, 420) + mask(700, 420) + person(400, 780, 1.6, GOLD) + child(700, 800, 1.5, GOLD) + f'<text x="400" y="200" font-size="80" font-weight="900" fill="{GOLD}" text-anchor="middle" font-family="DejaVu Sans">1</text><text x="700" y="200" font-size="80" font-weight="900" fill="{GOLD}" text-anchor="middle" font-family="DejaVu Sans">2</text>'
    elif key == 'altitude':
        S = (f'<polygon points="80,840 360,420 520,620 700,360 1000,840" fill="#33415f"/>'
             f'<line x1="120" y1="200" x2="960" y2="200" stroke="{GOLD}" stroke-width="6" stroke-dasharray="20 14"/>'
             f'<g transform="translate(700,170)"><path d="M-120,0 L120,0 L150,-20 L120,15 L-110,15 Z" fill="{LIGHT}"/><path d="M-20,0 L40,-70 L70,-70 L40,0Z" fill="{LIGHT}"/></g>'
             f'<text x="140" y="180" font-size="54" font-weight="900" fill="{GOLD}" font-family="DejaVu Sans">12,000 m</text>'
             + ''.join(f'<circle cx="{200 + i * 130}" cy="{300 + (i % 2) * 40}" r="10" fill="{LIGHT}" fill-opacity=".5"/>' for i in range(6)))
    elif key == 'timer':
        S = stopwatch(540, 480, 0.75)
    elif key == 'timer_half':
        S = stopwatch(540, 480, 0.375)
    elif key == 'faint':
        S = mask(380, 420) + f'<g transform="rotate(-28,400,800)">' + person(400, 790, 1.6, MID) + '</g>' + child(720, 800, 1.5, MID) + f'<text x="420" y="440" font-size="90" fill="{RED}" font-weight="900" font-family="DejaVu Sans">!</text>'
    elif key == 'belt_lap':
        S = seat_person(560, 520, 'lap')
    elif key == 'belt_lap_crash':
        S = seat_person(560, 520, 'lap', lean=32) + arrow(700, 260, 940, 260, RED)
    elif key == 'belt_3pt':
        S = seat_person(560, 520, '3pt')
    elif key == 'belt_3pt_hold':
        S = seat_person(560, 520, '3pt') + f'<path d="M780,200 L930,260 L930,400 Q930,510 780,570 Q630,510 630,400 L630,260 Z" fill="{GOLD}" fill-opacity=".9"/><path d="M710,390 l45,45 l90,-100" stroke="{DARK}" stroke-width="28" fill="none" stroke-linecap="round"/>'
    elif key == 'patent_open':
        S = doc(200, 160, '특허', GOLD) + (f'<rect x="680" y="420" width="240" height="200" rx="26" fill="{GOLD}"/>'
                                         f'<path d="M720,420 V320 A80,80 0 0 1 880,320 V300" stroke="{GOLD}" stroke-width="30" fill="none"/>')
    elif key == 'globe_cars':
        S = (f'<circle cx="540" cy="460" r="300" fill="#2f6fb5"/><path d="M380,300 q80,-60 160,0 t120,80 q-40,80 -140,60 t-140,-140z M600,520 q80,-20 120,40 q-40,90 -120,60z" fill="#5fb07a"/>'
             + car(230, 820, '#4f82e3', 0.55) + car(540, 840, GOLD, 0.55) + car(850, 820, RED, 0.55))
    elif key == 'back_seat':
        S = car(540, 560, '#4f82e3', 1.9) + f'<line x1="300" y1="380" x2="250" y2="480" stroke="{GOLD}" stroke-width="20" stroke-linecap="round"/>'
    elif key == 'toy_box':
        S = toybox(540, 520)
    elif key == 'cylinder':
        S = cylinder(540, 480)
    elif key == 'cylinder_in':
        S = cylinder(540, 480, part=True, inside=True)
    elif key == 'throat':
        S = (f'<path d="M420,140 Q300,160 290,300 Q280,360 240,420 Q300,450 300,500 Q290,560 360,580 L380,760" stroke="{LIGHT}" stroke-width="26" fill="none" stroke-linecap="round"/>'
             f'<ellipse cx="560" cy="560" rx="70" ry="22" fill="none" stroke="{RED}" stroke-width="12"/>'
             f'<line x1="490" y1="620" x2="630" y2="620" stroke="{GOLD}" stroke-width="8"/>')
    elif key == 'choke':
        S = (f'<path d="M420,140 Q300,160 290,300 Q280,360 240,420 Q300,450 300,500 Q290,560 360,580 L380,760" stroke="{LIGHT}" stroke-width="26" fill="none" stroke-linecap="round"/>'
             f'<rect x="500" y="500" width="110" height="110" rx="18" fill="{RED}"/>'
             f'<polygon points="800,260 930,490 670,490" fill="{RED}"/><rect x="788" y="330" width="24" height="90" rx="10" fill="{WHITE}"/><circle cx="800" cy="455" r="14" fill="{WHITE}"/>')
    elif key == 'shelf_high':
        S = (f'<rect x="460" y="220" width="520" height="30" rx="10" fill="#8a94a8"/>'
             f'<rect x="520" y="140" width="80" height="80" rx="12" fill="{RED}"/><circle cx="700" cy="180" r="40" fill="{SKY}"/><rect x="800" y="150" width="90" height="70" rx="12" fill="{GOLD}"/>'
             + child(300, 800, 1.6, LIGHT) + arrow(300, 520, 300, 300, MID, 12))
    else:
        raise KeyError(key)
    return S


DEFS = (f'<defs><linearGradient id="steel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#eef2f7"/><stop offset=".5" stop-color="#aab4c4"/><stop offset="1" stop-color="#d7dde7"/></linearGradient>'
        f'<linearGradient id="foil" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#cfd5df"/><stop offset=".5" stop-color="#ffffff"/><stop offset="1" stop-color="#b9c1ce"/></linearGradient></defs>')
