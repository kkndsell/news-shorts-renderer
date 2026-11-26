# Scenes for 일상 수사대 047~054 (body & everyday science). viewBox 0 0 1080 900.
import math
from scenes import person, arrow, doc, GOLD, RED, SKY, LIGHT, MID, DARK, WHITE
from scenes2 import txt, qmark, bubble, shield
from scenes3 import head, finger, waves, SKIN, BROWN, GREEN


def ruler(x, y, h=640, mark=None):
    s = f'<rect x="{x}" y="{y}" width="90" height="{h}" rx="10" fill="#e3c27a"/>'
    s += ''.join(f'<line x1="{x}" y1="{y + i * 32}" x2="{x + (50 if i % 5 == 0 else 28)}" y2="{y + i * 32}" stroke="#7a5a2a" stroke-width="5"/>' for i in range(1, int(h / 32)))
    if mark is not None:
        s += f'<line x1="{x - 60}" y1="{mark}" x2="{x + 150}" y2="{mark}" stroke="{GOLD}" stroke-width="10"/>'
    return s


def spine(x=540, y=120, n=7, gap=18, disc=GOLD, squash=False):
    out = ''
    for i in range(n):
        yy = y + i * (78 + (gap if not squash else gap * 0.4))
        out += f'<rect x="{x - 90}" y="{yy}" width="180" height="70" rx="22" fill="{LIGHT}"/>'
        if i < n - 1:
            g = gap if not squash else gap * 0.4
            out += f'<rect x="{x - 80}" y="{yy + 70}" width="160" height="{g + 8}" rx="{(g + 8) / 2}" fill="{disc}"/>'
    return out


def bed(x=540, y=600):
    return (f'<rect x="{x - 400}" y="{y}" width="800" height="90" rx="20" fill="#4f82e3"/><rect x="{x - 420}" y="{y - 140}" width="40" height="320" rx="14" fill="{BROWN}"/>'
            f'<rect x="{x + 380}" y="{y - 60}" width="40" height="240" rx="14" fill="{BROWN}"/><ellipse cx="{x - 290}" cy="{y - 20}" rx="90" ry="40" fill="{WHITE}"/>')


def sleeper(x=540, y=560, jerk=False):
    s = bed(x, y + 40)
    s += f'<circle cx="{x - 290}" cy="{y - 50}" r="52" fill="{SKIN}"/>'
    s += f'<path d="M{x - 230},{y - 20} Q{x},{y - 90} {x + 330},{y - 20} L{x + 330},{y + 40} L{x - 230},{y + 40} Z" fill="{GOLD}"/>'
    if jerk:
        s += ''.join(f'<path d="M{x - 380 + i * 30},{y - 150 - i * 12} l20,-30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/>' for i in range(3))
        s += ''.join(f'<path d="M{x + 360 + i * 30},{y - 70 - i * 12} l20,-30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/>' for i in range(3))
    else:
        s += txt(x + 200, y - 160, 'z z', 80, MID)
    return s


def toast(x, y, ang=0, s=1.0, butter=True):
    b = f'<rect x="-110" y="-26" width="220" height="16" rx="8" fill="#f7e27a"/>' if butter else ''
    return (f'<g transform="translate({x},{y}) rotate({ang}) scale({s})"><path d="M-130,-10 Q-140,-60 -100,-70 Q0,-110 100,-70 Q140,-60 130,-10 L130,40 L-130,40Z" fill="#d9a35a"/>'
            f'<rect x="-120" y="-10" width="240" height="44" rx="10" fill="#f0cd8f"/>{b}</g>')


def table(x=540, y=380, w=520):
    return (f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="30" rx="8" fill="#8a6f5a"/><rect x="{x - w / 2 + 30}" y="{y + 30}" width="30" height="{860 - y - 30}" fill="#6e5848"/>'
            f'<rect x="{x + w / 2 - 60}" y="{y + 30}" width="30" height="{860 - y - 30}" fill="#6e5848"/><rect x="80" y="860" width="920" height="16" fill="{MID}"/>')


def belly(x=540, y=480, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-180,-300 Q-260,0 -180,300 L180,300 Q260,0 180,-300Z" fill="{GOLD}"/>'
            f'<ellipse cx="0" cy="40" rx="120" ry="150" fill="#f0cd8f"/><circle cx="0" cy="110" r="10" fill="#c9952c"/></g>')


def stomach(x=540, y=460, s=1.0, empty=True):
    out = (f'<g transform="translate({x},{y}) scale({s})"><path d="M-60,-240 Q-40,-150 -140,-80 Q-260,30 -150,170 Q-20,280 140,160 Q240,60 160,-40 Q90,-120 40,-140 Q10,-190 20,-240Z" fill="#e8909a"/>')
    if not empty:
        out += ''.join(f'<circle cx="{-80 + i * 40}" cy="{80 - (i % 2) * 40}" r="22" fill="#c9952c"/>' for i in range(5))
    return out + '</g>'


def face_photo(x, y, flip=False, frame=GOLD, s=1.0):
    t = f'translate({x},{y}) scale({-s if flip else s},{s})'
    return (f'<g transform="{t}"><rect x="-150" y="-190" width="300" height="380" rx="20" fill="#16295a" stroke="{frame}" stroke-width="10"/>'
            f'<ellipse cx="0" cy="-10" rx="100" ry="125" fill="{SKIN}"/><path d="M-110,-60 Q-90,-170 40,-150 Q120,-140 110,-40 Q60,-110 -110,-60Z" fill="#3a2a1a"/>'
            f'<circle cx="-38" cy="-10" r="10" fill="{DARK}"/><circle cx="38" cy="-10" r="10" fill="{DARK}"/><path d="M-30,60 q30,16 60,0" stroke="{DARK}" stroke-width="7" fill="none"/>'
            f'<circle cx="55" cy="35" r="9" fill="#8a5a3a"/><path d="M-10,10 q-6,24 10,28" stroke="#c99a7a" stroke-width="6" fill="none"/></g>')


def eye(x=540, y=460, s=1.0, closed=False):
    if closed:
        return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-220,0 Q0,120 220,0" stroke="{SKIN}" stroke-width="26" fill="none" stroke-linecap="round"/>'
                + ''.join(f'<line x1="{-150 + i * 75}" y1="{55 - abs(i - 2) * 8}" x2="{-165 + i * 82}" y2="{100 - abs(i - 2) * 6}" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>' for i in range(5)) + '</g>')
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-240,0 Q0,-190 240,0 Q0,190 -240,0Z" fill="{WHITE}"/><circle r="100" fill="#4f82e3"/><circle r="46" fill="{DARK}"/><circle cx="-26" cy="-30" r="18" fill="{WHITE}"/></g>')


def sparkles(cx, cy, n=14, r=280, seed=3):
    cols = [GOLD, SKY, '#f08a9a', '#9ccf6a', WHITE]
    out = ''
    for i in range(n):
        a = (i * 137.5 + seed * 20) % 360; d = r * (0.3 + ((i * 53) % 70) / 100)
        x = cx + d * math.cos(math.radians(a)); y = cy + d * math.sin(math.radians(a)); c = cols[i % 5]; k = 10 + (i * 7) % 18
        out += f'<path d="M{x:.0f},{y - k:.0f} L{x + k * .3:.0f},{y - k * .3:.0f} L{x + k:.0f},{y:.0f} L{x + k * .3:.0f},{y + k * .3:.0f} L{x:.0f},{y + k:.0f} L{x - k * .3:.0f},{y + k * .3:.0f} L{x - k:.0f},{y:.0f} L{x - k * .3:.0f},{y - k * .3:.0f}Z" fill="{c}"/>'
    return out


def hand(x=540, y=520, s=1.0, nails=GOLD):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-170" y="-40" width="340" height="300" rx="80" fill="{SKIN}"/>'
    for i, (dx, h) in enumerate([(-130, 230), (-45, 290), (45, 300), (130, 250)]):
        out += f'<rect x="{dx - 38}" y="{-40 - h}" width="76" height="{h + 40}" rx="38" fill="{SKIN}"/><rect x="{dx - 26}" y="{-40 - h + 8}" width="52" height="56" rx="20" fill="{nails}"/>'
    out += f'<rect x="150" y="10" width="76" height="200" rx="38" fill="{SKIN}" transform="rotate(35,188,110)"/>'
    return out + '</g>'


def foot(x=540, y=560, s=1.0, nails=GOLD):
    out = (f'<g transform="translate({x},{y}) scale({s})"><path d="M-160,200 Q-220,-40 -120,-160 Q0,-230 140,-170 Q220,-120 200,40 Q190,200 120,220Z" fill="{SKIN}"/>')
    for i, (dx, dy, r) in enumerate([(-120, -170, 58), (-30, -205, 44), (45, -205, 40), (110, -185, 36), (165, -150, 32)]):
        out += f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="{SKIN}"/><ellipse cx="{dx}" cy="{dy - r * .35}" rx="{r * .55}" ry="{r * .4}" fill="{nails}"/>'
    return out + '</g>'


def scene4(key):
    S = {}
    # 047 taller in the morning
    S['height'] = lambda: ruler(700, 120, 680, 250) + person(470, 800, 3.0, GOLD)
    S['morning_tall'] = lambda: ruler(700, 120, 680, 230) + person(470, 800, 3.05, GOLD) + f'<circle cx="230" cy="190" r="70" fill="{GOLD}"/>' + txt(890, 240, '아침', 54, GOLD)
    S['night_short'] = lambda: ruler(700, 120, 680, 260) + person(470, 800, 2.92, LIGHT) + f'<path d="M260,140 a70,70 0 1 0 60,110 a55,55 0 1 1 -60,-110z" fill="{LIGHT}"/>' + txt(890, 300, '밤', 54, LIGHT)
    S['spine'] = lambda: spine()
    S['disc_soft'] = lambda: spine(540, 120, 4, 46) + f'<circle cx="760" cy="340" r="90" fill="none" stroke="{GOLD}" stroke-width="10" stroke-dasharray="20 14"/>' + txt(760, 520, '물렁한 쿠션', 50, GOLD)
    S['disc_squash'] = lambda: spine(540, 200, 5, 30, GOLD, True) + arrow(540, 60, 540, 180, RED, 20)
    S['disc_refill'] = lambda: bed(540, 640) + spine(540, 130, 4, 40) + ''.join(f'<path d="M{760 + i * 40},{300 + i * 60} q-18,32 0,46 q18,-14 0,-46z" fill="{SKY}"/>' for i in range(3))
    S['measure_tip'] = lambda: ruler(700, 120, 680, 230) + person(470, 800, 3.0, GOLD) + f'<circle cx="230" cy="190" r="70" fill="{GOLD}"/>' + f'<path d="M820,600 l40,40 l80,-90" stroke="{GOLD}" stroke-width="24" fill="none" stroke-linecap="round"/>'
    # 048 knuckle crack
    S['knuckle'] = lambda: hand(540, 640, 1.0, '#f7dcc4')
    S['knuckle_pop'] = lambda: hand(540, 640, 1.0, '#f7dcc4') + bubble(820, 200, '뚝', GOLD)
    S['joint'] = lambda: (f'<rect x="200" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/><rect x="580" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/>'
                          f'<rect x="480" y="370" width="120" height="160" rx="40" fill="{SKY}" fill-opacity=".45"/>' + txt(540, 640, '관절 속 액체', 50, SKY))
    S['joint_pull'] = lambda: (f'<rect x="140" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/><rect x="640" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/>'
                               f'<rect x="420" y="370" width="240" height="160" rx="40" fill="{SKY}" fill-opacity=".45"/>' + arrow(300, 300, 120, 300, GOLD, 16) + arrow(780, 300, 960, 300, GOLD, 16))
    S['bubble_form'] = lambda: (f'<rect x="140" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/><rect x="640" y="380" width="300" height="140" rx="70" fill="{LIGHT}"/>'
                                f'<rect x="420" y="370" width="240" height="160" rx="40" fill="{SKY}" fill-opacity=".45"/><circle cx="540" cy="450" r="60" fill="{DARK}" stroke="{GOLD}" stroke-width="8"/>'
                                + ''.join(f'<path d="M{540 + 110 * math.cos(math.radians(a)):.0f},{450 + 110 * math.sin(math.radians(a)):.0f} l{30 * math.cos(math.radians(a)):.0f},{30 * math.sin(math.radians(a)):.0f}" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/>' for a in range(0, 360, 45)))
    S['mri'] = lambda: (f'<rect x="200" y="200" width="680" height="500" rx="250" fill="{LIGHT}"/><rect x="380" y="330" width="320" height="240" rx="120" fill="#16295a"/>' + txt(540, 820, '2015 MRI 영상', 56, GOLD))
    S['wait'] = lambda: (f'<circle cx="540" cy="450" r="230" fill="{LIGHT}"/><circle cx="540" cy="450" r="200" fill="#16295a"/><line x1="540" y1="450" x2="540" y2="300" stroke="{GOLD}" stroke-width="16" stroke-linecap="round"/>'
                         f'<line x1="540" y1="450" x2="640" y2="500" stroke="{GOLD}" stroke-width="12" stroke-linecap="round"/>' + txt(540, 780, '다시 뚝 하려면 시간이 걸려요', 46, LIGHT))
    S['healthy'] = lambda: hand(380, 640, 0.75, '#f7dcc4') + shield(800, 420, 0.9)
    # 049 hypnic jerk
    S['sleep'] = lambda: sleeper()
    S['jerk'] = lambda: sleeper(jerk=True) + txt(540, 200, '움찔!', 90, GOLD)
    S['seventy'] = lambda: ''.join(person(170 + (i % 5) * 185, 420 + (i // 5) * 330, 1.15, GOLD if i < 7 else MID) for i in range(10))
    S['muscles_relax'] = lambda: sleeper() + ''.join(f'<path d="M{300 + i * 140},{760} q30,-30 60,0" stroke="{SKY}" stroke-width="10" fill="none"/>' for i in range(4))
    S['brain_fall'] = lambda: (f'<ellipse cx="420" cy="380" rx="230" ry="180" fill="#f08a9a"/>' + ''.join(f'<path d="M{260 + i * 70},{300 + (i % 2) * 40} q30,-50 60,0" stroke="#c96a7a" stroke-width="10" fill="none"/>' for i in range(5))
                               + arrow(800, 160, 800, 640, GOLD, 22) + bubble(760, 760, '?!', GOLD))
    S['tree'] = lambda: (f'<rect x="460" y="300" width="80" height="560" fill="{BROWN}"/><circle cx="500" cy="250" r="230" fill="{GREEN}"/><rect x="540" y="430" width="300" height="30" rx="10" fill="{BROWN}"/>' + person(720, 420, 0.9, GOLD))
    S['coffee'] = lambda: (f'<rect x="360" y="380" width="280" height="320" rx="30" fill="{WHITE}"/><path d="M640,450 q100,0 100,90 q0,90 -100,90" stroke="{WHITE}" stroke-width="30" fill="none"/>'
                           f'<rect x="380" y="400" width="240" height="60" rx="16" fill="{BROWN}"/>' + waves(500, 260, 2, LIGHT, 1, 10, 0) + txt(540, 820, '카페인·피곤·스트레스', 50, LIGHT))
    S['normal'] = lambda: sleeper() + shield(860, 240, 0.7)
    # 050 toast
    S['toast'] = lambda: toast(540, 470, 0, 1.6)
    S['toast_floor'] = lambda: f'<rect x="80" y="760" width="920" height="16" fill="{MID}"/>' + toast(540, 690, 0, 1.4, False).replace('fill="#f0cd8f"', 'fill="#d9a35a"') + f'<ellipse cx="540" cy="756" rx="200" ry="16" fill="#f7e27a"/><ellipse cx="760" cy="758" rx="40" ry="8" fill="#f7e27a"/>' + bubble(820, 300, '!', RED)
    S['toast_toss'] = lambda: toast(380, 300, 40, 1.0) + toast(700, 700, 0, 1.0) + arrow(380, 420, 380, 600, LIGHT, 10) + txt(540, 160, '던지면 반반', 64, LIGHT)
    S['table_edge'] = lambda: table() + toast(720, 340, 20, 1.0)
    S['toast_rotate'] = lambda: table() + toast(800, 360, 30, 0.9) + toast(880, 560, 110, 0.9) + toast(900, 790, 180, 0.9) + f'<path d="M820,400 Q960,560 900,760" stroke="{GOLD}" stroke-width="8" fill="none" stroke-dasharray="20 14"/>'
    S['half_turn'] = lambda: f'<circle cx="540" cy="450" r="230" fill="none" stroke="{MID}" stroke-width="10"/><path d="M540,220 A230,230 0 0 1 540,680" stroke="{GOLD}" stroke-width="22" fill="none"/>' + arrow(560, 680, 520, 680, GOLD, 22) + txt(540, 470, '반 바퀴', 80, GOLD)
    S['ig_nobel'] = lambda: doc(200, 160, '상', GOLD) + txt(800, 450, '1996', 120, GOLD)
    S['push_far'] = lambda: table() + toast(700, 340, 0, 1.0) + arrow(580, 300, 900, 260, GOLD, 18)
    # 051 stomach growl
    S['belly'] = lambda: belly()
    S['growl'] = lambda: belly() + bubble(830, 240, '꾸르륵', GOLD).replace('font-size="90"', 'font-size="44"')
    S['stomach_empty'] = lambda: stomach()
    S['stomach_squeeze'] = lambda: stomach() + ''.join(arrow(540 + 330 * math.cos(math.radians(a)), 460 + 300 * math.sin(math.radians(a)), 540 + 220 * math.cos(math.radians(a)), 460 + 200 * math.sin(math.radians(a)), GOLD, 14) for a in (0, 120, 240))
    S['air_echo'] = lambda: stomach() + ''.join(f'<circle cx="{480 + i * 60}" cy="{430 + (i % 2) * 60}" r="{18 + i * 4}" fill="none" stroke="{WHITE}" stroke-width="6"/>' for i in range(3)) + waves(800, 460, 3, GOLD)
    S['clean_sweep'] = lambda: stomach() + (f'<g transform="translate(560,500) rotate(-30)"><rect x="-10" y="-200" width="20" height="200" fill="{BROWN}"/><path d="M-70,0 L70,0 L50,90 L-50,90Z" fill="{GOLD}"/></g>')
    S['clock_90'] = lambda: (f'<circle cx="540" cy="450" r="230" fill="{LIGHT}"/><circle cx="540" cy="450" r="200" fill="#16295a"/><path d="M540,450 L540,250 A200,200 0 1 1 340,450 Z" fill="{GOLD}" fill-opacity=".6"/>' + txt(540, 780, '약 90~120분마다', 56, GOLD))
    S['full_quiet'] = lambda: stomach(540, 460, 1.0, False) + txt(840, 220, '쉿', 80, MID)
    # 052 photo face
    S['selfie'] = lambda: (f'<rect x="330" y="80" width="420" height="760" rx="60" fill="#2b3245"/><rect x="360" y="150" width="360" height="620" rx="20" fill="#16295a"/>' + face_photo(540, 460, False, '#16295a', 1.0))
    S['mirror_face'] = lambda: (f'<ellipse cx="540" cy="450" rx="300" ry="390" fill="#9cc0ec"/><ellipse cx="540" cy="450" rx="270" ry="360" fill="#c8dcf4"/>' + face_photo(540, 450, True, '#c8dcf4', 1.1))
    S['flip'] = lambda: face_photo(300, 450, True, SKY) + face_photo(780, 450, False, GOLD) + arrow(470, 450, 610, 450, LIGHT, 14) + txt(300, 760, '거울', 56, SKY) + txt(780, 760, '사진', 56, GOLD)
    S['familiar'] = lambda: (f'<ellipse cx="540" cy="450" rx="300" ry="390" fill="#9cc0ec"/><ellipse cx="540" cy="450" rx="270" ry="360" fill="#c8dcf4"/>' + face_photo(540, 450, True, '#c8dcf4', 1.1)
                             + ''.join(f'<path d="M{120 + i * 60},{150 + i * 30} l20,-20" stroke="{GOLD}" stroke-width="8"/>' for i in range(3)) + txt(540, 870, '매일 보는 얼굴', 50, GOLD))
    S['study_1977'] = lambda: doc(200, 160, '실험', GOLD) + txt(800, 450, '1977', 120, GOLD)
    S['choose_mirror'] = lambda: face_photo(300, 430, True, GOLD) + face_photo(780, 430, False, MID) + f'<path d="M240,700 l40,40 l80,-90" stroke="{GOLD}" stroke-width="22" fill="none" stroke-linecap="round"/>' + txt(300, 820, '나', 56, GOLD)
    S['friend_choose'] = lambda: face_photo(300, 430, True, MID) + face_photo(780, 430, False, GOLD) + f'<path d="M720,700 l40,40 l80,-90" stroke="{GOLD}" stroke-width="22" fill="none" stroke-linecap="round"/>' + txt(780, 820, '친구', 56, GOLD)
    S['flip_setting'] = lambda: (f'<rect x="330" y="80" width="420" height="760" rx="60" fill="#2b3245"/><rect x="360" y="150" width="360" height="620" rx="20" fill="#16295a"/>'
                                 f'<rect x="400" y="420" width="280" height="90" rx="45" fill="{GOLD}"/><circle cx="630" cy="465" r="34" fill="{WHITE}"/>' + txt(540, 360, '좌우 반전', 44, WHITE))
    # 053 eye rub
    S['eye_closed'] = lambda: eye(540, 460, 1.4, True)
    S['rub'] = lambda: eye(540, 520, 1.3, True) + finger(560, 300, 0.7) + ''.join(f'<path d="M{430 + i * 40},{180 - i * 20} q20,20 40,0" stroke="{GOLD}" stroke-width="8" fill="none"/>' for i in range(3))
    S['stars'] = lambda: f'<rect x="140" y="140" width="800" height="620" rx="40" fill="#050a18"/>' + sparkles(540, 450, 22, 300)
    S['retina'] = lambda: eye(540, 460, 1.5) + f'<path d="M360,290 A260,260 0 0 1 360,630" stroke="{GOLD}" stroke-width="16" fill="none"/>' + txt(260, 470, '망막', 54, GOLD)
    S['light_signal'] = lambda: f'<circle cx="200" cy="260" r="70" fill="{GOLD}"/>' + arrow(280, 300, 470, 420, GOLD, 14) + eye(640, 470, 0.9) + arrow(820, 470, 980, 470, GOLD, 14)
    S['pressure'] = lambda: eye(540, 460, 1.3) + ''.join(arrow(540 + 400 * math.cos(math.radians(a)), 460 + 300 * math.sin(math.radians(a)), 540 + 290 * math.cos(math.radians(a)), 460 + 200 * math.sin(math.radians(a)), GOLD, 14) for a in (0, 90, 180, 270))
    S['brain_light'] = lambda: (f'<ellipse cx="540" cy="420" rx="300" ry="230" fill="#f08a9a"/>' + ''.join(f'<path d="M{330 + i * 80},{360 + (i % 2) * 50} q30,-50 60,0" stroke="#c96a7a" stroke-width="10" fill="none"/>' for i in range(6)) + sparkles(540, 420, 10, 220, 7) + bubble(860, 140, '빛?', GOLD).replace('font-size="90"', 'font-size="60"'))
    S['no_rub'] = lambda: eye(540, 460, 1.3, True) + f'<circle cx="540" cy="460" r="320" fill="none" stroke="{RED}" stroke-width="16"/><line x1="315" y1="685" x2="765" y2="235" stroke="{RED}" stroke-width="16"/>'
    # 054 nails
    S['nails'] = lambda: hand(360, 640, 0.75) + foot(800, 600, 0.85)
    S['nail_compare'] = lambda: hand(320, 640, 0.7) + foot(800, 600, 0.8) + txt(320, 860, '손톱', 54, GOLD) + txt(800, 860, '발톱', 54, LIGHT)
    S['nail_numbers'] = lambda: (f'<rect x="180" y="{700 - 347}" width="240" height="347" rx="20" fill="{GOLD}"/><rect x="660" y="{700 - 162}" width="240" height="162" rx="20" fill="{LIGHT}"/>'
                                 f'<rect x="120" y="700" width="840" height="10" fill="{MID}"/>' + txt(300, 330, '3.47mm', 60, GOLD) + txt(780, 510, '1.62mm', 60, LIGHT) + txt(300, 790, '손톱', 50, GOLD) + txt(780, 790, '발톱', 50, LIGHT))
    S['typing'] = lambda: (f'<rect x="140" y="520" width="800" height="240" rx="24" fill="#2b3245"/>' + ''.join(f'<rect x="{170 + (i % 10) * 76}" y="{550 + (i // 10) * 64}" width="62" height="52" rx="10" fill="{MID}"/>' for i in range(30)) + hand(540, 560, 0.55))
    S['blood_flow'] = lambda: person(540, 820, 3.0, LIGHT) + f'<path d="M540,350 Q420,420 330,560" stroke="{RED}" stroke-width="14" fill="none"/><path d="M540,350 Q560,600 520,820" stroke="{RED}" stroke-width="8" fill="none" stroke-dasharray="20 16"/>' + f'<circle cx="540" cy="350" r="34" fill="{RED}"/>'
    S['shoe'] = lambda: (f'<path d="M180,620 Q180,420 380,400 L560,380 Q700,380 860,520 Q920,580 900,660 L180,660Z" fill="{BROWN}"/><rect x="170" y="650" width="760" height="50" rx="20" fill="#3a2a1a"/>' + txt(540, 260, '신발 속에서 쉬는 발톱', 52, LIGHT))
    S['dominant'] = lambda: hand(320, 640, 0.65, MID) + hand(780, 640, 0.65, GOLD) + txt(780, 860, '자주 쓰는 손', 48, GOLD)
    if key in S:
        return S[key]()
    return None
