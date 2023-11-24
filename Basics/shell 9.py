Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def singhal()
SyntaxError: expected ':'
def singhal():
    a='aditya'
    b='singal'
    c=a+b
    print(c)

    
singhal()
adityasingal
def singhal():
    a='aditya  '
    b='singal'
    c=a+b
    print(c)

    
singhal()
aditya  singal
def singhal():
    a='aditya  '
    b='singhal'
    c=a+b
    print(c)

    
singhal()
aditya  singhal






print(' HELLO ')
 HELLO 

a=print(' HELLO ')
 HELLO 
A
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a

print(a)
None
a='hii'
a
'hii'
def first('HELLO'):
    
SyntaxError: invalid syntax
def first(HELLO):
    print('HII')

    
first()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    first()
TypeError: first() missing 1 required positional argument: 'HELLO'
def first():
    print('HII')

    
first()
HII

def second()
SyntaxError: expected ':'
def second():
    return 'hello'

second()
'hello'
a=second()
a
'hello'

 

def third(x):
    print(x*2)

    
third()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
third(32)
64
a=third(34)
68
a


def four(x):
    return x**2

four(45)
2025
a=four(x)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a=four(x)
NameError: name 'x' is not defined
a=four(5)
a
25
def five(x,y)
SyntaxError: expected ':'
def five(x,y):
    return x**6,y%2

five
<function five at 0x000001D108CED120>
five(8,9)
(262144, 1)
def five(x,y):
    return x*y

five(5,6)
30
def six(x):
    return x*y,x**y,x+y

six(4)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    six(4)
  File "<pyshell#77>", line 2, in six
    return x*y,x**y,x+y
NameError: name 'y' is not defined
>>> def six(x,y):
...     return x*y,x**y,x+y
... 
>>> six(4,8)
(32, 65536, 12)
>>> def six(x,y):
...     return x*y,x**y,x+y
... 
>>> a=six(5,4)[0]
>>> b=six(5,4)[1]
>>> c=six(5,4)[2]
>>> 
>>> a
20
>>> b
625
>>> c
9
>>> six(5,4)
(20, 625, 9)
>>> a
20
>>> b
625
>>> c
9
