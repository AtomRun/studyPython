# -*- coding:utf-8 -*-

import math

def test (x):
    return x

def testFunctionAndValidType (x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad type');

# 这个函数返回了一个元组，包含了两个参数
def testFunctionRetunMultiValue(x):
    return x, x+1;

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('%s is bad type '%a)
    if not isinstance(b,(int,float)):
        raise TypeError('%s is bad type '%b)
    if not isinstance(c,(int,float)):
        raise TypeError('%s is bad type '%c)
    n = math.sqrt(b**2-4*a*c)
    if n < 0:
        print("无解")
    else:
        x = (-b+n)/(2*a)
        y = (-b-n)/(2*a)
        return x,y

print(test(2))

# print(testFunctionAndValidType('A'))

print(testFunctionRetunMultiValue(3))

print('quadratic(2,3,1) =',quadratic(2,3,1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))