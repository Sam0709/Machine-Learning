import pydotplus
import numpy as np
import pandas as pd
import sklearn
import random
import time
from tkinter import*
from itertools import *


root=Tk()

def ok():

    myCanvas = Canvas(root, width=700, height=650,bg="blue")

    def create_circle(x, y, r, canvasName):
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return canvasName.create_oval(x0, y0, x1, y1,fill= "red")

    b = [300,300]
    m=0
    for i in count(0):
          m=m+1
          b.append(random.randint(100,500))
          b.append(random.randint(100,500))

          myCanvas.create_text(350, 25, text="RANDOM DISTANCE", font=("arial", 20, 'bold'), fill="#33ff71")
          myCanvas.create_text(50, 25, text=m, font=("arial", 16, 'bold'), fill="yellow",tags="hmm")
          create_circle(300, 300, 35, myCanvas)
          myCanvas.create_text(300,300, text=0, font=("arial", 12, 'bold'), fill="yellow")
          create_circle((b[len(b)-2:])[0], (b[len(b)-2:])[1], 35, myCanvas)
          myCanvas.create_text((b[len(b)-2:])[0], (b[len(b)-2:])[1], text=m, font=("arial", 12, 'bold'), fill="yellow")
          myCanvas.create_line(b[len(b)-4:],dash=(4, 2),fill="white",width=2)

          x1=b[len(b)-4:]
          y1=b[len(b)-2:]
          print("count", m, b,x1,y1)

          def dist():
              c = []
              for i in range(int(len(x1) / 2)):
                  b1 = (np.array(x1)).reshape(-1, 2)
                  b2 = b1[i]
                  # print(b2)
                  b3 = np.delete(b1, i, 0)
                  # print(b3)
                  dist = (b2 - b3) ** 2
                  dist = np.sum(dist, axis=1)
                  dist = np.sqrt(dist)
                  c.append(dist)
                  # print(dist)

              j = (np.array(c)).reshape(1, -1)
              j1=np.unique(j)
              j2=np.sum(j1)
              return j2

          print("Distance:",dist())
          myCanvas.create_text(650, 25, text=round(dist()), font=("arial", 16, 'bold'), fill="yellow", tags="xyz")

          myCanvas.pack()
          root.update()
          # myCanvas.delete("all")

          time.sleep(1)
          myCanvas.delete("hmm")
          myCanvas.delete("xyz")


    return root.mainloop()
print(ok())