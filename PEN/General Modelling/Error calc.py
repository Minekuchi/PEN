import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from sympy import symbols, solve

wgl_11 = (ufloat(3.377, 0.006) + ufloat(3.377, 0.007))/2
wgl_12 = (ufloat(3.377, 0.006) + ufloat(3.635, 0.007))/2
wgl_13 = (ufloat(3.379, 0.006) + ufloat(3.829, 0.007))/2

wgeg_11 = (ufloat(3.523, 0.006) + ufloat(3.526, 0.007))/2
wgeg_12 = (ufloat(3.867, 0.006) + ufloat(4.125, 0.007))/2
wgeg_13 = (ufloat(4.348, 0.006) + ufloat(4.803, 0.007))/2

K_11 = (wgeg_11**2 - wgl_11**2)/(wgeg_11**2 + wgl_11**2)
K_12 = (wgeg_12**2 - wgl_12**2)/(wgeg_12**2 + wgl_12**2)
K_13 = (wgeg_13**2 - wgl_13**2)/(wgeg_13**2 + wgl_13**2)
