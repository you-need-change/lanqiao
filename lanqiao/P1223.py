n = int(input())
lst = list(map(int,input().split()))
lst2 = [] + lst
lst3 = [0] + lst
lst2.sort()
lst3.sort()
cnt_wai = 0
cnt_found = 0
sum = 0
suoyou_inx = []
for j in range(0,n):
    for i in range(0,n):
        if lst2[j] == lst[i] and i+1 not in suoyou_inx:
                suoyou_inx.append(i+1)
                cnt_found += 1
                break
print(*suoyou_inx)

for i in range(0,n-1):
    sum += lst2[i]*(n-i-1)

avg = sum / n
print("%.2f"%avg)