import pandas as pd
import numpy as np
import sys


print sys.argv[0]
filename = sys.argv[1]
k = sys.argv[2]
print k
data = pd.read_csv(filename)
df = pd.DataFrame()
df["x"] = data["x"]
df["y"] = data["y"]
df["z"] = data["z"]
dfmatrix = pd.DataFrame()
dfmatrix = df.as_matrix()
dfmatrix


def euclideanDist(x):
    lst = []
    dictkey = {}

    for i in range(len(x)-1):
        dist = 0.0
        d = np.power((x[i][0]-x[0][0]), 2)+np.power((x[i][1] -
                                                     x[0][1]), 2)+np.power((x[i][2]-x[0][2]), 2)
        dist = np.sqrt(d)
        # print dist, x[i][0], x[i][1], x[i][2]
        lst.append([dist, x[i][0], x[i][1], x[i][2]])
        dictkey[dist] = [x[i][0], x[i][1], x[i][2]]
    newDF = pd.DataFrame(lst, columns=['Distance', 'x', 'y', 'z'])

    for key in sorted(dictkey)[0:int(k)]:
        print dictkey[key]

    return
euclideanDist(dfmatrix)
