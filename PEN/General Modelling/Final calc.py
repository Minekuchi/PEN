import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from sympy import symbols, solve

wgl_dir = np.array([3.377, 3.377, 3.379])
wgeg_dir = np.array([3.523, 3.867, 4.348])
K_dir = np.array([0.0423, 0.1347, 0.2475])

wgl2_dir = 3.377
wgeg2_dir = 3.484
K2_dir = 0.0312

wgl_s = np.array([3.377, 3.635, 3.829])
wgeg_s = np.array([3.526, 4.125, 4.803])
K_s = np.array([0.0433, 0.1258, 0.2228])

wgl2_s = 3.401
wgeg2_s = 3.513
K2_s = 0.0324

wgl_calc = np.array([3.382, 3.382, 3.382])
#wgeg_calc = np.array([
#K_calc

J = 0.8816
D = 10.081

#plotting

r = np.array([0.281, 0.526, 0.780])

plt.plot(r, wgl_dir, color = "red")
plt.plot(r, wgl_s, color = "black")

plt.plot(r, wgeg_dir, color = "red")
plt.plot(r, wgeg_s, color = "black")

#plt.show()

#calc of kappa

#direct, spring 1
kap_dir_array = ((wgeg_dir**2 * J) - D)/(2 * r**2)
kap_dir = 0
for i in range(3):
    kap_dir = kap_dir + kap_dir_array[i]
kap_dir = kap_dir / 3

#direct, spring 2
kap2_dir = ((wgeg2_dir**2 * J) - D)/(2 * 0.281**2)

#schwebung, spring 1
kap_s_array = ((wgeg_s**2 * J) - D)/(2 * r**2)

kap_s = 0
for i in range(3):
    kap_s = kap_s + kap_s_array[i]
kap_s = kap_s / 3

#schwebung, spring 2
kap2_s = ((wgeg2_s**2 * J) - D)/(2 * 0.281**2)



#direct, spring 1, K
kap_dir_array2 = (K_dir * D)/((1 - K_dir)* r**2)
kap_dir2 = 0
for i in range(3):
    kap_dir2 = kap_dir2 + kap_dir_array2[i]
kap_dir2 = kap_dir2 / 3

#schwebung, spring 1, K
kap_s_array2 = (K_s * D)/((1 - K_s)* r**2)
kap_s2 = 0
for i in range(3):
    kap_s2 = kap_s2 + kap_s_array2[i]
kap_s2 = kap_s2 / 3

#direct, spring 2, K
kap2_dir2 = (K2_dir * D)/((1 - K2_dir)* 0.281**2)

#schwebung, spring 2, K
kap2_s2 = (K2_s * D)/((1 - K2_s)* 0.281**2)


#spring 1
kap1 = (kap_dir + kap_s + kap_dir2 + kap_s2) / 4

#spring 2
kap2 = (kap2_dir + kap2_s + kap2_dir2 + kap2_s2) / 4

print(f"kappa1 = {kap1}")
print(f"kappa2 = {kap2}")




