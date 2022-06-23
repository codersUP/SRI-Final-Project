from sympy.logic.boolalg import to_dnf
from sympy.abc import A, B, C, symbols
print(to_dnf(B & (A | C)))
dic ={}
dic['x'] = symbols('comer') 

dic['y'] = symbols('comer1') 



bla = A
bla= bla & B 
bla = (bla)
bla |= (A&~B) | (B & C) | (~B & C & dic['x']) | dic['y']

a = to_dnf(bla, True)
print(a)