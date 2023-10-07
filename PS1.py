import numpy as np

n = 8

def find_inv(n:int = 0)-> None:
    A = np.array([[2-abs((i-j)) if 2-abs((i-j)) > 0 else 0 for i in range(n)] for j in range(n)])
    b = np.array([[1] for i in range(n)])
    print('A: ', A)
    #print('b: ', b)
    x = np.linalg.inv(A)@b
    print(n, ': ', x)

"""for n in range(1,6):
    find_inv(2*n)"""

find_inv(20)

"""
NOTE: for even values of n the x is of the form

[[a][b][c]...[c][b][a]]
i.e. x is symmetric.

[[(0.5n + r-1)/(n+1)],[(1+r-1)/(n+1)],...,[],[]]
"""
#sol = np.array([[ mod(j + n, 0.5n)/(n+1) for i in range(n)]] for j in range(n))
#print(np.array([[min(abs(j), abs(n-j-1))] for j in range(n)]))
