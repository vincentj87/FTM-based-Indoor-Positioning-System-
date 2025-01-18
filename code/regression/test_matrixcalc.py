import numpy as np
x1=0
y1=0
x2=10
y2=0
x3=0
y3=10
d1=7
d2=7.2
d3=6.6
Au= np.array([
            [2*(x1-x3),2*(y1-y3)],
            [2*(x2-x3),2*(y2-y3)]
             ])
Du=np.array([[x1**2-x3**2+y1**2-y3**2+d3**2-d1**2],
            [x2**2-x3**2+y2**2-y3**2+d3**2-d2**2]])
Au_transpose=np.transpose(Au)
a=np.dot(Au_transpose,Au)
a_inv=np.linalg.inv(a)
b = np.dot(Au_transpose,Du)
Xu=np.dot(a_inv,b)
print(Xu)

print("test")