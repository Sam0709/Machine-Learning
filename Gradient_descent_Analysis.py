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


alp = 1.5 # learning rate or step
ep = 1.e-6
m = 51
x = np.linspace(0, 1, m)
y = 15 * x + 5 + np.random.normal(0, 0.4, x.shape); # Add Gaussian noise to original functio
plt.plot(x, y, "o")

w1 = np.random.rand(1)#https://www.geeksforgeeks.org/numpy-random-rand-python/
#"1D Array filled with random values : \n", array
w0 = np.random.rand(1) # random guess
#j[iter] = (0.5 / m) * sum(y - w1 * x - w0)** 2
err = 1
iter = 0
b=[0]
w3=[0]
while err > 1.e-5:
    yh = (w1 * x + w0);
    DJ0 = (yh - y);
    dw0 = -alp * sum(DJ0) / (m);
    DJ1 = (yh - y)* x;
    dw1 = -alp * sum(DJ1) / (m)
    print("ok",w0,w1)
    w0 = w0 + dw0;
    w1 = w1 + dw1;
    w3.append(w1)
    iter = iter + 1;
    print("hey", w0, w1)

    j = (0.5 / m) * sum(y - w1 * x - w0)**2;
    b.append(j)

    err = abs(b[iter] - b[iter-1]);#carefull abour 'abs'
    print(iter,err)
    def draw_fig():
        plt.subplot(2, 1, 1)
        plt.plot(x, y, "o",label="Random")
        plt.plot(x, yh, "r",label="Regression")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(prop={'size': 10, 'weight': 'light', 'style': 'italic'}, loc=0, facecolor='black', framealpha=0, \
                   bbox_to_anchor=(0.5, 0., 0.5, 0.5), edgecolor='r')
        plt.figure(1)
        plt.plot(w3, b, "r")
        plt.figure(2)
    drawnow(draw_fig)# continuos minimizing
    plt.pause(0.0005)
plt.show()