Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:/Users/admin/Desktop/python training/day 10.py ==========
5000

=========== RESTART: C:/Users/admin/Desktop/python training/day 10.py ==========

=========== RESTART: C:/Users/admin/Desktop/python training/day 10.py ==========
5000

=========== RESTART: C:/Users/admin/Desktop/python training/day 10.py ==========
15



lambda a:
    
SyntaxError: invalid syntax
lambda a: a*3
<function <lambda> at 0x000002630A43C8B0>
c=lambda a: a*3
c
<function <lambda> at 0x000002630A43C9D0>
list(c)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(c)
TypeError: 'function' object is not iterable
c(5)
15
c(10)
30
c(1919)
5757

b=lambda a: a**2
b(10101)
102030201
b(2)
4

b=lambda a,y: a+y
b(5,6)
11

b=lambda a: a%2=0 print('EVEN')
SyntaxError: cannot assign to lambda
b=lambda a: a%2=0
SyntaxError: cannot assign to lambda

x=lambda a: a%2=0 print('EVEN')
SyntaxError: cannot assign to lambda
x = lambda a: a%2=0 print('EVEN')
SyntaxError: cannot assign to lambda
t= lambda a: a%2==0 : print('EVEN')
SyntaxError: invalid syntax
t= lambda a: 'EVEN' if a%2==0 else 'ODD'
t(7)
'ODD'

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
EVEN

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
<map object at 0x0000015241246980>

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[24, 16, 20, 28]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[8916100448256, 16777216, 10000000000, 11112006825558016]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
(8916100448256, 16777216, 10000000000, 11112006825558016)

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[45, 14, 15]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[True, False, False, True]
()

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[True, False, False, True, True]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[225, 40, 50, 70, 75]
[45, 8, 10, 14, 15]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[225, 40, 50, 70, 75]
[45, 8, 10, 14, 15]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[225, 40, 50, 70, 75]
[45]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[True, True, True, True, True]
[45]

=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
[True, False, False, False, False]
[45]



import math
math.pi
3.141592653589793
math.pow(2,3)
8.0
import numpy as np
np,power(2,3)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    np,power(2,3)
NameError: name 'power' is not defined
np.power(2,3)
8
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
m.factorial(10)
3628800
m.pow(4,5)
1024.0
from math import sqrt
sqrt(81)
9.0
sqrt(69)
8.306623862918075
sqrt(69)
8.306623862918075
from math import pi
pi
3.141592653589793
from math import pi,sqrt,pow
pow(6,7)
279936.0




def abc(x,y)
SyntaxError: expected ':'
def abc(x,y):
    return x*y,x+y,x**y

a,b,c=abc(4,5)

a
20
b
9

c
1024


from abc import a
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    from abc import a
ImportError: cannot import name 'a' from 'abc' (C:\Users\admin\AppData\Local\Programs\Python\Python310\lib\abc.py)
from abc import x
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    from abc import x
ImportError: cannot import name 'x' from 'abc' (C:\Users\admin\AppData\Local\Programs\Python\Python310\lib\abc.py)

from abc import b
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    from abc import b
ImportError: cannot import name 'b' from 'abc' (C:\Users\admin\AppData\Local\Programs\Python\Python310\lib\abc.py)
import abc
abc.abc(2,3)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    abc.abc(2,3)
AttributeError: module 'abc' has no attribute 'abc'. Did you mean: 'ABC'?
>>> abc.a
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    abc.a
AttributeError: module 'abc' has no attribute 'a'
>>> import abc
>>>  def abc(x,y):
...      return a=x*y,b=x+y,c=x**y
...     
SyntaxError: unexpected indent
>>> 
>>> 
>>> def abc(x,y):
...     return a=x*y,b=x+y,c=x**y
SyntaxError: invalid syntax
>>> 
>>> 
=============================== RESTART: C:/Users/admin/Desktop/python training/MODULE CREATING.py ==============================
>>> import MODULE CREATING
SyntaxError: invalid syntax
>>> import mymod
>>> mymod.abc
<function abc at 0x0000019F49E0C940>
>>> print(mymod.abc)
<function abc at 0x0000019F49E0C940>
>>> print(list(mymod.abc))
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(list(mymod.abc))
TypeError: 'function' object is not iterable
>>> 
=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
<function abc at 0x000001C262DAC8B0>
>>> 
=================================== RESTART: C:/Users/admin/Desktop/python training/day 10.py ===================================
HII MASTER
