'''
python2中整数有整型（int）和长整型（long）之分
超过一定大小的数字可以在后面加L标识为长整型
python3不需要考虑溢出
'''

'''
python3不需要考虑编码问题，可以在代码中任意出现非ascii字符
用中文做变量名或者函数名也行
'''
i = 123456
bin(i) # 二进制 0b1010
oct(i) # 八进制 0o6321
hex(i) # 十六进制 0xabcd
str = '0b1101'
base = 2 # python支持2-36进制
int(str,base) #将字符串转换成整数
'''
base不写默认十进制
int('0b1110')报错，进制不匹配
'''

'''
in python3 ,it takes 64bit to  save a float number.
The accuracy of float number can reach 17 decimal places
after Floating-point.
'''
a = 3+5j
c = complex(3,5) # 虚数

from fractions import Fraction
Fraction(4,5)
# 分数,并且能够自动约分,分数比float精确,但一般情况下除法够用
print(a==c)
'''
python 中可以用3+5j的形式来表示虚数
float('inf')是无穷大
float('-inf')是负无穷大
float('nan') not a number
'''
print(3/2) # 1.5
print(3//2) # 1
# python3 默认的除法是带小数的,与C语言不同,需要除法取整使用//
'''
算数运算符: + - * / %(取余) //(取整除法) **(指数运算)
比较运算符: == != > < >= <=
    python2还有<>表示不等于,python3取消了这种写法
赋值运算符: = += -= /= %= //= **=
    e.g. '1+=2' equals to '1 = 1+2'
    e.g. '1 **= 2' equals to '1 = 1**2'
位运算符: &(按位与) |(按位或) ^(按位异或) ~(按位取反) <<(左移) >>(右移)
逻辑运算符: and or not
成员运算符: in , not in
    e.g. if a in b 即 是否a在b中
    e.g. for a in b 即 对所有b的元素一一列举
身份运算符:is(同一个对象),is not(不是同一个对象)
'''
i = [1,2,3,4,5,6] # 队列
s = [number for number in i if 1<number<5]
# 队列的子序列可以使用类似 s = { x | 1<x<5.x∈i}的语法
print(s)

# 但是集合操作会更便捷,可以直接使用交集并集
j = [1,1,2,2,3,3,4,4]
j = set(j) # 转化为集合,去掉所有重复元素
k = {2,3,4,5}

print(j & k) # 交集
print(j - k) # 去集,差
print(j ^ k) # 对称差
print(j | k) # 并集
