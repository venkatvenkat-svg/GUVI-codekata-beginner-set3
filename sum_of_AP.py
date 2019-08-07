n,a,d=map(int,input().split())
sum = 0
value = a
for i in range(n):
    sum = sum + value
    value = value + d
print(sum)
