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

class NeuralNetwork():
      def __init__(self):
          np.random.seed(1)
          self.synaptic_weight = 2 * np.random.random((3, 1)) - 1



      def sigmoid(self,x):
          a=1/(1+np.exp(-x))
          return a

      def sigmoid_derivative(self,x):
          s=x*(1-x)
          return s

      def train(self,tarining_input,training_output,training_itrration):

             for i in range(training_itrration):

                  output=self.think(tarining_input)
                  error=training_output-output
                  adjustment=np.dot(tarining_input.T,error*self.sigmoid_derivative(output))
                  self.synaptic_weight+=adjustment

      def think(self,inputs):
             inputs=inputs.astype(float)
             output=self.sigmoid(np.dot(inputs,self.synaptic_weight))

             return output

if __name__ == '__main__':

      neural_network=NeuralNetwork()
      tarining_input=np.array([[0,0,1],
                               [1,1,1],
                               [1,0,1],
                               [0,1,1]])

      training_output=np.array([[0,1,1,0]]).T

      neural_network.train(tarining_input,training_output,1000)
      print(neural_network.synaptic_weight)



A=str(input("input 1:"))
B=str(input("input 2:"))
C=str(input("input 3:"))
k=neural_network.think(np.array([A,B,C]))
print(k)
