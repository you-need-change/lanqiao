"""
a, b=2,1
print(f"a:{a} b:{b}")

x = lambda a, b:a ^b
# print(f"lambda形式的a^b:{x(a,b)}")
# print(f"实际的a^b:{a^b}")
# print(x(a, b) ^ a)

print("*"*12)

a =a^b
b =a^b
a =a^b

print(f"a:{a} b:{b}")
"""

def swap(a,b):
    a =a^b
    b =a^b
    a =a^b
    
    return a, b

x, y, z=map(int, input().split())

if x > y:
    x, y = swap(x,y)

if x > z:
    x, z = swap(x,z)

if y > z:
    y, z = swap(y,z)

print(x,y,z)