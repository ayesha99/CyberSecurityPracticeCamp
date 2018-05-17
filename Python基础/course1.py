
'''
add the line to your python source

#! add python path in this

e.g.:

#!/usr/bin/env python

make the script to a executable file

~:chmod +x *.py
'''

if True:
    print('the first True')
    if True:
        print("the second True")
else:
    print('the first else')
"""
python中单引号与双引号没有区别，用连续三个引号可以进行段落注释
"""
# 单行注释
'''
注释
'''
a = "hello 'test'" # 不需要转义
print(a)

a = """hello
    world"""
print(a)
# 用三引号进行段落引用
