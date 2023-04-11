import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from sympy import symbols, solve

M = ufloat(1.08, 0.02)
m = ufloat(0.16, 0.005)
l_0 = ufloat(1.03, 0.02)
l = ufloat(0.874, 0.001)
g = ufloat(9.822, 0.028)

J = ((1/3) * m * l_0**2) + (M* l**2)
D = g * (m * (l_0 / 2) + M *l)
