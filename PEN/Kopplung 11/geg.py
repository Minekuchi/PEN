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
sheet_name = "S1P1geg"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

t = df["t / s"]
A1 = df["U_A1 / V"]
B1 = df["U_B1 / V"]

plt.scatter(t, A1, color="red")

t2 = ufloat(29.344, 0.03)
t1 = ufloat(2.592, 0.03)
omegageg = 15 * (2 * 3.1416)/(t2 - t1)



#plt.show()

print(f"omegageg = {omegageg} 1/s")
