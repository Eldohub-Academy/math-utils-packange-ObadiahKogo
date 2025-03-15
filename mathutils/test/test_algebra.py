## 4x-34=-2
from sympy import symbols,Eq,solve

x=symbols("x")
equation=Eq(4*x-34,-2)
sln=solve(equation,x)
print(sln)