import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import scipy.optimize as spo

x = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
y = np.array(
    [388, 463, 538, 526, 482, 346, 247, 219, 193, 192, 167, 179, 226, 304, 482, 514, 577, 542, 429, 403, 392, 374, 488,
     524, 619, 682, 983, 1162, 1194, 1258, 1073, 896, 710, 832, 448, 388, 285, 242, 189, 96, 68, 64, 89, 34, 36, 32, 23,
     35, 29, 33, 63, 53])
X = np.array([np.ones(x.size), x, x * x, x * x * x, x * x * x * x])
Y = y

theta = np.dot(Y, np.linalg.pinv(X))

f = lambda x: theta[0] + theta[1] * x + theta[2] * x * x + theta[3] * x * x * x + theta[4] * x * x * x * x

xx = np.linspace(0, 52, 52)
yy = f(xx)

plt.plot(x, y, 'ro', label='Daily_Deaths')
plt.plot(xx, yy, 'b', label='Fitted_Equation')
plt.legend()
plt.show()
print(r2_score(y, f(xx)))

# optimizing
x_start = 0.0
result = spo.minimize(np.poly1d(np.polyfit(x, y, 4)), x_start, options={"disp": True})
if result.success:
    print("Success!")
    print(f"x = {result.x} y = {result.fun}")
else:
    print("Sorry, could not find a minimum.")
