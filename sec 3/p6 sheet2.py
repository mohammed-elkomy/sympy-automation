from sympy import Eq

from commons import feedback, cascade, G1, C2, G2, G3, G4, C1, R2, R1, render_exper

feedback_exp = feedback(G1, cascade(G2, G3, G4), negative=True)
KOM61 = Eq(C1 / R1, feedback_exp)
render_exper(KOM61, "KOM61")

feedback_exp = feedback(-cascade(G1, G3, G4), G2, negative=False)
KOM62 = Eq(C1 / R2, feedback_exp)
render_exper(KOM62, "KOM62")

KOM65 = Eq(KOM61.lhs + KOM62.lhs, KOM61.rhs + KOM62.rhs).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(KOM65, "KOM65")

feedback_exp = feedback(cascade(G1, G2, G4), G3, negative=True)
KOM63 = Eq(C2 / R1, feedback_exp)
render_exper(KOM63, "KOM63")

feedback_exp = feedback(G4, -cascade(G1, G2, G3), negative=False)
KOM64 = Eq(C2 / R2, feedback_exp)
render_exper(KOM64, "KOM64")

KOM66 = Eq(KOM63.lhs + KOM64.lhs, KOM63.rhs + KOM64.rhs).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(KOM66, "KOM66")
