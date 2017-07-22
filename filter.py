import numpy as np
import math
'''
101 = Shapes aren't equal
'''
class filter(DataSet):
    'oganizes all filers'

    def __init__(self,filter,confi,used): #filter [] acutual filter, confi [] = confidence value of each filter element
        self.filter = filter
        self.confi  = confi
        self.used   = used
    def createnew(self):
        if DataSet.score

    def learn(self):


class DataSet:
    'is a data pair'

    def __init__(self,x,z,y,score,truth): #x = data set, z = after filter, y = filter, score = what the model thought truth = what it actually is
        self.x = x
        self.z = z
        self.y = y

    def score_I(self):  # only for (x,2) arrays
        length = DataSet.z.shape[0]
        height = DataSet.z.shape[1]
        new = np.zeros((length))
        for a in range(length):
            new[a] = z[a][0] * z[a][1]
        print(new)
        print(sum(new))
        DataSet.y = new

    def filterr(self):
        length = DataSet.x.shape[0]
        height = DataSet.x.shape[1]
        if length != DataSet.y.shape[0]:
            return 101
        DataSet.z = np.zeros((length, height))
        for a in range(length):
            for b in range(height):
                x_value = x[a][b]
                y_value = y[a][b]
                # print('x',x_value)
                # print('y',y_value)
                if b == 1:
                    z[a][
                        b] = x_value * y_value  # usually the second value is confidence so the two confidences added/multiplied/squared
                    continue
                z[a][b] = abs(x_value - y_value)


def mod_filter(X,y,filterr):
    length = x.shape[0]
    height = x.shape[1]



x = np.array([[1,3],[4,3],[5,1]])
y = np.array([[1,4],[3,1],[3,9]])
score_I(filterr(x,y))

