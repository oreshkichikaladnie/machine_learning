import numpy as np

class grib:
    def __init__(self,id,pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,cl):
        self.id = id
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr3 = pr3
        self.pr4 = pr4
        self.pr5 = pr5
        self.pr6 = pr6
        self.pr7 = pr7
        self.pr8 = pr8
        self.cl = cl


# dataset
t = 0
mushroom = []
data = open("agaricus-lepiota.data")
for line in data:
    t += 1
    mushroom.append(grib(t,line[0],line[2],line[4],line[6],line[8],line[10],line[12],line[14],"None"))
mushroom = np.array(mushroom)

# classes
classes=['pxsntpfc','efygtnfc','efyetnfc','pxfgfffc','efyntnfc','pxfgfffc','effetnfc',]

# classification
for gri in (mushroom):
    for i in range(len(classes)):
        if (gri.pr1 == classes[i][0] and gri.pr2 == classes[i][1] and gri.pr3 == classes[i][2] and gri.pr4 == classes[i][3]
                and gri.pr5 == classes[i][4] and gri.pr6 == classes[i][5] and gri.pr7 == classes[i][6] and gri.pr8 == classes[i][7]):
            gri.cl=i
for grib in mushroom:
    print(grib.cl)
