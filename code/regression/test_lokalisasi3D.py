import numpy as np
#koordinat tag
# x_tag= 3.2
# y_tag= 5
# z_tag= 7
#koordinat anch1
x1=-5.05
y1=-6.35
z1=1.381
#koordinat anch2
x2=-5.05
y2=6.35
z2=1.384
#koordinat anch3
x3=5.05
y3=6.35
z3=1.385
#koordinat anch4
x4 =5.05
y4=-6.35
z4=1.380

#jarak dari anchor menuju ke tag
# d1=((x_tag-x1)**2+(y_tag-y1)**2+(z_tag-z1)**2)**0.5
# d2=((x_tag-x2)**2+(y_tag-y2)**2+(z_tag-z2)**2)**0.5
# d3=((x_tag-x3)**2+(y_tag-y3)**2+(z_tag-z3)**2)**0.5
# d4=((x_tag-x4)**2+(y_tag-y4)**2+(z_tag-z4)**2)**0.5

d1=7.904




d2=11.359




d3=9.476




d4=4.78





print("jarak D1 : ",d1)
print("jarak D2 : ",d2)
print("jarak D3 : ",d3)
print("jarak D4 : ",d4)
#Au.Xu=Du
#AuT.Au.Xu=AuT.Du
#Xu=inv(AuT.Au).AuT.Du
#menciptakan matrix Au 
Au = np.array([
    [-2*x4+2*x1,-2*y4+2*y1,-2*z4+2*z1],
    [-2*x4+2*x2,-2*y4+2*y2,-2*z4+2*z2],
    [-2*x4+2*x3,-2*y4+2*y3,-2*z4+2*z3]
])
print(Au)
Au_transpose=np.transpose(Au)
print("Au transpose :\n",Au_transpose)
Du= np.array([
    [d4**2-d1**2+x1**2-x4**2+y1**2-y4**2+z1**2-z4**2],
    [d4**2-d2**2+x2**2-x4**2+y2**2-y4**2+z2**2-z4**2],
    [d4**2-d3**2+x3**2-x4**2+y3**2-y4**2+z3**2-z4**2],
])
print("Du: \n",Du)
AuT_dot_Au=np.dot(Au_transpose,Au)
print("AuT.Au : \n",AuT_dot_Au)

AuT_dot_Du=np.dot(Au_transpose,Du)
print("AuT.Du : \n",AuT_dot_Du)
Aut_dot_Au_inv=np.linalg.inv(AuT_dot_Au)
print("inv AuT.Au \n", Aut_dot_Au_inv)
Xu=np.dot(Aut_dot_Au_inv,AuT_dot_Du)
print("======hasil perhitungan======")
print("X : ",Xu[0]," Y : ",Xu[1]," Z : ",Xu[2])