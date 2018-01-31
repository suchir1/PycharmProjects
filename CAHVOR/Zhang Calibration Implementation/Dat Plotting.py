import numpy as np
import pylab
with open("/home/cheesecake/PycharmProjects/CAHVOR/Zhang Calibration Implementation/data/corners_1.dat") as f:
    data = f.read()

data = data.strip()
data = data.replace('\n', " ")
data = data.split()
x_list = []
y_list = []
print(data)
for i, val in enumerate(data):
    print(val)
    val = float(val)
    if(i%2==0):
        x_list.append(val)
    else:
        y_list.append(val)




pylab.plot(x_list,y_list)

pylab.legend()
pylab.title("Title of Plot")
pylab.xlabel("X Axis Label")
pylab.ylabel("Y Axis Label")

pylab.show()