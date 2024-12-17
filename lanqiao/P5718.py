n = int(input())

lst=list(map(int,input().split()))

min = lst[0]
for i in lst:
    if min > i:
        min = i

print(min)