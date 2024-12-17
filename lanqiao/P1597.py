# 把表达式拆成一个一个的，放入expression里
expression = input().split(";")
expression.pop()
# print(f"expression是：",*expression)

result = [0, 0, 0]

# print(f"判断expression中元素最后一位是否为int类型：{expression[0][-1].isnumeric()}")
for exp in expression:
    
    #当前的是a, b还是c，a为 b为1 c为2
    weizhi = ord(exp[0])-97
    if exp[-1].isnumeric():
        result[weizhi] = exp[-1]
    else:
        result[weizhi]=result[ord(exp[-1])-97]
            

print(*result)