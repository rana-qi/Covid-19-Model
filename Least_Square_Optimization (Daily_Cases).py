import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import scipy.optimize as spo

x = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
y = np.array(
    [15535, 19717, 18083, 12154, 8708, 6328, 5139, 4972, 4413, 4229, 4148, 4298, 8632, 11962, 13679, 14596, 12162, 8778,
     6320, 8267, 9275, 10408, 13265, 14128, 22318, 35452, 52076, 49777, 28491, 23592, 17779, 13280, 16957, 19690, 13460,
     10972, 14909, 4986, 3069, 1654, 1136, 920, 888, 673, 2383, 546, 980, 1115, 1156, 1419, 1942, 5048])

X = np.array([np.ones(x.size), x, x * x, x*x*x, x*x*x*x, x*x*x*x*x, x*x*x*x*x*x, x*x*x*x*x*x*x])
Y = y

theta = np.dot(Y, np.linalg.pinv(X))

f = lambda x: theta[0] + theta[1] * x + theta[2] * x * x + theta[3] * x * x * x + theta[4] * x * x * x * x + theta[5] * x * x * x * x * x + theta[6] * x * x * x * x * x * x

xx = np.linspace(0, 52, 52)
yy = f(xx)

plt.plot(x, y, 'ro', label='Daily_Cases')
plt.plot(xx, yy, 'b', label='Fitted_Equation')
plt.legend()
plt.show()
print(r2_score(y, f(xx)))

# optimizing (Cost Function)
x_start = 2.0
result = spo.minimize(np.poly1d(np.polyfit(x, y, 6)), x_start, options={"disp": True})
if result.success:
    print("Success!")
    print(f"x = {result.x} y = {result.fun}")
else:
    print("Sorry, could not find a minimum.")
