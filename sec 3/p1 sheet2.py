from sympy import Eq, symbols

from commons import feedback, cascade, H2, H, G5, G1, H1, S, C2, G2, G3, G4, N, C1, R2, R1, render_exper, R, C, summing_junction

q11 = feedback(G5, H, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q11, "q11")

q12 = feedback(cascade(q11, G4), H / G5, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q12, "q12")

q13 = feedback(cascade(q12, G3 * (G1 + G2)), 1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q13, "q13")

K = symbols("K")
q14 = (K * q13).simplify(numer=True, denom=True).expand(numer=True, denom=True)

render_exper(Eq(C / R, q14), "q14")
