# Scenes for 일상 수사대 039~046 (everyday science). viewBox 0 0 1080 900.
import math
from scenes import person, arrow, doc, GOLD, RED, SKY, LIGHT, MID, DARK, WHITE
from scenes2 import txt, qmark, bubble, shield

GREEN, BROWN, SKIN = '#5fb07a', '#8a5a3a', '#f1c9a5'


def waves(x, y, n=3, c=GOLD, d=1, w=10, r0=40):
    return ''.join(f'<path d="M{x + d * (r0 + i * 40)},{y - 40 - i * 25} q{d * 30},{40 + i * 25} 0,{80 + i * 50}" stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round"/>' for i in range(n))


def head(x=540, y=470, s=1.0, c=SKIN):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-170,60 Q-200,-220 20,-240 Q200,-240 210,-60 Q215,20 180,60 L190,140 Q160,160 140,150 L120,240 L-60,240 L-60,170 Q-150,150 -170,60Z" fill="{c}"/>'
            f'<ellipse cx="-70" cy="-10" rx="38" ry="55" fill="#e3ad88"/><circle cx="120" cy="-50" r="14" fill="{DARK}"/><path d="M180,90 q-25,10 -50,0" stroke="{DARK}" stroke-width="10" fill="none"/></g>')


def phone(x=540, y=460, s=1.0, screen=''):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-150" y="-280" width="300" height="560" rx="44" fill="#2b3245"/>'
            f'<rect x="-128" y="-240" width="256" height="470" rx="18" fill="#16295a"/>{screen}<circle cy="250" r="14" fill="{MID}"/></g>')


def mic_screen():
    return (f'<circle cx="0" cy="-20" r="80" fill="{RED}"/><rect x="-30" y="-80" width="60" height="100" rx="30" fill="{WHITE}"/>'
            f'<path d="M-50,0 a50,50 0 0 0 100,0" stroke="{WHITE}" stroke-width="10" fill="none"/>'
            + ''.join(f'<rect x="{-100 + i * 25}" y="{140 - (h := [20, 50, 80, 40, 70, 30, 60, 25, 45][i]) / 2}" width="12" height="{h}" rx="6" fill="{GOLD}"/>' for i in range(9)))


def finger(x, y, s=1.0, wrinkly=False):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="-260" width="140" height="420" rx="70" fill="{SKIN}"/><ellipse cx="0" cy="-200" rx="50" ry="40" fill="#f7dcc4"/>'
    if wrinkly:
        out += ''.join(f'<path d="M-55,{-230 + i * 34} q30,-14 55,0 q30,14 55,0" stroke="#c99a7a" stroke-width="7" fill="none"/>' for i in range(7))
    return out + '</g>'


def marble(x, y, r=40, c=SKY):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/><circle cx="{x - r * .35}" cy="{y - r * .35}" r="{r * .25}" fill="{WHITE}" fill-opacity=".7"/>'


def bowl(x, y, w=520, water=True):
    s = f'<path d="M{x - w / 2},{y} Q{x - w / 2},{y + 220} {x},{y + 220} Q{x + w / 2},{y + 220} {x + w / 2},{y} Z" fill="#c8ced9"/>'
    if water:
        s += f'<path d="M{x - w / 2 + 20},{y + 30} Q{x - w / 2 + 30},{y + 200} {x},{y + 200} Q{x + w / 2 - 30},{y + 200} {x + w / 2 - 20},{y + 30} Z" fill="#6fa8e6" fill-opacity=".8"/>'
    return s


def icecream(x=540, y=520, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><polygon points="-120,-20 120,-20 0,320" fill="#e3a250"/>'
            + ''.join(f'<line x1="{-100 + i * 50}" y1="-10" x2="{-40 + i * 50}" y2="120" stroke="#c98a3a" stroke-width="6"/>' for i in range(5))
            + f'<circle cx="-60" cy="-80" r="100" fill="#f7c6d0"/><circle cx="60" cy="-80" r="100" fill="#fff2d6"/><circle cx="0" cy="-170" r="100" fill="#a8e0c8"/></g>')


def chili(x=540, y=450, s=1.0, rot=-25):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><path d="M-260,0 Q-200,-90 60,-70 Q220,-55 280,40 Q160,10 40,40 Q-160,90 -260,0Z" fill="{RED}"/>'
            f'<path d="M-260,0 q-40,-20 -60,-80 q30,20 70,40" fill="{GREEN}"/><path d="M-120,-40 q80,-20 160,-10" stroke="#ff8a8f" stroke-width="12" fill="none" stroke-linecap="round"/></g>')


def glass(x, y, fill='#6fa8e6', s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-110,-180 L110,-180 L85,180 L-85,180Z" fill="{WHITE}" fill-opacity=".25" stroke="{LIGHT}" stroke-width="8"/>'
            f'<path d="M-100,-100 L100,-100 L85,170 L-85,170Z" fill="{fill}"/></g>')


def cloud(x, y, s=1.0, c=LIGHT):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{c}"><circle cx="-90" cy="0" r="80"/><circle cx="0" cy="-50" r="110"/><circle cx="100" cy="0" r="85"/>'
            f'<rect x="-170" y="0" width="355" height="80" rx="40"/></g>')


def drops(x, y, n=6, c=SKY):
    return ''.join(f'<path d="M{x + (i % 3) * 110 - 110 + (i // 3) * 55},{y + (i // 3) * 110} q-18,32 0,46 q18,-14 0,-46z" fill="{c}"/>' for i in range(n))


def soil(y=700):
    return (f'<rect x="80" y="{y}" width="920" height="200" rx="20" fill="{BROWN}"/>'
            + ''.join(f'<circle cx="{130 + (i * 97) % 860}" cy="{y + 40 + (i * 53) % 140}" r="{6 + i % 3 * 3}" fill="#6e4630"/>' for i in range(22)))


def banana(x=540, y=460, s=1.0, c='#f2d24a', spots=0):
    out = (f'<g transform="translate({x},{y}) scale({s})"><path d="M-300,-60 Q-20,260 300,-140 Q320,-110 300,-80 Q-10,330 -320,-30Z" fill="{c}"/>'
           f'<rect x="-345" y="-80" width="40" height="40" rx="8" fill="#6e5530" transform="rotate(-30,-325,-60)"/>')
    out += ''.join(f'<ellipse cx="{-200 + i * 70}" cy="{60 + (i % 2) * 30 - (i * i * 3)}" rx="18" ry="12" fill="#3a2a1a"/>' for i in range(spots))
    return out + '</g>'


def can(x=540, y=470, s=1.0, c=RED, open_=False):
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-140" y="-250" width="280" height="500" rx="30" fill="{c}"/>'
           f'<ellipse cx="0" cy="-250" rx="140" ry="34" fill="#c8ced9"/><ellipse cx="0" cy="-250" rx="110" ry="24" fill="#aab4c4"/>'
           f'<path d="M-140,-40 Q0,40 140,-40" stroke="{WHITE}" stroke-width="22" fill="none"/>')
    out += (f'<ellipse cx="30" cy="-252" rx="34" ry="12" fill="#2b3245"/>' if open_ else f'<rect x="0" y="-262" width="70" height="22" rx="10" fill="{MID}"/>')
    return out + '</g>'


def bubbles(x, y, w, h, n=30, rmax=12, c=WHITE, op=.8):
    return ''.join(f'<circle cx="{x + (i * 137) % w}" cy="{y + (i * 89) % h}" r="{3 + (i * 7) % rmax}" fill="none" stroke="{c}" stroke-opacity="{op}" stroke-width="4"/>' for i in range(n))


def shower(x=540, y=440):
    s = (f'<rect x="{x - 360}" y="{y - 360}" width="720" height="780" rx="20" fill="#d9e4f2"/>'
         + ''.join(f'<line x1="{x - 360 + i * 120}" y1="{y - 360}" x2="{x - 360 + i * 120}" y2="{y + 420}" stroke="#b8c6da" stroke-width="5"/>' for i in range(1, 6))
         + ''.join(f'<line x1="{x - 360}" y1="{y - 360 + i * 120}" x2="{x + 360}" y2="{y - 360 + i * 120}" stroke="#b8c6da" stroke-width="5"/>' for i in range(1, 7))
         + f'<path d="M{x + 220},{y - 320} v60 h-80" stroke="{MID}" stroke-width="18" fill="none"/><ellipse cx="{x + 120}" cy="{y - 250}" rx="60" ry="20" fill="{MID}"/>'
         + ''.join(f'<line x1="{x + 80 + i * 20}" y1="{y - 220}" x2="{x + 60 + i * 24}" y2="{y - 80}" stroke="{SKY}" stroke-width="6" stroke-dasharray="20 18"/>' for i in range(5)))
    return s


def note(x, y, s=1.0, c=GOLD):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="60" rx="34" ry="26" fill="{c}" transform="rotate(-20,0,60)"/>'
            f'<line x1="30" y1="55" x2="30" y2="-60" stroke="{c}" stroke-width="10"/><path d="M30,-60 q50,20 50,60" stroke="{c}" stroke-width="10" fill="none"/></g>')


def vessel(x, y, w=60, c=RED, l=600):
    return f'<rect x="{x - l / 2}" y="{y - w / 2}" width="{l}" height="{w}" rx="{w / 2}" fill="{c}"/>'


def scene3(key):
    S = {}
    # 039 recorded voice
    S['phone_mic'] = lambda: phone(screen=mic_screen())
    S['two_paths'] = lambda: head() + waves(760, 330, 3, SKY) + f'<path d="M420,300 q-60,120 0,240" stroke="{GOLD}" stroke-width="12" fill="none" stroke-dasharray="20 14"/>'
    S['air_path'] = lambda: head() + waves(760, 330, 3, SKY) + f'<path d="M760,330 C900,120 300,80 470,450" stroke="{SKY}" stroke-width="10" fill="none" stroke-dasharray="22 16"/>' + arrow(480, 380, 470, 450, SKY, 10)
    S['bone_path'] = lambda: head() + ''.join(f'<path d="M{620 - i * 40},{330 - i * 30} q-80,{100 + i * 15} -150,{120}" stroke="{GOLD}" stroke-width="12" fill="none" stroke-linecap="round"/>' for i in range(3))
    S['bass_waves'] = lambda: f'<path d="M120,450 ' + ' '.join(f'q60,{-180 if i % 2 == 0 else 180} 120,0' for i in range(7)) + f'" stroke="{GOLD}" stroke-width="18" fill="none"/>' + txt(540, 780, '낮은 소리 ↑', 64, GOLD)
    S['recorder'] = lambda: phone(560, 470, 0.9, mic_screen()) + waves(250, 470, 3, SKY, -1)
    S['voice_thin'] = lambda: f'<path d="M120,450 ' + ' '.join(f'q15,{-90 if i % 2 == 0 else 90} 30,0' for i in range(28)) + f'" stroke="{SKY}" stroke-width="10" fill="none"/>' + txt(540, 780, '더 높고 얇게', 64, SKY)
    S['friends_hear'] = lambda: person(300, 760, 2.2, GOLD) + person(780, 760, 2.2, LIGHT) + waves(420, 420, 3, SKY) + phone(780, 260, 0.35, '')
    S['earplug'] = lambda: head() + f'<ellipse cx="470" cy="460" rx="40" ry="30" fill="{GOLD}"/>' + ''.join(f'<circle cx="540" cy="420" r="{200 + i * 50}" fill="none" stroke="{GOLD}" stroke-width="6" stroke-opacity="{.6 - i * .15:.2f}"/>' for i in range(3))
    # 040 wrinkly fingers
    S['finger'] = lambda: finger(430, 520, 1.1, True) + finger(650, 540, 1.0, True)
    S['finger_swell'] = lambda: finger(540, 560, 1.1, True) + drops(820, 220, 3) + bubble(260, 220, '?', MID)
    S['nerve'] = lambda: finger(380, 560, 1.1, True) + f'<path d="M620,820 Q700,600 650,450 T720,150" stroke="{GOLD}" stroke-width="16" fill="none"/>' + ''.join(f'<circle cx="{650 + i * 30}" cy="{450 - i * 110}" r="16" fill="{GOLD}"/>' for i in range(3))
    S['vessel'] = lambda: vessel(540, 300, 90) + arrow(540, 420, 540, 520, GOLD, 18) + vessel(540, 620, 40) + txt(540, 820, '혈관이 좁아져요', 56, LIGHT)
    S['lab'] = lambda: doc(200, 160, '실험', GOLD) + txt(800, 450, '2013', 120, GOLD)
    S['marbles'] = lambda: bowl(540, 380) + ''.join(marble(400 + i * 90, 500 + (i % 2) * 40, 34, [SKY, GOLD, RED, GREEN][i % 4]) for i in range(4)) + finger(820, 260, 0.6, True)
    S['tire_tread'] = lambda: (f'<rect x="300" y="160" width="480" height="600" rx="80" fill="#2b3245"/>' + ''.join(f'<path d="M340,{220 + i * 70} l60,30 l60,-30 l60,30 l60,-30 l60,30 l60,-30 l60,30" stroke="{MID}" stroke-width="16" fill="none"/>' for i in range(8)))
    S['dry_marble'] = lambda: ''.join(marble(380 + i * 110, 600, 40, [SKY, GOLD, RED][i % 3]) for i in range(4)) + finger(300, 420, 0.7, True) + finger(800, 420, 0.7, False) + txt(540, 200, '= 차이 없음', 64, LIGHT)
    # 041 brain freeze
    S['icecream'] = lambda: icecream()
    S['palate_cold'] = lambda: head() + icecream(860, 560, 0.5) + f'<path d="M540,520 q120,-50 230,0" stroke="{SKY}" stroke-width="18" fill="none"/>' + ''.join(f'<text x="{600 + i * 60}" y="500" font-size="40" fill="{SKY}">*</text>' for i in range(3))
    S['palate_nerves'] = lambda: head() + ''.join(f'<path d="M{560 + i * 30},520 q-40,-60 -20,-140" stroke="{[GOLD, RED][i % 2]}" stroke-width="8" fill="none"/>' for i in range(5))
    S['vessel_narrow'] = lambda: vessel(540, 300, 110) + arrow(540, 400, 540, 520, SKY, 18) + vessel(540, 620, 36) + txt(540, 820, '확 좁아졌다가', 56, SKY)
    S['vessel_wide'] = lambda: vessel(540, 300, 36) + arrow(540, 400, 540, 520, GOLD, 18) + vessel(540, 620, 130) + txt(540, 820, '다시 확 넓어져요', 56, GOLD)
    S['head_pain'] = lambda: head() + ''.join(f'<line x1="{420 + i * 60}" y1="{180 - (i % 2) * 30}" x2="{400 + i * 70}" y2="{100 - (i % 2) * 30}" stroke="{GOLD}" stroke-width="14" stroke-linecap="round"/>' for i in range(5))
    S['tongue_warm'] = lambda: head() + f'<path d="M560,560 q100,-80 200,-40" stroke="#e86a7a" stroke-width="40" fill="none" stroke-linecap="round"/>' + glass(880, 620, '#e3a250', 0.6) + waves(860, 380, 2, GOLD, 1, 8, 10)
    # 042 spicy + water
    S['chili'] = lambda: chili()
    S['receptor_hot'] = lambda: (f'<rect x="140" y="560" width="800" height="120" rx="40" fill="#e86a7a"/>' + ''.join(f'<path d="M{220 + i * 160},560 v-60 l-30,-30 m30,30 l30,-30" stroke="{GOLD}" stroke-width="10" fill="none"/>' for i in range(5))
                                 + ''.join(f'<circle cx="{205 + i * 160}" cy="460" r="22" fill="{RED}"/>' for i in range(5)) + txt(540, 300, '뜨거워!', 90, RED))
    S['water_no'] = lambda: glass(540, 500) + ''.join(f'<circle cx="{460 + i * 60}" cy="{420 + (i % 2) * 50}" r="20" fill="{RED}"/>' for i in range(3)) + f'<circle cx="540" cy="500" r="260" fill="none" stroke="{MID}" stroke-width="10" stroke-dasharray="26 18"/>'
    S['spread'] = lambda: (f'<rect x="140" y="420" width="800" height="200" rx="80" fill="#e86a7a"/>' + ''.join(f'<circle cx="{180 + (i * 113) % 720}" cy="{450 + (i * 61) % 140}" r="18" fill="{RED}"/>' for i in range(16))
                           + drops(540, 220, 6) + ''.join(arrow(540, 520, 540 + dx, 520, SKY, 10) for dx in (-300, 300)))
    S['oil_yes'] = lambda: glass(540, 500, '#f0c35a') + ''.join(f'<circle cx="{480 + i * 60}" cy="{460 + (i % 2) * 40}" r="18" fill="{RED}" fill-opacity=".45"/>' for i in range(3))
    S['milk'] = lambda: glass(540, 500, WHITE) + chili(820, 260, 0.45, 20)
    S['casein'] = lambda: (f'<rect x="140" y="560" width="800" height="120" rx="40" fill="#e86a7a"/>' + ''.join(f'<path d="M{220 + i * 160},560 v-60" stroke="{GOLD}" stroke-width="10"/>' for i in range(5))
                           + ''.join(f'<circle cx="{220 + i * 160}" cy="{300 - (i % 2) * 40}" r="22" fill="{RED}"/><circle cx="{250 + i * 160}" cy="{300 - (i % 2) * 40}" r="30" fill="{WHITE}"/>' for i in range(5)) + ''.join(arrow(220 + i * 160, 480, 220 + i * 160, 360, WHITE, 8) for i in range(5)))
    S['milk_tip'] = lambda: glass(380, 520, WHITE, 1.0) + chili(760, 420, 0.6, -30) + f'<path d="M640,700 l40,40 l80,-90" stroke="{GOLD}" stroke-width="24" fill="none" stroke-linecap="round"/>'
    # 043 rain smell
    S['rain_soil'] = lambda: cloud(540, 180, 1.2) + drops(540, 360, 6) + soil(640)
    S['name_card'] = lambda: f'<rect x="200" y="300" width="680" height="300" rx="30" fill="{WHITE}"/>' + txt(540, 470, 'petrichor', 100, DARK, 800) + txt(540, 560, '페트리코', 50, MID)
    S['lab_1964'] = lambda: doc(200, 160, '이름', GOLD) + txt(800, 450, '1964', 120, GOLD)
    S['molecule'] = lambda: (''.join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LIGHT}" stroke-width="14"/>' for x1, y1, x2, y2 in [(400, 350, 540, 280), (540, 280, 680, 350), (680, 350, 680, 510), (680, 510, 540, 580), (540, 580, 400, 510), (400, 510, 400, 350), (680, 350, 820, 280), (680, 510, 820, 580)])
                             + ''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="{GOLD if i == 6 else LIGHT}"/>' for i, (x, y) in enumerate([(400, 350), (540, 280), (680, 350), (680, 510), (540, 580), (400, 510), (820, 280), (820, 580)])))
    S['bacteria'] = lambda: soil(560) + ''.join(f'<rect x="{220 + i * 150}" y="{620 + (i % 2) * 70}" width="90" height="34" rx="17" fill="{GREEN}"/>' for i in range(5)) + waves(540, 380, 3, '#9ccf6a', -1)
    S['raindrop'] = lambda: soil(620) + f'<path d="M540,220 q-60,110 0,160 q60,-50 0,-160z" fill="{SKY}"/>' + ''.join(f'<circle cx="{500 + i * 40}" cy="{590 - (i % 2) * 30}" r="{10 + i * 3}" fill="none" stroke="{WHITE}" stroke-width="5"/>' for i in range(3))
    S['aerosol'] = lambda: soil(660) + ''.join(f'<circle cx="{200 + (i * 131) % 700}" cy="{200 + (i * 71) % 400}" r="{6 + i % 4 * 3}" fill="#9ccf6a" fill-opacity=".8"/>' for i in range(30))
    S['nose_sensitive'] = lambda: (f'<path d="M420,160 Q330,420 290,520 Q280,580 360,590 L460,590" stroke="{LIGHT}" stroke-width="34" fill="none" stroke-linecap="round"/>'
                                   + f'<circle cx="760" cy="420" r="8" fill="#9ccf6a"/>' + ''.join(f'<circle cx="760" cy="420" r="{60 + i * 60}" fill="none" stroke="{GOLD}" stroke-width="6" stroke-opacity="{.8 - i * .2:.1f}"/>' for i in range(4)))
    S['rain_smell'] = lambda: cloud(540, 160, 1.1) + drops(540, 330, 6) + soil(660) + waves(540, 560, 3, '#9ccf6a', 1)
    # 044 banana
    S['banana'] = lambda: banana()
    S['tropical'] = lambda: f'<circle cx="820" cy="200" r="100" fill="{GOLD}"/>' + f'<rect x="280" y="300" width="40" height="520" fill="{BROWN}"/>' + ''.join(f'<path d="M300,320 q{dx},{dy} {dx * 2},{dy + 80}" stroke="{GREEN}" stroke-width="40" fill="none" stroke-linecap="round"/>' for dx, dy in [(-120, -80), (120, -80), (-160, 20), (160, 20)]) + banana(640, 640, 0.5)
    S['cell_break'] = lambda: ''.join(f'<rect x="{220 + (i % 4) * 160}" y="{260 + (i // 4) * 160}" width="140" height="140" rx="14" fill="#f2d24a" stroke="#c9a530" stroke-width="8" stroke-dasharray="{"30 20" if i in (2, 5, 9) else "0"}"/>' for i in range(12)) + txt(540, 200, '❄', 90, SKY)
    S['mix'] = lambda: f'<rect x="340" y="260" width="400" height="400" rx="30" fill="#f2d24a" stroke="#c9a530" stroke-width="10" stroke-dasharray="40 24"/>' + ''.join(f'<circle cx="{420 + (i * 83) % 260}" cy="{330 + (i * 57) % 260}" r="16" fill="{[GREEN, BROWN][i % 2]}"/>' for i in range(14))
    S['brown'] = lambda: banana(540, 460, 1.0, '#c98f3a', 6) + waves(860, 300, 2, LIGHT, 1, 8, 10)
    S['apple'] = lambda: (f'<circle cx="400" cy="480" r="200" fill="{RED}"/><path d="M400,280 q20,-60 60,-80" stroke="{BROWN}" stroke-width="16" fill="none"/>'
                          + f'<path d="M640,320 q160,0 160,160 q0,160 -160,160 z" fill="#f6e7c1"/><path d="M640,320 q160,0 160,160 q0,160 -160,160 z" fill="#b5803d" fill-opacity=".55"/>')
    S['room_temp'] = lambda: banana(400, 520, 0.7) + (f'<rect x="740" y="220" width="220" height="460" rx="24" fill="{LIGHT}"/><line x1="740" y1="380" x2="960" y2="380" stroke="{MID}" stroke-width="8"/>'
                                                         f'<circle cx="850" cy="460" r="110" fill="none" stroke="{RED}" stroke-width="16"/><line x1="772" y1="538" x2="928" y2="382" stroke="{RED}" stroke-width="16"/>')
    # 045 shaken soda
    S['soda_can'] = lambda: can()
    S['co2_in'] = lambda: can(540, 480) + bubbles(420, 300, 240, 400, 18, 10, WHITE, .5)
    S['tiny_bubbles'] = lambda: can(540, 480) + bubbles(410, 260, 260, 460, 60, 6, WHITE, .9) + ''.join(arrow(200 + i * 680, 480, 260 + i * 560, 480, GOLD, 12) for i in range(2))
    S['open_can'] = lambda: can(540, 520, 1.0, RED, True) + arrow(540, 230, 540, 80, GOLD, 18)
    S['bubbles_grow'] = lambda: can(540, 520, 1.0, RED, True) + bubbles(420, 330, 240, 380, 14, 28, WHITE, .9)
    S['spray'] = lambda: can(540, 600, 0.9, RED, True) + ''.join(f'<circle cx="{560 + 120 * math.sin(i)}" cy="{320 - i * 22}" r="{26 + (i % 3) * 8}" fill="{WHITE}" fill-opacity=".9"/>' for i in range(12))
    S['tap'] = lambda: can(480, 500) + finger(800, 380, 0.6) + ''.join(f'<path d="M{660 + i * 20},{330 + i * 30} l30,-10" stroke="{GOLD}" stroke-width="8"/>' for i in range(3))
    S['cans_study'] = lambda: ''.join(f'<rect x="{150 + (i % 8) * 100}" y="{260 + (i // 8) * 140}" width="70" height="120" rx="12" fill="{[GOLD, "#c9952c"][i % 2]}"/>' for i in range(24)) + txt(540, 200, '1031캔', 90, GOLD)
    S['no_shake'] = lambda: can(540, 500) + f'<circle cx="540" cy="500" r="330" fill="none" stroke="{GOLD}" stroke-width="12" stroke-dasharray="30 20"/>' + txt(540, 120, '흔들지 않기', 64, GOLD)
    # 046 shower singing
    S['shower'] = lambda: shower()
    S['tiles'] = lambda: shower() + f'<rect x="300" y="200" width="240" height="240" fill="none" stroke="{GOLD}" stroke-width="12"/>'
    S['bounce'] = lambda: shower() + person(380, 820, 2.0, GOLD) + f'<polyline points="440,420 860,250 520,120 860,60" stroke="{GOLD}" stroke-width="10" fill="none" stroke-dasharray="24 14"/>'
    S['reverb'] = lambda: shower() + person(380, 820, 2.0, GOLD) + ''.join(f'<circle cx="420" cy="420" r="{100 + i * 90}" fill="none" stroke="{GOLD}" stroke-width="8" stroke-opacity="{.9 - i * .2:.1f}"/>' for i in range(4))
    S['bass_room'] = lambda: shower() + f'<path d="M220,500 ' + ' '.join(f'q60,{-120 if i % 2 == 0 else 120} 120,0' for i in range(5)) + f'" stroke="{GOLD}" stroke-width="20" fill="none"/>'
    S['mask_notes'] = lambda: ''.join(f'<line x1="140" y1="{280 + i * 70}" x2="940" y2="{280 + i * 70}" stroke="{LIGHT}" stroke-width="5"/>' for i in range(5)) + ''.join(note(260 + i * 160, 300 + [60, 0, 120, 30, 80][i], 1.0, RED if i == 2 else GOLD) for i in range(5)) + f'<rect x="530" y="330" width="160" height="260" rx="30" fill="{SKY}" fill-opacity=".35"/>'
    S['singer'] = lambda: person(540, 780, 2.6, GOLD) + note(250, 300, 1.3) + note(820, 260, 1.1) + f'<polygon points="540,80 565,150 640,150 580,195 600,265 540,225 480,265 500,195 440,150 515,150" fill="{GOLD}"/>'
    if key in S:
        return S[key]()
    return None
