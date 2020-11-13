from sympy import Add, Mul

from commons import P1, L1, TF, render_eqn, H2, G1, H1, G2, Delta1, Delta, L2

P1_ = G1 * G2
render_eqn(P1, P1_, "P1", mul_symbol=".")

L1_ = -H1
render_eqn(L1, L1_, "L1", mul_symbol=".")
L2_ = -G1 * G2 * H2
render_eqn(L2, L2_, "L1", mul_symbol=".")

delta1_ = 1
render_eqn(Delta1, delta1_, "delta1_", mul_symbol=".")

delta_ = Add(1, Mul(-1, Add(L1, L2, evaluate=False), evaluate=False), evaluate=False)
render_eqn(Delta, delta_, "delta_", mul_symbol=".", order="none")

delta_ = 1 - (L1_ + L2_)
render_eqn(Delta, delta_, "delta_", mul_symbol=".")

render_eqn(TF, P1 * Delta1 / Delta, "TF1", mul_symbol=".")
Tf_ = (delta1_ * P1_) / delta_
render_eqn(P1 * Delta1 / Delta, Tf_, "TF2", mul_symbol=".")
