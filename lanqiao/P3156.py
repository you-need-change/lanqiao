n, m = map(int, input().split())

student_ids = list(map(int, input().split()))

# queries = list(map(int, input().split()))
 
# for q in queries:
#     print(student_ids[q - 1],end=" ")
for i in range(m):
    n = input()
    print(student_ids[n - 1])