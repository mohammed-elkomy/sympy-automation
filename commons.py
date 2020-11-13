from sympy import symbols, preview, latex, Eq

import os
import re

S = symbols("S")

G, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10 = symbols('G_{(s)}  G_{^{1}(s)} G_{^{2}(s)} G_{^{3}(s)} G_{^{4}(s)} G_{^{5}(s)} G_{^{6}(s)} G_{^{7}(s)} G_{^{8}(s)} G_{^{9}(s)} G_{^{10}(s)} ')

Delta, Delta1, Delta2, Delta3, Delta4, Delta5, Delta6, Delta7, Delta8, Delta9, Delta10 = symbols('\Delta \Delta_{1} \Delta_{2} \Delta_{3} \Delta_{4} \Delta_{5} \Delta_{6} \Delta_{7} \Delta_{8} \Delta_{9} \Delta_{10}')
H, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10 = symbols('H_{(s)}  H_{^{1}(s)} H_{^{2}(s)} H_{^{3}(s)} H_{^{4}(s)} H_{^{5}(s)} H_{^{6}(s)} H_{^{7}(s)} H_{^{8}(s)} H_{^{9}(s)} H_{^{10}(s)} ')
R, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10 = symbols('R_{(s)}  R_{^{1}(s)} R_{^{2}(s)} R_{^{3}(s)} R_{^{4}(s)} R_{^{5}(s)} R_{^{6}(s)} R_{^{7}(s)} R_{^{8}(s)} R_{^{9}(s)} R_{^{10}(s)} ')
C, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 = symbols('C_{(s)}  C_{^{1}(s)} C_{^{2}(s)} C_{^{3}(s)} C_{^{4}(s)} C_{^{5}(s)} C_{^{6}(s)} C_{^{7}(s)} C_{^{8}(s)} C_{^{9}(s)} C_{^{10}(s)} ')
N, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10 = symbols('N_{(s)}  N_{^{1}(s)} N_{^{2}(s)} N_{^{3}(s)} N_{^{4}(s)} N_{^{5}(s)} N_{^{6}(s)} N_{^{7}(s)} N_{^{8}(s)} N_{^{9}(s)} N_{^{10}(s)} ')
K, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10 = symbols('K K_{1} K_{2} K_{3} K_{4} K_{5} K_{6} K_{7} K_{8} K_{9} K_{10}')
E, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10 = symbols('E_{(s)}  E_{^{1}(s)} E_{^{2}(s)} E_{^{3}(s)} E_{^{4}(s)} E_{^{5}(s)} E_{^{6}(s)} E_{^{7}(s)} E_{^{8}(s)} E_{^{9}(s)} E_{^{10}(s)} ')
X, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = symbols('X_{(s)}  X_{^{1}(s)} X_{^{2}(s)} X_{^{3}(s)} X_{^{4}(s)} X_{^{5}(s)} X_{^{6}(s)} X_{^{7}(s)} X_{^{8}(s)} X_{^{9}(s)} X_{^{10}(s)} ')
A, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10 = symbols('A_{(s)}  A_{^{1}(s)} A_{^{2}(s)} A_{^{3}(s)} A_{^{4}(s)} A_{^{5}(s)} A_{^{6}(s)} A_{^{7}(s)} A_{^{8}(s)} A_{^{9}(s)} A_{^{10}(s)} ')
B, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10 = symbols('B_{(s)}  B_{^{1}(s)} B_{^{2}(s)} B_{^{3}(s)} B_{^{4}(s)} B_{^{5}(s)} B_{^{6}(s)} B_{^{7}(s)} B_{^{8}(s)} B_{^{9}(s)} B_{^{10}(s)} ')
P, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 = symbols('P_{(s)}  P_{^{1}(s)} P_{^{2}(s)} P_{^{3}(s)} P_{^{4}(s)} P_{^{5}(s)} P_{^{6}(s)} P_{^{7}(s)} P_{^{8}(s)} P_{^{9}(s)} P_{^{10}(s)} ')
L, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26, L27, L28, L29, L30, L31, L32, L33, L34, L35, L36, L37, L38, L39, L40, L41, L42, L43, L44, L45, L46, L47, L48, L49, L50, L51, L52, L53, L54, L55, L56, L57, L58, L59, L60, L61, L62, L63, L64, L65, L66, L67, L68, L69, L70, L71, L72, L73, L74, L75, L76, L77, L78, L79, L80, L81, L82, L83, L84, L85, L86, L87, L88, L89, L90, L91, L92, L93, L94, L95, L96, L97, L98, L99 = symbols(
    'L_{(s)}  L_{^{1}(s)} L_{^{2}(s)} L_{^{3}(s)} L_{^{4}(s)} L_{^{5}(s)} L_{^{6}(s)} L_{^{7}(s)} L_{^{8}(s)} L_{^{9}(s)} L_{^{10}(s)} L_{^{11}(s)} L_{^{12}(s)} L_{^{13}(s)} L_{^{14}(s)} L_{^{15}(s)} L_{^{16}(s)} L_{^{17}(s)} L_{^{18}(s)} L_{^{19}(s)} L_{^{20}(s)} L_{^{21}(s)} L_{^{22}(s)} L_{^{23}(s)} L_{^{24}(s)} L_{^{25}(s)} L_{^{26}(s)} L_{^{27}(s)} L_{^{28}(s)} L_{^{29}(s)} L_{^{30}(s)} L_{^{31}(s)} L_{^{32}(s)} L_{^{33}(s)} L_{^{34}(s)} L_{^{35}(s)} L_{^{36}(s)} L_{^{37}(s)} L_{^{38}(s)} L_{^{39}(s)} L_{^{40}(s)} L_{^{41}(s)} L_{^{42}(s)} L_{^{43}(s)} L_{^{44}(s)} L_{^{45}(s)} L_{^{46}(s)} L_{^{47}(s)} L_{^{48}(s)} L_{^{49}(s)} L_{^{50}(s)} L_{^{51}(s)} L_{^{52}(s)} L_{^{53}(s)} L_{^{54}(s)} L_{^{55}(s)} L_{^{56}(s)} L_{^{57}(s)} L_{^{58}(s)} L_{^{59}(s)} L_{^{60}(s)} L_{^{61}(s)} L_{^{62}(s)} L_{^{63}(s)} L_{^{64}(s)} L_{^{65}(s)} L_{^{66}(s)} L_{^{67}(s)} L_{^{68}(s)} L_{^{69}(s)} L_{^{70}(s)} L_{^{71}(s)} L_{^{72}(s)} L_{^{73}(s)} L_{^{74}(s)} L_{^{75}(s)} L_{^{76}(s)} L_{^{77}(s)} L_{^{78}(s)} L_{^{79}(s)} L_{^{80}(s)} L_{^{81}(s)} L_{^{82}(s)} L_{^{83}(s)} L_{^{84}(s)} L_{^{85}(s)} L_{^{86}(s)} L_{^{87}(s)} L_{^{88}(s)} L_{^{89}(s)} L_{^{90}(s)} L_{^{91}(s)} L_{^{92}(s)} L_{^{93}(s)} L_{^{94}(s)} L_{^{95}(s)} L_{^{96}(s)} L_{^{97}(s)} L_{^{98}(s)} L_{^{99}(s)} ')

TF = symbols("T.F")


def feedback(forward, backward, negative=True):
    forward = (forward + S - S).expand()
    backward = (backward + S - S).expand()
    temp = forward \
           / (1 - (-1 if negative else +1) * (forward * backward))

    return temp


def summing_junction(*inputs):
    temp = (inputs[0] + S - S).expand()
    for input_ in inputs[1:]:
        temp += (input_ + S - S).expand()
    return temp


def cascade(*inputs):
    temp = (inputs[0] + S - S).expand()
    for input_ in inputs[1:]:
        temp *= (input_ + S - S).expand()
    return temp


root_imgs_path = "../imgs"

for img in os.listdir(root_imgs_path):
    os.remove(os.path.join(root_imgs_path, img))

counter = 0


def render_eqn(left, right, name, mul_symbol=".", reverse=True, order=None):
    render_exper(Eq(left, right), name, mul_symbol=mul_symbol, reverse=reverse, order=order)


def render_exper(esp, name, mul_symbol=".", reverse=True, order=None):
    global counter
    if order is None:
        order = "rev-lex" if reverse else "lex"
    esp = r"$\displaystyle {} $".format(latex(esp, mul_symbol=mul_symbol, order=order, long_frac_ratio=2))
    # esp = r"$\displaystyle  \left(x+1 \right)  $"
    colors = ["1,0,0",
              "0,0,1",
              "0,1,0",
              "0.82, 0.41, 0.12",
              "1, 0,1",
              "0, 1,1",
              "0.29, 0.33, 0.13",
              "0.58, 0.0, 0.83",
              "0,0,0",
              "0,0,0",
              "0,0,0",
              "0,0,0",
              "0,0,0",
              ]

    def get_left_sizes(max_depth):
        left_sizes = [r"\Bigg(", r"\bigg(", r"\Big(", r"\big(", ]
        if max_depth < len(left_sizes):
            return left_sizes[-max_depth:]
        else:
            return [r"\Bigg("] * (max_depth - 4) + left_sizes

    def get_right_sizes(max_depth):
        right_sizes = [r"\Bigg)", r"\bigg)", r"\Big)", r"\big)", ]
        if max_depth < len(right_sizes):
            return right_sizes[-max_depth:]
        else:
            return [r"\Bigg)"] * (max_depth - 4) + right_sizes

    left_regex = re.compile(r'\\left\(', re.S)
    right_regex = re.compile(r'\\right\)', re.S)
    left_matches = list(left_regex.finditer(esp))
    right_matches = list(right_regex.finditer(esp))
    parentheses = sorted(left_matches + right_matches, key=lambda item: item.span(0))
    match_to_color = {}
    depth = 0
    for parenthesis in parentheses:
        if ")" in parenthesis.group(0):
            depth -= 1

        match_to_color[str(parenthesis)] = r"\color[rgb]{{{before}}}{paren}\color{{{after}}}".format(paren=parenthesis.group(0), before=colors[depth], after="black")
        if "(" in parenthesis.group(0):
            depth += 1

    # max_depth = len(left_regex.findall(esp))
    # left_sizes = get_left_sizes(max_depth)
    # right_sizes = get_right_sizes(max_depth)
    regex = re.compile(r'\\right\)|\\left\(', re.S)

    esp = regex.sub(lambda m: match_to_color[str(m)], esp)

    print(esp)
    preview(esp, viewer='file', filename=os.path.join(root_imgs_path, '{}-{}.png'.format(counter, name)), packages=("color",), dvioptions=['-D', '1200'])
    counter += 1
