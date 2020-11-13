from sympy import Eq, symbols, latex

from commons import feedback, cascade, G1, B, X, E, A, S, C2, G2, G3, G4, N, C1, R2, R1, B1, B2, B3, B4, B5, render_exper, R, C, summing_junction

nested = B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * (B1 + B2 * B3)))))))))
#nested = B1 + B2 * (B1 + B2 * (B1 + B2 ))
print(latex(nested))
render_exper(nested, "C_over_E", mul_symbol="", reverse=False)
exit(

)

kom71 = feedback((10 / (S * (S + 1))).expand(), .5 * S, negative=True)
kom71 = kom71.simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(kom71, "KOM71", mul_symbol="", reverse=False)

kom72 = (cascade(kom71, (S + 4))).simplify(numer=True, denom=True).expand(numer=True, denom=True).expand(numer=True)
render_exper(kom72, "KOM72", mul_symbol="", reverse=False)

kom73 = feedback(kom72.expand(), 1, negative=True).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(kom73, "kom73", mul_symbol="", reverse=False)

kom74 = cascade(1 + (3 / (S + 4)), kom73)
eq = Eq(C / R, kom74).simplify(numer=True, denom=True).expand(numer=True, denom=True).simplify(numer=True, denom=True)
render_exper(eq, "kom74", mul_symbol="", reverse=False)

backward = summing_junction(S + 4, .5 * S)
kom75 = feedback((10) / (S * (S + 1)).expand(), backward, negative=True).expand(numer=True, denom=True).simplify(numer=True, denom=True)
render_exper(kom75, "kom75", mul_symbol="", reverse=False)

kom76 = cascade((S * (S + 1)).expand() / (10), kom75)
eq = Eq(C / N, kom76).simplify(numer=True, denom=True).expand(numer=True, denom=True).simplify(numer=True, denom=True).expand(numer=True).simplify(numer=True, denom=True)
render_exper(eq, "kom76", mul_symbol="", reverse=False)

BA = kom72 * (3 / (S + 4))
kom77 = ((kom72 + BA) / (1 - BA)).simplify(numer=True, denom=True).expand(numer=True, denom=True)
render_exper(Eq(C / E, kom77), "C_over_E", mul_symbol="", reverse=False)
#########################
eq_1 = Eq(X, A * R + E)
eq_2 = Eq(C, X * B)
eq_3 = Eq(E, R - C)
render_exper(eq_1, "eq_1", mul_symbol="", reverse=False)
render_exper(eq_2, "eq_2", mul_symbol="", reverse=False)
render_exper(eq_3, "eq_3", mul_symbol="", reverse=False)

eq_4 = Eq(C, (A * R + E) * B)
render_exper(eq_4, "eq_4", mul_symbol="", reverse=False)

eq_5 = Eq(C, (A * (E + C) + E) * B)
render_exper(eq_5, "eq_5", mul_symbol="", reverse=False)

eq_6 = eq_5.expand().simplify(numer=True, denom=True)
render_exper(eq_6, "eq_6", mul_symbol="", reverse=False)

render_exper(Eq(C * (1 - A * B), E * (A * B + B)), "eq_7", mul_symbol="", reverse=False)
render_exper(Eq(C / E, (A * B + B) / (1 - A * B)).subs({A: (3 / (S + 4)), B: kom72}).expand(numer=True, denom=True).simplify(numer=True, denom=True), "eq_9", mul_symbol="", reverse=False)

render_exper(Eq(C / E, (A * B + B) / (1 - A * B)), "eq_8", mul_symbol="", reverse=True)
