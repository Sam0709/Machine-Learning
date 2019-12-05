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




alp = 0.8 # learning rate or step
ep = 1.e-6
m = 51
x = np.linspace(0, 1, m)
y = 15 * x + 5 + np.random.normal(0, 0.4, x.shape); # Add Gaussian noise to original functio
plt.plot(x, y, "o")

w1 = np.random.rand()
w0 = np.random.rand() # random guess
err = 1
iter = 0
b=[0]
w4=[0]
w3=[0]
while err > 1.e-5:
    yh = (w1 * x + w0);
    DJ0 = (yh - y);
    dw0 = -alp * sum(DJ0) / (m);
    DJ1 = (yh - y)* x;
    dw1 = -alp * sum(DJ1) / (m)
    w0 = w0 + dw0;
    w1 = w1 + dw1;
    w3.append(w1)
    w4.append(w0)
    iter = iter + 1;

    j = (0.5 / m) * sum(y - w1 * x - w0)**2;
    b.append(j)

    err = abs(b[iter] - b[iter-1]);#careful about 'abs'


    def draw_fig():

        plt.figure(1, figsize=[5, 5])
        plt.subplot(221)
        plt.plot(x, y, "o",label="Random")
        plt.plot(x, yh, "r",label="Regression")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(prop={'size': 10, 'weight': 'light', 'style': 'italic'}, loc=0, facecolor='black', framealpha=0, \
                   bbox_to_anchor=(0.5, 0., 0.5, 0.5), edgecolor='r')


        plt.subplot(222)
        plt.plot(w3, b, "r")
        plt.xlabel('Iteration')
        plt.figure(1, figsize=[5, 5])

        ax=plt.subplot(223, projection='3d')# ax = fig.gca(224,projection='3d')
        X, Y = np.meshgrid(w3, w4)
        X1=np.array(X).reshape(len(w3),-1)
        Y1 = np.array(X).reshape(len(w4), -1)
        Z = (np.array(b)).reshape(np.shape(Y1)[0], -1)

        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
        #ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        # colorbar(surf, shrink=0.5, aspect=5)

        time.sleep(0.5)
        plt.tight_layout()

    drawnow(draw_fig)
    plt.pause(0.0005)
plt.show()
