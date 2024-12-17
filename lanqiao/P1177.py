N = (input())
# lst = list(map(int,input().split()))
lst = [[int(i)] for i in input().split()]
# print(ldt)
# print()
# tmp = 0
# for i in range(N):
#     # j = i
#     for j in range(i+1,N):
#         if lst[i]>=lst[j]:
#             tmp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = tmp
lst.sort()     
print(*lst,sep='\n')
print(lst)
