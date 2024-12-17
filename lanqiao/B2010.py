# bc_num, c_num分别为被除数和除数
bc_str, c_str  = input().split()
bc_num, c_num = int(bc_str), int(c_str)

# shang_num, r分别为商和余数
shang_num = bc_num // c_num

r = bc_num % c_num

print(f'{shang_num} {r}')