from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import quandl
import random
from pandas import *
import math
from sklearn import *
from sklearn.linear_model import *

def sigmoid(x):
    a=1/(1+np.exp(-x))
    return a

def sigmoid_derivative(x):
    s=x*(1-x)
    return s

tarining_input=np.array([[0,0,1],
                         [1,1,1],
                         [1,0,1],
                         [0,1,1]])

training_output=np.array([[0,1,1,0]]).T
np.random.seed(1)
synaptic_weight=2*np.random.random((3,1))-1

for i in range(100000):
    input_layer=tarining_input
    output=sigmoid(np.dot(input_layer,synaptic_weight))
    error=training_output-output
    adjustment=error*sigmoid_derivative(output)
    synaptic_weight+=np.dot(input_layer.T,adjustment)

print(output)



