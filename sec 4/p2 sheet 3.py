from commons import P1, L, L1, TF, render_eqn, H2, G1, H1, G2, Delta1, Delta, L2, G4, G3, H3, H4, L3, L4, L13, L23, P2, Delta2
from sympy import Mul, Add

P1_ = Mul(G1, G2, evaluate=False)
render_eqn(P1, P1_, "P1", mul_symbol=".", order="none")

P2_ = Mul(G3, evaluate=False)
render_eqn(P2, P2_, "P2", mul_symbol=".", order="none")

L1_ = Mul(-G1, H1, evaluate=False)
render_eqn(L1, L1_, "L1", mul_symbol=".", order="none")

L2_ = Mul(-G1, H2, evaluate=False)
render_eqn(L2, L2_, "L2", mul_symbol=".", order="none")

L3_ = Mul(G1, G2, H3, evaluate=False)
render_eqn(L3, L3_, "L3", mul_symbol=".", order="none")

delta1_ = 1
render_eqn(Delta1, delta1_, "delta1_", mul_symbol=".")

delta2_ = Add(1, Mul(-1, Add(L1, L2, evaluate=False), evaluate=False), evaluate=False)
render_eqn(Delta2, delta2_, "delta2_", mul_symbol=".", order="none")

delta_ = Add(1, Mul(-1, Add(L1, L2, L3, evaluate=False), evaluate=False), evaluate=False)
render_eqn(Delta, delta_, "delta_", mul_symbol=".", order="none")

delta_ = 1 - (L1_ + L2_ + L3_)
render_eqn(Delta, delta_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "delta_", mul_symbol=".")

render_eqn(TF, (P1 * Delta1 + P2 * Delta2) / Delta, "TF1", mul_symbol=".", reverse=False)

Tf_ = (delta1_ * P1_ + delta2_ * P2_) / delta_
render_eqn(TF, Tf_.simplify(numer=True, denom=True).expand(numer=True, denom=True), "TF2", mul_symbol=".")
