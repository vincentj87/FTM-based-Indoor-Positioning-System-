from IPython.display import display
import sympy as sy
from sympy.vector import CoordSys3D
sy.init_printing()

x_tag,y_tag,z_tag=sy.symbols("x_tag y_tag z_tag",real=True)
x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1,d2,d3,d4=sy.symbols("x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4 d1 d2 d3 d4",real=True)
#Xu=Au^-1.Du

Au=sy.Matrix([
    [-2*x4+2*x1,-2*y4+2*y1,-2*z4+2*z1],
    [-2*x4+2*x2,-2*y4+2*y2,-2*z4+2*z2],
    [-2*x4+2*x3,-2*y4+2*y3,-2*z4+2*z3]
])
Au_inv=Au.inv()

Du= sy.Matrix([
    [d4**2-d1**2+x1**2-x4**2+y1**2-y4**2+z1**2-z4**2],
    [d4**2-d2**2+x2**2-x4**2+y2**2-y4**2+z2**2-z4**2],
    [d4**2-d3**2+x3**2-x4**2+y3**2-y4**2+z3**2-z4**2],
])
Xu=sy.simplify(Au_inv*Du)
print(Xu)