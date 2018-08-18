#!/usr/bin/env python3
# สรายุทธ   สมภักดี
# 610510672
# Lab 02
# Problem 3
# 204111 Sec 001

print('First Equation')
m1 = float(input('Input m1: '))
b1 = float(input('Input b1: '))
print('Second Equation')
m2 = float(input('Input m2: '))
b2 = float(input('Input b2: '))

x = ( b2 - b1 ) / ( m1 - m2 )
y = ( m1 * x ) + b1
#print(x)
#print(y)

print('The point of intersection is at x = %.2f'%x, 'and y = %.2f'%y)
