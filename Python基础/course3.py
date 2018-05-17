
from fractions import Fraction
# 导入模块/包/函数

a = 10
b = 3.14
c = 5+3j
d = Fraction(4,5)
'''
变量类型向容量大的类型变化
整数<分数<浮点数<虚数
'''

import math
abs(-10)
math.fabs(-10)
round(2.5)
round(3.5)
math.ceil(1.5)
math.ceil(-1.5)
math.floor(1.5)
'''
四舍五入向遇见5向偶数方向靠拢
ceil()向上取整,floor向下取整
'''

import random
random.random() # 0-1之间随机小数
c = (1,2) # 二元组
random.choice((1,2,3,4,5))
# 随机取多元组中的一个数
a = [1,2,3,4,5]
random.choice([1,2,3,4,5])
random.sample(a,2)
# 随机取队列中的一个数/N个数
'''
random.choice({1,2,3,4,5}) is error
随机数一个列表中的元素是通过随机一个下标(index)完成的,set没有下标
'''
a = [1,2,3,4,5]
random.shuffle(a) # 随机打乱
random.getrandbits(10) # 取N位二进制数
random.randint(1,99) # 随机一个范围的小数

math.log(2) # 默认e为底数
math.log(4,2) # 以2为底数
math.log10(5) # 以10为底数
math.sqrt(9) # 开平方
max(1,2,3,4,5)
max(a)
min(a) # 最大最小值

math.modf(2.5) # (0.5,2.0)分离小数个整数部分
'''
其他格式化数字/取整数字/舍入数字可以参考百度,使用不多此处不多赘言

需要极高精度的时候可以使用 Decimal 模块
'''
from decimal import Decimal
a = Decimal('2.1')
b = Decimal('4.2')
print(a+b) # 6.3
a = 2.1
b = 4.2
print(a+b) # 6.300000000000001 出现浮点数误差
