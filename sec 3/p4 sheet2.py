from sympy import Eq

from commons import feedback, cascade, H2, G5, K, K1, K2, K3, G1, H1, S, C2, G2, G3, G4, N, C1, R2, R1, render_exper, R, C, summing_junction

q41 = feedback(G3, H1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)

render_exper(q41, "q41")

q42 = feedback(cascade(q41, K3), 1, negative=False).simplify(numer=True, denom=True).expand(numer=True, denom=True)

render_exper(q42, "q42")

q43 = feedback(cascade(q42, K2 + G2 / K3, G1), K1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)

render_exper(q43, "q43")

q44 = feedback(q43, H1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)

render_exper(Eq(C / R, q44), "q43")
