import numpy as np
import matplotlib.pyplot as plt    
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
X = 4 * np.random.rand(100,1) - 2
y = 4 + 2 * X + 7 * X**2 + 15 * X**3 + 12 * X**4 + 20 * np.random.randn(100,1)

poly_features = PolynomialFeatures(degree=15,include_bias=False)
X_poly = poly_features.fit_transform(X)

reg = LinearRegression()
reg.fit(X_poly ,y)

X_vals=np.linspace(-2,2,100).reshape(-1,1)
X_vals_poly = poly_features.transform (X_vals)


y_vals=reg.predict(X_vals_poly)


plt.scatter(X,y)
plt.plot(X_vals,y_vals,color="red")
plt.show()