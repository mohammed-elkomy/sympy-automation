from sympy import Eq

from commons import feedback, cascade, H2, G5, G1, H1, S, C2, G2, G3, G4, N, C1, R2, R1, render_exper, R, C, summing_junction

q31 = feedback(G1, H1, negative=False)
render_exper(q31, "q31")

q32 = summing_junction(cascade(1 + G1, q31, G1), G1).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q32, "q32")

q33 = feedback(cascade(q32, G1), H1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(q33, "q33")

q34 = cascade(G1, q33).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(Eq(C / R, q34), "q34")
