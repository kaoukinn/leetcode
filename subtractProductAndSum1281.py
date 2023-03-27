n = 4421

res = 1
num = 0
for i in str(n):
    num += int(i)

for i in str(n):
    res *= int(i)
print(res - num)