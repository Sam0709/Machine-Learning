import pydotplus
import PyPDF4
import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from IPython.display import Image
import os
import random
from drawnow import drawnow
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import time

# Transition Probabilities
p_ss = 0.8
p_sr = 0.2
p_rs = 0.4
p_rr = 0.6

# Initial Probabilities
p_s = 2 / 3
p_r = 1 / 3

# Emission Probabilities
p_sh = 0.8
p_sg = 0.2
p_rh = 0.4
p_rg = 0.6

moods = ['H', 'H', 'G', 'G', 'G', 'H']
probabilities = []
weather = []

if moods[0] == 'H':
    probabilities.append((p_s * p_sh, p_r * p_rh))
else:
    probabilities.append((p_s * p_sg, p_r * p_rg))

for i in range(1, len(moods)):
    yesterday_sunny, yesterday_rainy = probabilities[-1]
if moods[i] == 'H':
    today_sunny = max(yesterday_sunny * p_ss * p_sh, yesterday_rainy * p_rs * p_sh)
    today_rainy = max(yesterday_sunny * p_sr * p_rh, yesterday_rainy * p_rr * p_rh)
    probabilities.append((today_sunny, today_rainy))
else:
    today_sunny = max(yesterday_sunny * p_ss * p_sg, yesterday_rainy * p_rs * p_sg)
    today_rainy = max(yesterday_sunny * p_sr * p_rg, yesterday_rainy * p_rr * p_rg)
    probabilities.append((today_sunny, today_rainy))

for p in probabilities:
    if p[0] > p[1]:
         weather.append('S')
    else:
         weather.append('R')

print(weather)
print(probabilities)