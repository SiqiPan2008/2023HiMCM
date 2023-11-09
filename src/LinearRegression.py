from numpy import *
import csv


def leastSquareSolve(dataName, residualName):
    dataFile = open(dataName, encoding = "UTF-8")
    dataReader = csv.reader(dataFile)
    datas = array(list(dataReader), dtype = float)
    matrixShape = datas.shape
    AArray, bArray = hsplit(datas, [matrixShape[1] - 1])
    A = mat(AArray)
    b = mat(bArray)
    ATA = matmul(A.T, A)
    ATb = matmul(A.T, b)
    x = linalg.solve(ATA, ATb)
    for i in range(matrixShape[1] - 1):
        x[i, 0] = int(x[i, 0] * 1000) / 1000
    print(x)
    print("\n")

    residualCount = [0, 0, 0, 0] # r>=10, 5<=r<10, 1<=r<5, 0<=r<1
    residualFile = open(residualName, "w", encoding='UTF-8')
    residualVector = b - matmul(A, x)

    print(str(matrixShape[0]))
    for i in range(4):
        print(str(residualCount[i]) + ", " + str(residualCount[i] * 100 / matrixShape[0]), "%")
    residualFile.close()

leastSquareSolve("Output/fitting.csv", "residual.csv")