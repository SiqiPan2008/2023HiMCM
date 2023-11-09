import numpy as np

def AHP(matrix):
    print('----------Begin CR-------------')
    eigvals = np.linalg.eigvals(matrix)
    max_eigval = max(eigvals)
    print('max_eigval = ', max_eigval)
    n = len(matrix[0])
    print('n = ', n)
    CI = (max_eigval - n) / (n -1)
    print('CI = ', CI)
    RI = 1.49
    print('RI = ', RI)
    CR = CI/RI
    print('CR = ', CR)
    print('----------End CR-------------')
    k = matrix/matrix.sum(0)
    w = k.sum(1)
    print('weight = ', w)
    return w

print('cal CR for matrix global')
matrixG = np.array([[1, 1/3., 1/7., 1/3., 1, 1/7., 1/4., 1/7., 1/5., 1/9., 1/5., 1/3., 1/4., 1/4.],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2.],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3, 5, 4, 4],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2.],
                   [1, 1/3., 1/7., 1/3., 1, 1/7., 1/4., 1/7., 1/5., 1/9., 1/5., 1/3., 1/4., 1/4.],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3., 5, 4, 4],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3., 5, 4, 4],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2],
                   [9, 7, 3, 7, 7, 3, 4, 3, 5, 1, 5, 7, 4, 4],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2.],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1]])
AHP(matrixG)


print('cal CR for matrix local')
matrixL = np.array([[1, 1/3., 1/7., 1/3., 1, 1/7., 1/4., 1/7., 1/5., 1/9., 1/5., 1/3., 1/4., 1/4., 1/5., 1/5., 1/5., 1/3.],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2., 1/3., 1/3., 1/3., 1],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3, 5, 4, 4, 3, 3, 3, 5],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2., 1/3., 1/3., 1/3., 1],
                   [1, 1/3., 1/7., 1/3., 1, 1/7., 1/4., 1/7., 1/5., 1/9., 1/5., 1/3., 1/4., 1/4., 1/5., 1/5., 1/5., 1/3.],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3., 5, 4, 4, 3, 3, 3, 5],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1, 1/2., 1/2., 1/2., 2],
                   [7, 5, 1, 5, 7, 1, 4, 1, 3, 1/3., 3., 5, 4, 4, 3, 3, 3, 5],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2, 1, 1, 1, 3],
                   [9, 7, 3, 7, 7, 3, 4, 3, 5, 1, 5, 7, 4, 4, 5, 5, 5, 7],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2, 1, 1, 1, 3],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2., 1/3., 1/3., 1/3., 1],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1, 1/2., 1/2., 1/2., 2],
                   [4, 2, 1/4., 2, 4, 1/4., 1, 1/4., 1/2., 1/4., 1/2., 2, 1, 1, 1/2., 1/2., 1/2., 2],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2, 1, 1, 1, 3],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2, 1, 1, 1, 3],
                   [5, 3, 1/3., 3, 5, 1/3., 2, 1/3., 1, 1/5., 1, 3, 2, 2, 1, 1, 1, 3],
                   [3, 1, 1/5., 1, 3, 1/5., 1/2., 1/5., 1/3., 1/7., 1/3., 1, 1/2., 1/2., 1/3., 1/3., 1/3., 1]])
AHP(matrixL)
