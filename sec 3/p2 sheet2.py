from sympy import Eq

from commons import feedback, cascade, H2, G5, G1, H1, S, C2, G2, G3, G4, N, C1, R2, R1, render_exper, R, C, summing_junction

q21 = feedback(G1, H1, negative=False)
render_exper(q21, "q21")

q22 = feedback(q21, cascade(G2, H2), negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q22, "q22")

q23 = cascade(q22, G4 + cascade(G2, G3)).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(Eq(C/R,q23), "q23")
