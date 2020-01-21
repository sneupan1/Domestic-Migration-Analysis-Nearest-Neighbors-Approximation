
import matplotlib.pyplot as mplot
import numpy as np
import math
xval = []
yval = []
xpt = []
ypt = []
val = []
distancelist =[]
xplot = []
yplot = []
valplot = []

while (True):  
    k = input("Enter the value of k: ")
    try:
        k = int(k)
        break
    except:
        print("Please enter an integer greater than 0")
        continue
    
if (k > 0):
    file = open("us_outline.csv", "r")
    outline = file.read()
    outline = outline.split("\n")
    
    for x in range(len(outline)):
        outline[x] = outline[x].split(",")
        
        outline[x][0] = np.float64(outline[x][0])
        outline[x][1] = np.float64(outline[x][1])
        
        xval.append(outline[x][0])
        yval.append(outline[x][1])
    
    file2 = open("data.csv", "r")
    data = file2.read()
    data = data.split("\n")
    
    for x in range(len(data)):
        data[x] = data[x].split(",")
        
        data[x][0] = np.float64(data[x][0])
        data[x][1] = np.float64(data[x][1])
        data[x][2] = np.float64(data[x][2])
        
        xpt.append(data[x][0])
        ypt.append(data[x][1])
        val.append(data[x][2])
    
    for x in range(0, 195):
        for y in range(0,121):
            distancelist = []
            for n in range(len(xpt)):
                distance = math.pow(ypt[n]-y,2)+math.pow(xpt[n]-x,2)
                distancelist.append([distance, val[n]])
            distancelist = sorted(distancelist, key = lambda i:i[0])
            distancelist = distancelist[0:k]
            average = 0
            for i in range(len(distancelist)):
                average = average + distancelist[i][1]
            average = average / k
            xplot.append(x)
            yplot.append(y)
            valplot.append(average)
            
    mplot.plot(xval,yval, color = "black" , linewidth = 2)
    mplot.scatter(xplot, yplot, c = valplot , cmap = "viridis")
    mplot.show()
else:
    print("The value of K should be greater than 0")
    
