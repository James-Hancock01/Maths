import numpy as np
class Matrix:
    def __init__(self, dimensions, values = None):
        self.shape = dimensions  #(n,m)
        if self.shape == np.shape(values): self.values = [val for val in values]
        elif values == None: self.values = [[0]*self.shape[1] for i in range(0, self.shape[0])]
        else: raise ValueError('shape of supplied values does not match dimensions given')
        self.determinant = 1

    def print(self):
        for row in self.values:
            print(row)

    def scalarMult(self, scalar = 1):
        for row in range(self.shape[0]):
            for col in range(self.shape[1]):
                self.values[row][col] *= scalar

    def id(self, n:int):
        return [[1 if i == j else 0 for i in range(n)] for j in range(n)]

    #def REF(self):
        #if self.values == [[0]*self.shape[1] for i in range(0, self.shape[0])]: return self.values
        #for i in

mat = Matrix((2,2), [[0, 0], [0,0]])#Matrix((2,2), [[1,2], [3,4]])
#mat.scalarMult(2)
print(mat.id(2))
