from sympy import *

S = symbols("S")


def parallel_shit(symbol1, symbol2):
    return (symbol1 * symbol2) / (symbol1 + symbol2)


def to_s_domain(symbol, type):
    if type == "C":
        symbol = 1 / (symbol * S)
    elif type == "L":
        symbol = (symbol * S)

    return symbol


R1, R2, R3, C1, C2, L = symbols('R1 R2 R3 C1 C2 L')

R1, R2, R3, C1, C2, L = symbols('R1 R2_{(x)} R3 C1 C2 \\alpha_{x}')
# the same
R1_s = to_s_domain(R1, "R")
R2_s = to_s_domain(R2, "R")
R3_s = to_s_domain(R3, "R")

# capacitor
C1_s = to_s_domain(C1, "C")
C2_s = to_s_domain(C2, "C")

# inductor
L_s = to_s_domain(L, "L")

# workout the circuit
Z1 = parallel_shit(R2_s, C1_s)
Z2 = Z1 + R1_s
Z3 = parallel_shit(Z2, L_s)
Z4 = parallel_shit(C2_s, R3_s)

transfer = Z4 / (Z4 + Z3)
init_printing()
pprint(transfer)
print("=" * 50)
print(latex(transfer.simplify().expand().simplify()))

exp = Z3.simplify().expand().simplify()
print(exp)
preview(exp, viewer='file', filename='output.png', dvioptions=['-D', '1200'])
#preview(exp, viewer='file', filename='output.png',mul_symbol='dot', dvioptions=['-D', '1200'])