from commons import summing_junction, feedback, cascade, G2, H2, H1, G3, G4, G1, render_exper

right = summing_junction(G3, G4 / G2)
temp1 = feedback(G1, H1, negative=False)

left = feedback(cascade(temp1, G2), H2)

tf = cascade(left, right).expand().simplify().expand(numer=True)

render_exper(tf)
