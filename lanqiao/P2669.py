m =int(input())

"""
1.求出金币发放的轮次
2.用等差数列公式求和公式求完整周期的时间wanzheng
3.求剩下不完整的方法时间r

"""

k=1
while int(k + k*(k - 1) / 2) <= m:
    k += 1

k = k - 1

"""
求出金币发放的轮次
用等差数列公式求和公式求

"""

# 在完整周期的时间为wanzheng，发放的金币pre_money
wanzheng = int(k + k*(k - 1) // 2)
pre_money = int(k*(k + 1)*(2*k + 1) //6)

# 求减去完整的金币发放轮次，周期后剩下的不完整的发放日期r
r = m - wanzheng

# 当前发放的金币数目为k
k = k + 1
all_money = pre_money + k * r
print(all_money)

# print("{:0.0f}".format(k*1 + k*(k-1)/2*1))