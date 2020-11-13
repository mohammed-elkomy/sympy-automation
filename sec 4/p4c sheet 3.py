from commons import P1, L, L1, TF, render_eqn, H2, G1, H1, G2, Delta1, Delta, L2, G4, G3, H3, H4, L3, L4, L13, L23
from sympy import Mul, Add

P1_ = Mul(G1, G2, G3, G4, evaluate=False)
render_eqn(P1, P1_, "P1", mul_symbol=".", order="none")

L1_ = Mul(-G1, G2, H2, evaluate=False)
render_eqn(L1, L1_, "L1", mul_symbol=".", order="none")

L2_ = Mul(-G2, H1, evaluate=False)
render_eqn(L2, L2_, "L2", mul_symbol=".", order="none")

L3_ = Mul(-G4, H3, evaluate=False)
render_eqn(L3, L3_, "L3", mul_symbol=".", order="none")

L4_ = Mul(-G2, G3, G4, H4, evaluate=False)
render_eqn(L4, L4_, "L4", mul_symbol=".", order="none")

L13_ = Mul(G1, G2, G4, H2, H3, evaluate=False)
render_eqn(L13, L13_, "L13_", mul_symbol=".", order="none")

L23_ = Mul(G2, G4, H1, H3, evaluate=False)
render_eqn(L23, L23_, "L23_", mul_symbol=".", order="none")

delta1_ = 1
render_eqn(Delta1, delta1_, "delta1_", mul_symbol=".")

delta_ = Add(1, Mul(-1, Add(L1, L2, L3, L4, evaluate=False), evaluate=False), Add(L13, L23, evaluate=False), evaluate=False)
render_eqn(Delta, delta_, "delta_", mul_symbol=".", order="none")

delta_ = 1 - (L1_ + L2_ + L3_ + L4_) + L13_ + L23_
render_eqn(Delta, delta_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "delta_", mul_symbol=".")

render_eqn(TF, P1 * Delta1 / Delta, "TF1", mul_symbol=".")

Tf_ = (delta1_ * P1_) / delta_
render_eqn(P1 * Delta1 / Delta, Tf_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "TF2", mul_symbol=".")
