import math
import matplotlib.pyplot as plt


def isPrimeNumber(num):
    i = 2
    x = math.sqrt(num)
    while i < x:
        if num % i == 0:
            return False
        i += 1
    return True


n = 5
arr = []
temp = 0
const = 309090
matrix = [[0 for i in range(4)] for i in range(const)]
while n < 1001:
    for j in range(3, int(n/3)):
        for k in range(j,int(n/2)):
            if isPrimeNumber(j) and isPrimeNumber(k) and isPrimeNumber(n-j-k):
                # print('%s = %s + %s + %s' % (n, j, k, n-j-k))
                # print(temp)
                matrix[temp][0] = n
                matrix[temp][1] = j
                matrix[temp][2] = k
                matrix[temp][3] = n-j-k
                temp = temp + 1
                #break   # 找到符合的组合后，便结束内循环
    n += 2
print(temp)
# print(matrix)
cout = 0
matrix2 = [[0 for i in range(2)] for i in range(const)]
for i in range(const):
    if matrix[i][0] == temp:
        cout = cout + 1
    else:
        matrix2[i][0] = matrix[i][0]
        matrix2[i][1] = cout + 1
        cout = 0
    temp = matrix[i][0]
print(matrix2)
matrix3 = [[0 for i in range(2)] for i in range(497)]
j = 0
for i in range(const):
    if matrix2[i][0] != 0:
        matrix3[j][0] = matrix2[i][0]
        matrix3[j][1] = matrix2[i][1]
        j = j + 1
print(matrix3)
x = []
y = []
for i in range(497):
    x.append(matrix3[i][0])
    y.append(matrix3[i][1])
print(x)
print(y)
plt.plot(x, y)
plt.show()

