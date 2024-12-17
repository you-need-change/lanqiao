m, t, s = map(int, input().split())

#已经吃了的苹果数量
if t == 0:
    print('0')

else:
    used = s // t

    remain = (m - used) if used * t == s else (m - used - 1)

    remain = remain if remain > 0 else 0

    # 剩下的苹果数量
    print(remain)