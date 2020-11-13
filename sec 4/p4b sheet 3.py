from commons import P1, L1, TF, render_eqn, H2, G1, H1, G2, Delta1, Delta, L2, G4, G3, H3, H4, L3, L4
from sympy import Mul, Add

P1_ = Mul(G1, G2, G3, G4, evaluate=False)
render_eqn(P1, P1_, "P1", mul_symbol=".", order="none")

L1_ = Mul(-H1, G1, G2, G3, G4, evaluate=False)
render_eqn(L1, L1_, "L1", mul_symbol=".", order="none")

L2_ = -Mul(H2, G2, G3, G4, evaluate=False)
render_eqn(L2, L2_, "L2", mul_symbol=".", order="none")

L3_ = Mul(-H3, G3, G4, evaluate=False)
render_eqn(L3, L3_, "L3", mul_symbol=".", order="none")

L4_ = -Mul(H4, G4, evaluate=False)
render_eqn(L4, L4_, "L4", mul_symbol=".", order="none")

delta1_ = 1
render_eqn(Delta1, delta1_, "delta1_", mul_symbol=".")

delta_ = Add(1, Mul(-1, Add(L1, L2, L3, L4, evaluate=False), evaluate=False), evaluate=False)
render_eqn(Delta, delta_, "delta_", mul_symbol=".", order="none")

delta_ = 1 - (L1_ + L2_ + L3_ + L4_)
render_eqn(Delta, delta_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "delta_", mul_symbol=".")

render_eqn(TF, P1 * Delta1 / Delta, "TF1", mul_symbol=".")

Tf_ = (delta1_ * P1_) / delta_
render_eqn(P1 * Delta1 / Delta, Tf_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "TF2", mul_symbol=".")
