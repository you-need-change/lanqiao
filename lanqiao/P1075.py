n = int(input())
a = 0
for i in range(2,int(n**0.5) + 1):

    if n % i ==0:
        a = i
print(int(max(a, n/a)))