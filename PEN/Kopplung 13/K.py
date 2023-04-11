import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from sympy import symbols, solve

#K calc

w_gl = ufloat(3.377, 0.006)
w_geg = ufloat(4.348, 0.006)

K = (w_geg**2 - w_gl**2) / (w_geg**2 + w_gl**2)

print(f"K = {K}")
