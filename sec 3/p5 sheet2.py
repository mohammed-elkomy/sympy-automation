from sympy import Eq

from commons import feedback, cascade, H2, G5, G1, H1, S, C2, G2, G3, G4, N, C1, R2, R1, render_exper, R, C, summing_junction

q52 = feedback(G1, H1, negative=True)
render_exper(q52, "q52")

q51 = feedback(G4, H2, negative=True)
render_exper(q51, "q51")

forward = cascade(G5, q51, G2 + G3, q52)
q53 = feedback(forward, 1, negative=True)
render_exper(Eq(C / R, q53), "q53")

render_exper(Eq(C / R, q53).simplify(numer=True, denom=True).expand(numer=True, denom=True), "q53expanded")
