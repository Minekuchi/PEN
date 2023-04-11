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
sheet_name = "S1P1gl"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

t = df["t  in s"]
A1 = df["pendulum 1"]
B1 = df["pendulum 2"]

plt.scatter(t, B1, color="red")

plt.show()

print("omegagl = 3.377 1/s")
