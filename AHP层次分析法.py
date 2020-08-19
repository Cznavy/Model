import numpy as np


def ahp_sort(X):  #归一化，获得特征值和特征向量
    col_sum1 = X.sum(axis=0)
    col_sum2 = X/col_sum1
    row_sum1 = col_sum2.sum(axis=1)
    row_sum2 = row_sum1.sum(axis=0)
    w = row_sum1/row_sum2
    Xw = X@w
    lamida = (Xw/w).sum(axis=0)/(A.shape[1])
    return lamida, w


def consistency_check(X):  #一致性检验
    n = X.shape[1]
    lamida = ahp_sort(X)[0]
    if n == 1 or n == 2:
        RI = 0
    elif n == 3:
        RI = 0.58
    elif n == 4:
        RI = 0.9
    elif n == 5:
        RI = 1.12
    elif n == 6:
        RI = 1.24
    elif n ==7:
        RI = 1.32
    elif n == 8:
        RI = 1.41
    elif n ==9:
        RI =1.45
    elif n==10:
        RI = 1.49
    elif n==11:
        RI = 1.51
    CI = (lamida-n)/(n-1)
    CR = CI/RI
    if CR>0.1:
        print('不一致程度在容许范围之外！')
    else:
        print('一致性检验通过！CR为%s'%CR)
    return CR


class Ahp:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def ahp_sortA(self):
        ahp_sort(self.A)

    def ahp_sortB(self):
        for i in self.B:
            ahp_sort(i)

    def consistency_checkA(self):
        consistency_check(self.A)

    def consistency_checkB(self):
        for i in self.B:
            consistency_check(i)

    def result(self):
        BI = []
        for i in self.B:
            Bi = ahp_sort(i)
            BI.append(Bi[1])
        W = np.array(BI).T
        result = W@ahp_sort(A)[1]
        print(result)

        
'''例1'''
# A = np.array([[1,8,5,3],[1/8,1,1/2,1/6],[1/5,2,1,1/3],[1/3,6,3,1]])
# B1 = np.array([[1,1/3,1/9],[3,1,1/8],[9,8,1]])
# B2 = np.array([[1,3,9],[1/3,1,8],[1/9,1/8,1]])
# B3 = np.array([[1,2,9],[1/2,1,7],[1/9,1/7,1]])
# B4 = np.array([[1,1/3,1/9],[3,1,1/7],[9,7,1]])
# B = np.array([B1,B2,B3,B4])
'''例1'''

'''例2'''
A = np.array([[1,1/2,4,3,3],[2,1,7,5,5],[1/4,1/7,1,1/2,1/3],[1/3,1/5,2,1,1],[1/3,1/5,2,1,1]])
B1= np.array([[1,2,5],[1/2,1,2],[1/5,1/2,1]])
B2 = np.array([[1,1/3,1/8],[3,1,1/3],[8,3,1]])
B3 = np.array([[1,1,3],[1,1,3],[1/3,1/3,1]])
B4 = np.array([[1,3,4],[1/3,1,1],[1/4,1,1]])
B5 = np.array([[1,1,1/4],[1,1,1/4],[4,4,1]])
B = np.array([B1,B2,B3,B4,B5])
'''例2'''

X = Ahp(A, B)
# X.ahp_sortB()
# X.consistency_checkB()
X.result()
