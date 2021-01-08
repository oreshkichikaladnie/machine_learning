import matplotlib.pyplot as plt
import numpy as np
import math

# Датасет
xx = []
yy = []
data = open('Salary_Data.csv')
for line in data:
    if float(line.split(',', maxsplit=-1)[0]) not in xx:
        xx.append(float(line.split(',', maxsplit=-1)[0]))
        yy.append(float(line.split(',', maxsplit=-1)[1]))
xx = np.array(xx)
xx = np.reshape(xx, (1, -1))
yy = np.array(yy)
yy = np.reshape(yy, (1, -1))
plt.scatter(xx, yy)
ma = np.amax(xx)
mi = np.amin(xx)


xlearn = np.split(np.reshape(xx, -1),[10,20])[0]
ylearn = np.split(np.reshape(yy, -1),[10,20])[0]
reg = np.polyfit(xlearn, np.log(ylearn), 1)
xlearn = np.arange(int(mi), int(ma), 1)
ylearn = np.zeros(int(ma) - int(mi))
for i in range(len(xlearn)):
    ylearn[i] = math.exp(reg[1]) * math.exp(reg[0] * xlearn[i])
plt.plot(xlearn, ylearn, color="pink")

xtest = np.split(np.reshape(xx, -1),[10,20])[1]
ytest = np.split(np.reshape(yy, -1),[10,20])[1]

plt.plot(xtest, ytest,  color='black')
plt.show()