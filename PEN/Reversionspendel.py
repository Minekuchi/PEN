import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from sympy import symbols, solve

# Data retrievel

sheet_id = "17OGKsLRMaH05Ag00z-kKX9SNPyC3H7zCTnW4fDtNBk8"
sheet_name = "AAA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

pos_number = df["Positions (Axis 1)"]
period_1 = df["Mean Period (s) 1"]
period_2 = df["Mean Period (s) 2"]

#plotting
plt.scatter(pos_number, period_1, color = "red")
plt.scatter(pos_number, period_2, color = "black")

#fitting

def line(x, m, c):
    return m*x + c

x_1 = np.array([3, 5])
y_11 = np.array([period_1[2], period_1[4]])
y_12 = np.array([period_2[2], period_2[4]])

x_2 = np.array([21, 22])
y_21 = np.array([period_1[20], period_1[21]])
y_22 = np.array([period_2[20], period_2[21]])

(m11, c11), cov1 = curve_fit(line, x_1, y_11)
(m12, c12), cov2 = curve_fit(line, x_1, y_12)

(m21, c21), cov3 = curve_fit(line, x_2, y_21)
(m22, c22), cov4 = curve_fit(line, x_2, y_22)

#plot tangents

y_data11 = pos_number * m11 + c11
y_data12 = pos_number * m12 + c12

y_data21 = pos_number * m21 + c21
y_data22 = pos_number * m22 + c22

plt.plot(pos_number, y_data11, color = "red")
plt.plot(pos_number, y_data12, color = "black")

plt.plot(pos_number, y_data21, color = "red")
plt.plot(pos_number, y_data22, color = "black")

#solving eq

x = symbols('x')

expr1 = (m11 - m12)*x + (c11 - c12)
sol1 = solve(expr1)

expr2 = (m21 - m22)*x + (c21 - c22)
sol2 = solve(expr2)

x1 = 4.44190219829517
x2 = 21.5110767645544

t1 = ufloat(1.79682, 0.00180)
t2 = ufloat(1.79518, 0.00180)

t = (t1 + t2) / 2

l_r = ufloat(0.8025, 0.002)

g = 4 * 3.1416**2 * ((l_r) / (t**2))

print(f"t = {t}")
print(f"g = {g}")


#plt.show()


