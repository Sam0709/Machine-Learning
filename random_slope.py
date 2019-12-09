import pydotplus
import numpy as np
import pandas as pd
import sklearn
import random
import time
from tkinter import*

root=Tk()  # root.geometry('200x150') # tk enter window

def ok():
      myCanvas = Canvas(root, width=800, height=600,bg="blue")

      def create_circle(x, y, r, canvasName): #center coordinates, radius
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return canvasName.create_oval(x0, y0, x1, y1,fill= "red")

      def mate():
            a= np.zeros((4,2))
            for i in range (4):
               for j in range(2):
                  a[i][j]=np.random.randint(100,500)
            return a


      count=0
      while True:
          count = count + 1
          myCanvas.create_text(400, 25, text="LET'S TRY YOUR LUCK", font=("arial", 20, 'bold'), fill="#33ff71")
          myCanvas.create_text(50, 25, text=(round(100/count,2),'%'), font=("arial", 16, 'bold'), fill="yellow")
          m = np.random.randint(4)
          n = np.random.randint(2)
          k = np.random.randint(4)
          l = np.random.randint(2)
          j=["G=!!","Parents","Dream","Friends"]
          dist=[]

          for i in range (4):
              x=mate()[m][n]
              y=mate()[k][l]
              create_circle(x,y, 35, myCanvas) # radius

              myCanvas.create_text(x, y,text=j[i],font=("arial",12,'bold'),fill="yellow")
              dist.append([])
              dist[i].append(x)
              dist[i].append(y)
          dist_1 = np.array(dist)
          dist_2=dist_1.reshape(1,-1)
          dist_3=dist_2.tolist() # convert array to list, create line only work in list
          print("ok", dist)
          myCanvas.create_line(dist_3)

          angle=[]
          for i in range(len(dist)-1):
              a=(dist[i][1]-dist[i+1][1])/(dist[i][0]-dist[i+1][0])
              angle.append(abs(a))

              if i == 1:
                  a = (dist[i][1] - dist[i+2][1]) / (dist[i][0] - dist[i+2][0])
                  angle.append(abs(a))

              if i==2:
                  a = (dist[i-2][1] - dist[i][1]) / (dist[i-2][0] - dist[i][0])
                  angle.append(abs(a))

              if i+1==3:
                  a = (dist[i-3][1] - dist[i][1]) / (dist[i-3][0] - dist[i][0])
                  angle.append(abs(a))

          print(angle)


          # print(dist_1)
          # print(dist_2)
          # print(dist_3)

          dist2=np.delete(dist,0,0)
          # print(dist[0])
          # print(dist2)
          dist3 = (abs(dist[0] - dist2)) ** 2
          dist3 = np.sum(dist3, axis=1)
          dist3 = np.sqrt(dist3)
          k=np.sum(dist3)
          myCanvas.create_text(700, 25, text=round(k), font=("arial", 16, 'bold'), fill="yellow", tags="xyz")

          myCanvas.pack()
          root.update()

          time.sleep(1) #root.after(10)
          myCanvas.delete("all") # every 4 shape will appear and then delete

          if (angle[0]==angle[1]==angle[2]==angle[3]==angle[4]==angle[5]):
                      break

      return root.mainloop()

print(ok())

print(k)