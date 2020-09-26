L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
# 切片
L = ['A', 'B', 'C', 'D', 'E']

print(L[0:3])
L = list(range(100))
print(L)
print(L[:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[:10:2])  # [0, 2, 4, 6, 8]
# 迭代
