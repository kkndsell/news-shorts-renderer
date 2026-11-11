# Scenes for 일상 수사대 031~038 (light, everyday objects). viewBox 0 0 1080 900.
import math
from scenes import person, arrow, doc, car, GOLD, RED, SKY, LIGHT, MID, DARK, WHITE

F = 'font-family="Noto Sans CJK KR"'


def txt(x, y, s, size=60, c=WHITE, w=900, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{anchor}" {F}>{s}</text>'


def shield(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0,-150 L140,-95 L140,30 Q140,130 0,185 Q-140,130 -140,30 L-140,-95 Z" fill="{GOLD}"/>'
            f'<path d="M-60,20 l45,45 l90,-100" stroke="{DARK}" stroke-width="28" fill="none" stroke-linecap="round"/></g>')


def qmark(x=540, y=450, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="230" fill="none" stroke="{GOLD}" stroke-width="18"/>'
            + txt(0, 95, '?', 300, GOLD) + '</g>')


def bubble(x, y, s, c=GOLD):
    return (f'<rect x="{x - 110}" y="{y - 80}" width="220" height="140" rx="40" fill="{WHITE}"/>'
            f'<polygon points="{x - 40},{y + 55} {x - 80},{y + 110} {x},{y + 58}" fill="{WHITE}"/>' + txt(x, y + 25, s, 90, c))


# ---------- airplane lavatory ----------
def lav_door(x=390, y=120, sign='down', crack=False):
    s = f'<rect x="{x - 20}" y="{y - 20}" width="340" height="700" rx="14" fill="#33415f"/>'
    s += f'<rect x="{x}" y="{y}" width="300" height="660" rx="10" fill="{LIGHT}"/>'
    s += ''.join(f'<line x1="{x + 150}" y1="{y + 10}" x2="{x + 150}" y2="{y + 650}" stroke="{MID}" stroke-width="6"/>' for _ in [0])  # bi-fold line
    s += f'<rect x="{x + 230}" y="{y + 320}" width="40" height="90" rx="12" fill="{MID}"/>'  # handle
    s += f'<rect x="{x + 40}" y="{y + 330}" width="90" height="40" rx="10" fill="#4caf7a"/>'  # vacant indicator
    if sign == 'down':
        s += f'<rect x="{x + 30}" y="{y + 60}" width="240" height="70" rx="10" fill="#c8ced9" stroke="{MID}" stroke-width="4"/>' + txt(x + 150, y + 108, 'LAVATORY', 34, DARK, 800)
    else:
        s += f'<rect x="{x + 30}" y="{y - 10}" width="240" height="60" rx="10" fill="#c8ced9" stroke="{MID}" stroke-width="4" transform="skewX(-12)"/>'
        s += f'<rect x="{x + 40}" y="{y + 70}" width="220" height="60" rx="8" fill="#2b3245"/><rect x="{x + 70}" y="{y + 86}" width="70" height="28" rx="8" fill="{GOLD}"/>'
    return s


def scene_lav(key):
    if key == 'lav_door':
        return lav_door() + f'<circle cx="540" cy="215" r="150" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="24 16"/>'
    if key == 'lav_sign_up':
        return lav_door(sign='up') + arrow(700, 260, 700, 80, GOLD, 18)
    if key == 'lav_latch':
        return (f'<rect x="160" y="200" width="760" height="420" rx="30" fill="#2b3245"/>'
                f'<rect x="200" y="120" width="680" height="110" rx="16" fill="#c8ced9" transform="rotate(-6,540,175)"/>' + txt(540, 200, 'LAVATORY', 58, DARK, 800)
                + f'<rect x="300" y="360" width="200" height="90" rx="20" fill="{GOLD}"/>' + arrow(520, 405, 800, 405, GOLD, 22))
    if key == 'lav_crew':
        return lav_door(x=480, sign='up') + person(260, 700, 2.0, GOLD) + f'<line x1="300" y1="560" x2="520" y2="210" stroke="{GOLD}" stroke-width="16" stroke-linecap="round"/>'
    if key == 'lav_help':
        return lav_door() + bubble(840, 260, '!', RED)
    if key == 'lav_locked':
        return (lav_door() + f'<rect x="760" y="380" width="160" height="130" rx="20" fill="{MID}"/><path d="M790,380 v-50 a50,50 0 0 1 100,0 v50" stroke="{MID}" stroke-width="22" fill="none"/>'
                + ''.join(f'<path d="M{330 - i * 30},{300 + i * 40} q-20,20 0,40" stroke="{GOLD}" stroke-width="8" fill="none"/>' for i in range(3)))
    if key == 'lav_shield':
        return lav_door(x=220) + shield(780, 420, 1.2)


# ---------- fuel gauge arrow ----------
def gauge(x=540, y=520, s=1.0, hi=False, side='left'):
    out = f'<g transform="translate({x},{y}) scale({s})">'
    out += f'<path d="M-300,0 A300,300 0 0 1 300,0" fill="none" stroke="{LIGHT}" stroke-width="26" stroke-linecap="round"/>'
    out += txt(-300, 80, 'E', 70, RED) + txt(300, 80, 'F', 70, WHITE)
    out += f'<line x1="0" y1="0" x2="-170" y2="-170" stroke="{RED}" stroke-width="18" stroke-linecap="round"/><circle r="30" fill="{LIGHT}"/>'
    # pump icon
    out += f'<rect x="-60" y="-200" width="80" height="110" rx="10" fill="{WHITE}"/><rect x="-46" y="-186" width="52" height="34" rx="6" fill="{DARK}"/><path d="M20,-170 h30 v60" stroke="{WHITE}" stroke-width="12" fill="none"/>'
    ax = -110 if side == 'left' else 110
    pts = f'{ax},-160 {ax + (40 if side == "left" else -40)},-185 {ax + (40 if side == "left" else -40)},-135'
    out += f'<polygon points="{pts}" fill="{GOLD if hi else WHITE}"/>'
    if hi:
        out += f'<circle cx="{ax + (20 if side == "left" else -20)}" cy="-160" r="62" fill="none" stroke="{GOLD}" stroke-width="10"/>'
    return out + '</g>'


def pump(x, y):
    return (f'<rect x="{x - 80}" y="{y - 300}" width="160" height="300" rx="16" fill="{RED}"/><rect x="{x - 55}" y="{y - 270}" width="110" height="80" rx="10" fill="{DARK}"/>'
            f'<path d="M{x + 80},{y - 200} q70,0 70,80 v80" stroke="#2b3245" stroke-width="16" fill="none"/>')


def car_cap(x, y, s, cap_side='right', c='#4f82e3'):
    cx = x + (150 if cap_side == 'right' else -150) * s
    return car(x, y, c, s) + f'<circle cx="{cx}" cy="{y - 30 * s}" r="{18 * s}" fill="{GOLD}"/>'


def scene_fuel(key):
    if key in ('gauge_arrow', 'fuel_gauge'):
        return gauge(hi=key == 'gauge_arrow')
    if key == 'gauge_arrow2':
        return gauge(540, 420, 0.8, True) + car_cap(540, 800, 1.0, 'left')
    if key == 'car_sides':
        return (gauge(540, 330, 0.55, True) + car_cap(540, 700, 1.4, 'left') + arrow(330, 650, 160, 650, GOLD, 18))
    if key == 'designer':
        return (person(330, 720, 2.2, GOLD) + f'<rect x="520" y="300" width="380" height="300" rx="16" fill="{WHITE}" transform="rotate(-8,710,450)"/>'
                + gauge(710, 520, 0.42, True))
    if key == 'gas_station':
        return pump(260, 760) + car_cap(680, 700, 1.4, 'right') + txt(540, 200, '1986', 120, GOLD)
    if key == 'car_wrong_side':
        return (pump(200, 760) + car_cap(640, 700, 1.4, 'right')
                + f'<circle cx="400" cy="380" r="80" fill="none" stroke="{RED}" stroke-width="16"/><line x1="345" y1="435" x2="455" y2="325" stroke="{RED}" stroke-width="16"/>')
    if key == 'memo':
        return doc(200, 160, '제안', GOLD) + gauge(800, 520, 0.35, True)
    if key == 'cars_many':
        return car_cap(250, 760, 0.7) + car_cap(540, 760, 0.7, 'left', GOLD) + car_cap(830, 760, 0.7, 'right', RED) + gauge(540, 420, 0.6, True)


# ---------- pencils ----------
def pencil(x, y, ang=0, s=1.0, hexa=True, c=GOLD):
    body = (f'<rect x="-260" y="-34" width="420" height="68" fill="{c}"/>'
            + (f'<line x1="-260" y1="-11" x2="160" y2="-11" stroke="#c9952c" stroke-width="6"/><line x1="-260" y1="12" x2="160" y2="12" stroke="#c9952c" stroke-width="6"/>' if hexa else '')
            + f'<polygon points="160,-34 260,0 160,34" fill="#f2d3a0"/><polygon points="228,-11 260,0 228,11" fill="#333"/>'
            f'<rect x="-310" y="-34" width="50" height="68" fill="#c8ced9"/><rect x="-360" y="-34" width="54" height="68" rx="14" fill="#f08a9a"/>')
    return f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">{body}</g>'


def hexagon(cx, cy, r, c=GOLD):
    p = ' '.join(f'{cx + r * math.cos(math.radians(60 * k)):.0f},{cy + r * math.sin(math.radians(60 * k)):.0f}' for k in range(6))
    return f'<polygon points="{p}" fill="{c}"/>'


def scene_pencil(key):
    desk = f'<rect x="80" y="620" width="760" height="40" rx="10" fill="#8a6f5a"/><rect x="100" y="660" width="40" height="220" fill="#6e5848"/>'
    if key == 'pencils':
        return pencil(540, 420, -20) + pencil(560, 520, -5, 1, True, '#4f82e3') + pencil(540, 620, 10, 1, True, RED)
    if key == 'pencil_desk':
        return desk + pencil(460, 586, 0, 1.0) + f'<path d="M760,560 l40,40 l80,-90" stroke="{GOLD}" stroke-width="24" fill="none" stroke-linecap="round"/>'
    if key == 'pencil_roll':
        return (desk + f'<circle cx="900" cy="700" r="40" fill="#4f82e3"/><circle cx="900" cy="700" r="12" fill="#333"/>'
                + arrow(560, 590, 820, 640, MID, 14) + ''.join(f'<path d="M{930 + i * 30},{640 + i * 20} q20,20 0,40" stroke="{MID}" stroke-width="8" fill="none"/>' for i in range(3)))
    if key == 'pencil_grip':
        return (pencil(540, 470, -35, 1.2) + f'<ellipse cx="470" cy="520" rx="70" ry="44" fill="#f1c9a5"/><ellipse cx="560" cy="440" rx="70" ry="44" fill="#f1c9a5"/><ellipse cx="610" cy="560" rx="60" ry="40" fill="#e8b994"/>')
    if key == 'slat':
        return (f'<rect x="140" y="340" width="800" height="200" rx="10" fill="#c99a63"/>'
                + ''.join(f'<path d="M{190 + i * 88},540 a36,36 0 0 1 72,0" fill="#8a6038"/>' for i in range(9)))
    if key == 'slat_count':
        s = f'<rect x="100" y="180" width="880" height="160" rx="10" fill="#c99a63"/>' + ''.join(f'<circle cx="{170 + i * 106}" cy="260" r="48" fill="#4f82e3"/>' for i in range(8))
        s += f'<rect x="100" y="520" width="880" height="160" rx="10" fill="#c99a63"/>' + ''.join(hexagon(156 + i * 96, 600, 50) for i in range(9))
        return s + txt(540, 150, '8자루', 64, WHITE) + txt(540, 780, '9자루', 72, GOLD)
    if key == 'pencils_many':
        return ''.join(hexagon(300 + (i % 6) * 96 + (48 if (i // 6) % 2 else 0), 260 + (i // 6) * 84, 50, [GOLD, '#4f82e3', RED][i % 3]) for i in range(30))


# ---------- aisle armrest ----------
def seat(x, y, arm='down', btn=False):
    s = f'<rect x="{x - 40}" y="{y - 420}" width="120" height="440" rx="44" fill="#4f82e3"/>'
    s += f'<rect x="{x - 40}" y="{y - 20}" width="360" height="110" rx="34" fill="#3d6fd0"/>'
    s += f'<rect x="{x + 80}" y="{y + 90}" width="40" height="160" fill="{MID}"/>'
    if arm == 'down':
        s += f'<rect x="{x + 40}" y="{y - 120}" width="300" height="46" rx="20" fill="{LIGHT}"/>'
    else:
        s += f'<rect x="{x + 40}" y="{y - 120}" width="300" height="46" rx="20" fill="{LIGHT}" transform="rotate(-80,{x + 60},{y - 97})"/>'
    if btn:
        s += f'<circle cx="{x + 82}" cy="{y - 64}" r="20" fill="{GOLD}"/><circle cx="{x + 82}" cy="{y - 64}" r="46" fill="none" stroke="{GOLD}" stroke-width="8"/>'
    return s


def wheelchair(x, y, s=1.0, c=GOLD):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cx="0" cy="0" r="110" fill="none" stroke="{c}" stroke-width="24"/>'
            f'<circle cx="150" cy="80" r="30" fill="none" stroke="{c}" stroke-width="16"/><path d="M-20,-220 v150 h170 l30,150" stroke="{c}" stroke-width="24" fill="none"/>'
            f'<circle cx="-20" cy="-280" r="40" fill="{c}"/></g>')


def scene_arm(key):
    if key == 'armrest':
        return seat(360, 600, btn=True)
    if key == 'armrest_button':
        return seat(360, 600, btn=True) + f'<circle cx="442" cy="536" r="120" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="24 16"/>'
    if key == 'armrest_up':
        return seat(360, 600, 'up') + arrow(560, 470, 560, 230, GOLD, 18)
    if key == 'wheelchair':
        return wheelchair(540, 560, 1.2)
    if key == 'wheelchair_transfer':
        return seat(160, 640, 'up') + wheelchair(780, 640, 0.8, LIGHT) + arrow(700, 360, 470, 360, GOLD, 20)
    if key == 'armrest_down':
        return seat(360, 600, 'down') + f'<g transform="translate(820,200) rotate(-20)"><path d="M-120,0 L120,0 L150,-20 L120,15 L-110,15 Z" fill="{GOLD}"/><path d="M-20,0 L40,-70 L70,-70 L40,0Z" fill="{GOLD}"/></g>'
    if key == 'aisle':
        rows = ''.join(f'<rect x="{x}" y="{120 + r * 140}" width="110" height="100" rx="20" fill="#4f82e3"/>' for r in range(5) for x in (150, 280, 690, 820))
        return rows + f'<rect x="420" y="100" width="240" height="720" rx="20" fill="#2b3245"/>' + arrow(540, 780, 540, 160, GOLD, 22)
    if key == 'crew_ask':
        return person(420, 760, 2.2, GOLD) + person(720, 780, 2.0, LIGHT) + bubble(820, 200, '?', GOLD)


# ---------- side mirror ----------
def mirror(x=540, y=440, s=1.0, inside='', text=True, hi=False):
    out = f'<g transform="translate({x},{y}) scale({s})">'
    out += f'<path d="M-330,-170 Q-340,-230 -260,-240 L280,-220 Q350,-210 340,-120 L320,170 Q310,230 240,230 L-280,220 Q-340,215 -340,150 Z" fill="#2b3245"/>'
    out += f'<path d="M-290,-170 L270,-160 Q300,-150 295,-110 L280,140 Q275,180 240,182 L-270,175 Q-300,170 -300,140 Z" fill="#9cc0ec"/>'
    out += inside
    if text:
        out += f'<rect x="-250" y="128" width="500" height="38" rx="8" fill="{GOLD if hi else "#dce6f4"}" fill-opacity="{1 if hi else .7}"/>'
    out += f'<rect x="300" y="-60" width="160" height="90" rx="20" fill="#2b3245"/>'
    return out + '</g>'


def scene_mirror(key):
    if key == 'mirror':
        return mirror()
    if key == 'mirror_text':
        return mirror(hi=True) + txt(540, 820, '"보이는 것보다 가까이 있음"', 54, GOLD)
    if key == 'mirror_convex':
        return (f'<line x1="200" y1="200" x2="200" y2="700" stroke="{MID}" stroke-width="20" stroke-linecap="round"/>' + txt(200, 790, '평면', 54, MID)
                + f'<path d="M760,200 Q900,450 760,700" stroke="{GOLD}" stroke-width="22" fill="none" stroke-linecap="round"/>' + txt(800, 790, '볼록', 54, GOLD))
    if key == 'mirror_wide':
        s = f'<path d="M520,620 Q600,450 520,280" stroke="{GOLD}" stroke-width="18" fill="none"/>'
        s += ''.join(f'<line x1="560" y1="450" x2="{200 + i * 0}" y2="{120 + i * 165}" stroke="{GOLD}" stroke-width="6" stroke-opacity=".7"/>' for i in range(5))
        return s + f'<polygon points="560,450 120,120 120,780" fill="{GOLD}" fill-opacity=".12"/>'
    if key == 'blindspot':
        s = (f'<rect x="200" y="60" width="680" height="800" fill="#3b445c"/><line x1="540" y1="80" x2="540" y2="840" stroke="{WHITE}" stroke-width="10" stroke-dasharray="50 40"/>')
        s += f'<polygon points="420,520 760,640 760,820" fill="{GOLD}" fill-opacity=".28"/>'
        s += f'<rect x="300" y="420" width="140" height="240" rx="30" fill="#4f82e3"/><rect x="630" y="660" width="140" height="240" rx="30" fill="{RED}"/>'
        return s
    if key == 'mirror_small':
        inner = f'<g transform="translate(-40,30) scale(.35)">{car(0, 0, RED, 1)}</g>'
        return mirror(540, 380, 1.0, inner) + f'<g opacity=".5">{car(540, 800, RED, 1.1)}</g>' + arrow(540, 600, 540, 700, MID, 10)
    if key == 'head_check':
        return person(540, 760, 2.6, GOLD) + f'<path d="M700,330 A170,170 0 0 1 760,520" stroke="{GOLD}" stroke-width="18" fill="none"/>' + arrow(760, 500, 740, 560, GOLD, 18)


# ---------- receipt ----------
def receipt(x=540, y=120, fade=0.0, coat=False):
    zig = ' '.join(f'{x + 200 - i * 40},{y + 700 + (20 if i % 2 else 0)}' for i in range(11))
    s = f'<polygon points="{x - 200},{y} {x + 200},{y} {zig}" fill="{WHITE}"/>'
    op = 1 - fade
    s += txt(x, y + 90, '영수증', 54, DARK)
    s += ''.join(f'<rect x="{x - 150}" y="{y + 150 + i * 70}" width="{300 - (i % 3) * 60}" height="22" rx="11" fill="#555" fill-opacity="{op:.2f}"/>' for i in range(7))
    if coat:
        s += f'<rect x="{x - 200}" y="{y}" width="400" height="30" fill="{GOLD}" fill-opacity=".8"/>'
    return s


def scene_receipt(key):
    if key == 'receipt':
        return receipt()
    if key == 'receipt_noink':
        return (receipt(380) + f'<path d="M760,330 q-70,110 -70,170 a70,70 0 0 0 140,0 q0,-60 -70,-170z" fill="#4f82e3"/>'
                + f'<circle cx="760" cy="460" r="130" fill="none" stroke="{RED}" stroke-width="16"/><line x1="668" y1="552" x2="852" y2="368" stroke="{RED}" stroke-width="16"/>')
    if key == 'receipt_coat':
        return receipt(400, coat=True) + ''.join(f'<path d="M{760 + i * 60},{560} q-25,-40 0,-80 q25,-40 0,-80" stroke="{RED}" stroke-width="12" fill="none" stroke-linecap="round"/>' for i in range(3))
    if key == 'printer_heat':
        return (f'<rect x="270" y="520" width="540" height="260" rx="40" fill="{MID}"/><rect x="330" y="520" width="420" height="24" fill="#2b3245"/>'
                + f'<rect x="380" y="160" width="320" height="370" fill="{WHITE}"/>'
                + ''.join(f'<circle cx="{420 + i * 40}" cy="490" r="10" fill="{RED}"/>' for i in range(7))
                + ''.join(f'<rect x="410" y="{220 + i * 60}" width="{240 - i * 30}" height="18" rx="9" fill="#444"/>' for i in range(4)))
    if key == 'receipt_sun':
        return receipt(380, fade=0.7) + f'<circle cx="820" cy="240" r="100" fill="{GOLD}"/>' + ''.join(f'<line x1="{820 + 140 * math.cos(math.radians(a))}" y1="{240 + 140 * math.sin(math.radians(a))}" x2="{820 + 190 * math.cos(math.radians(a))}" y2="{240 + 190 * math.sin(math.radians(a))}" stroke="{GOLD}" stroke-width="14" stroke-linecap="round"/>' for a in range(0, 360, 45))
    if key == 'receipt_wallet':
        return (receipt(380, fade=0.55) + f'<rect x="620" y="420" width="360" height="260" rx="30" fill="#8a5a3a"/><rect x="620" y="420" width="360" height="90" rx="30" fill="#6e4630"/><circle cx="920" cy="470" r="18" fill="{GOLD}"/>')
    if key == 'receipt_photo':
        return (f'<rect x="330" y="80" width="420" height="760" rx="60" fill="#2b3245"/><rect x="360" y="150" width="360" height="620" rx="20" fill="#16295a"/>'
                + f'<g transform="translate(540,190) scale(.75) translate(-540,0)">{receipt(540, 0)}</g>' + f'<circle cx="540" cy="800" r="22" fill="{MID}"/>')


# ---------- winglet ----------
def wing(x=540, y=560, winglet=True, vortex='none'):
    s = f'<polygon points="{x - 420},{y + 40} {x + 300},{y - 80} {x + 360},{y - 60} {x - 380},{y + 120}" fill="{LIGHT}"/>'
    if winglet:
        s += f'<polygon points="{x + 300},{y - 80} {x + 360},{y - 60} {x + 420},{y - 320} {x + 380},{y - 330}" fill="{GOLD}"/>'
    if vortex == 'big':
        s += ''.join(f'<ellipse cx="{x + 380 + i * 10}" cy="{y - 40 + i * 10}" rx="{60 + i * 40}" ry="{40 + i * 28}" fill="none" stroke="{SKY}" stroke-width="10" stroke-opacity="{1 - i * 0.2:.1f}"/>' for i in range(4))
    if vortex == 'small':
        s += ''.join(f'<ellipse cx="{x + 400}" cy="{y - 300 + i * 4}" rx="{30 + i * 18}" ry="{20 + i * 12}" fill="none" stroke="{SKY}" stroke-width="8" stroke-opacity="{1 - i * 0.3:.1f}"/>' for i in range(2))
    return s


def plane(x, y, s=1.0, c=LIGHT):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-260,0 Q-260,-40 -200,-40 L200,-40 Q280,-40 300,0 Q280,40 200,40 L-200,40 Q-260,40 -260,0Z" fill="{c}"/>'
            f'<polygon points="-40,0 80,0 -60,180 -120,180" fill="{c}"/><polygon points="-200,-30 -150,-30 -230,-140 -260,-140" fill="{c}"/></g>')


def scene_wing(key):
    if key in ('wing', 'winglet', 'winglet2'):
        s = wing()
        if key == 'winglet':
            s += f'<circle cx="920" cy="350" r="150" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="24 16"/>'
        if key == 'winglet2':
            s += shield(220, 260, 0.8)
        return s
    if key == 'wing_pressure':
        return (f'<path d="M140,470 Q300,300 700,380 Q900,420 960,470 Q700,520 140,470Z" fill="{LIGHT}"/>'
                + txt(540, 290, '압력 낮음', 56, SKY) + txt(540, 640, '압력 높음', 56, GOLD) + arrow(540, 700, 540, 560, GOLD, 16))
    if key == 'vortex':
        return wing(440, 600, False, 'big')
    if key == 'drag':
        return plane(560, 400, 1.3) + arrow(220, 720, 60, 720, RED, 22) + arrow(620, 720, 900, 720, LIGHT, 22)
    if key == 'vortex_small':
        return wing(440, 640, True, 'small')
    if key == 'nasa':
        return doc(200, 160, '실험', GOLD) + plane(780, 520, 0.7)
    if key == 'fuel_save':
        return (f'<path d="M540,180 q-170,260 -170,380 a170,170 0 0 0 340,0 q0,-120 -170,-380z" fill="{GOLD}"/>' + arrow(860, 300, 860, 650, GOLD, 24))


# ---------- rumble strip ----------
def road(lines=True, strips=True, hi=False):
    s = f'<rect x="160" y="40" width="760" height="840" fill="#3b445c"/>'
    s += f'<line x1="540" y1="60" x2="540" y2="860" stroke="{WHITE}" stroke-width="10" stroke-dasharray="60 40"/>' if lines else ''
    s += f'<line x1="200" y1="40" x2="200" y2="880" stroke="{WHITE}" stroke-width="10"/><line x1="880" y1="40" x2="880" y2="880" stroke="{WHITE}" stroke-width="10"/>'
    if strips:
        s += ''.join(f'<rect x="{x}" y="{60 + i * 46}" width="44" height="22" rx="6" fill="{GOLD if hi else "#2a3144"}"/>' for i in range(18) for x in (176, 858))
    return s


def scene_rumble(key):
    if key == 'rumble_road':
        return road(hi=True)
    if key == 'rumble':
        return road(hi=True) + f'<circle cx="880" cy="450" r="110" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="24 16"/>'
    if key == 'rumble_name':
        return (''.join(f'<rect x="{160 + i * 70}" y="560" width="44" height="60" rx="8" fill="#2a3144"/>' for i in range(11)) + f'<rect x="140" y="540" width="800" height="20" fill="#3b445c"/>'
                + ''.join(f'<path d="M{380 + i * 80},{420 - i * 10} q30,-40 0,-80" stroke="{GOLD}" stroke-width="12" fill="none" stroke-linecap="round"/>' for i in range(4)))
    if key == 'drowsy':
        return road() + f'<rect x="700" y="480" width="140" height="240" rx="30" fill="#4f82e3" transform="rotate(14,770,600)"/>' + txt(330, 300, 'Z z', 110, MID)
    if key == 'rumble_shake':
        return (f'<rect x="140" y="640" width="800" height="40" fill="#3b445c"/>' + ''.join(f'<rect x="{160 + i * 70}" y="660" width="44" height="30" rx="6" fill="#2a3144"/>' for i in range(11))
                + f'<circle cx="540" cy="500" r="150" fill="#2b3245"/><circle cx="540" cy="500" r="70" fill="{MID}"/>'
                + ''.join(f'<path d="M{330 - i * 40},{420 + i * 30} q-25,40 0,80" stroke="{GOLD}" stroke-width="12" fill="none"/><path d="M{750 + i * 40},{420 + i * 30} q25,40 0,80" stroke="{GOLD}" stroke-width="12" fill="none"/>' for i in range(3)))
    if key == 'wake':
        return person(540, 780, 2.6, GOLD) + bubble(820, 220, '!', GOLD)
    if key == 'cheap':
        return (f'<circle cx="540" cy="450" r="230" fill="{GOLD}"/><circle cx="540" cy="450" r="180" fill="none" stroke="#c9952c" stroke-width="14"/>' + txt(540, 500, '₩', 170, '#8a6020'))
    if key == 'lane_back':
        return road() + f'<rect x="680" y="520" width="140" height="240" rx="30" fill="#4f82e3"/>' + f'<path d="M760,500 Q760,300 620,220" stroke="{GOLD}" stroke-width="22" fill="none"/>' + arrow(660, 240, 600, 205, GOLD, 22)


def scene2(key):
    if key == 'question':
        return qmark()
    if key == 'law':
        return doc(340, 160)
    for fn in (scene_lav, scene_fuel, scene_pencil, scene_arm, scene_mirror, scene_receipt, scene_wing, scene_rumble):
        out = fn(key)
        if out:
            return out
    raise KeyError(key)
