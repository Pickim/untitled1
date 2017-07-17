from sympy import *

#from sympy import Symbol, limit, oo

n = Symbol('n')
s = ((n+3)/(n+2))**n
print limit(s, n, oo)

pprint(n*(sqrt(n**2+1)-n))

t = Symbol('t')
x = Symbol('x')

m = integrate(sin(t)/(pi-t),(t,0,x))
n = integrate(m,(x,0,pi))

print n

f = Function('f')
x = Symbol('x')

print dsolve(diff(f(x),x) - 2*f(x)*x,f(x))
