Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[12,56,41,23,100,20]
for i in range(3):
    print(a[i*3])

    
12
23
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    print(a[i*3])
IndexError: list index out of range
for i in range(3):
    print(a[i]*3)

    
36
168
123
for i in range(3):
    print(a[i]*3)
print(a+a[i]*3)
SyntaxError: invalid syntax

for i in range(3):
    print(a[i]*3)
print([a]+[a[i]*3])
SyntaxError: invalid syntax

for i in range(3):
    print(a[i]*3)
print([a]+[a[i]*3])
SyntaxError: invalid syntax

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
36
168
123
[23, 100]
[23, 100]
: invalid syntax

for i in range(3):
    print(a[i]*3)
print([a]+[a[i]*3])
SyntaxError: invalid syntax

for i in range(3):
    print(a[i]*3)
print([a]+[a[i]*3])
SyntaxError: invalid syntax

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
36
168
123
SyntaxError: invalid decimal literal










============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
{'name': ['aryan', 'balkrishna', 'ayush'], 'age': [18, 20, 19]}

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
{'name': ['aryan', 'balkrishna', 'ayush'], 'age': [18, 20, 19]}

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
{'name': ['aryan', 'balkrishna', 'ayush'], 'age': [18, 20, 19]}
<class 'dict'>

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 20, in <module>
    d1=dic(zip(a,b))
NameError: name 'dic' is not defined. Did you mean: 'dir'?

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
{'name': ['aryan', 'balkrishna', 'ayush'], 'age': [18, 20, 19]}

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
{'name': ['aryan', 'balkrishna', 'ayush'], 'age': [18, 20, 19]}
<class 'dict'>

 

a='aryan raj singh rathore'
b=tuple(a)
b
('a', 'r', 'y', 'a', 'n', ' ', 'r', 'a', 'j', ' ', 's', 'i', 'n', 'g', 'h', ' ', 'r', 'a', 't', 'h', 'o', 'r', 'e')

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
(0, 12)
(1, 56)
(2, 41)
(3, 23)
(4, 100)
(5, 20)

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 33, in <module>
    print(i,endl='')
TypeError: 'endl' is an invalid keyword argument for print()

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 33, in <module>
    print(i,end1='')
TypeError: 'end1' is an invalid keyword argument for print()

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
(0, 12)(1, 56)(2, 41)(3, 23)(4, 100)(5, 20)

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
(0, 12)
(1, 56)
(2, 41)
(3, 23)
(4, 100)
(5, 20)

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
0
1
2
3
4
5

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
0
1
2
3
4
5

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
12
56
41
23
100
20

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 43, in <module>
    s
NameError: name 's' is not defined

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
12
56
41

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
12
56
41
23
100
20

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
12
56
41
23
100
20
20
20







x=20
if x%2==0
SyntaxError: expected ':'
if x%2=='0'
SyntaxError: expected ':'
print('even')
even

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
enter the number23
odd

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
enter the number23
odd

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
ENTER THE FIRST NUMBER:23
ENTER THE SECOND NUMBER:454
ENTER THE THIRD NUMBER:678
THIRD NO. is greater

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge
nhi rahenge

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 79, in <module>
    print('**')
KeyboardInterrupt

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
RATHORE
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/8.py", line 79, in <module>
    print('RATHORE')
KeyboardInterrupt

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
ENTER THE NUMBER9
81
90

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
ENTER THE NUMBER8
0
8
16
24
32
40
48
56
64
72
80

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
ENTER THE NUMBER10
0
10
20
30
40
50
60
70
80
90
100

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============
ENTER THE NUMBER6
6 * 0 = 0
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60

============= RESTART: C:/Users/admin/Desktop/python training/8.py =============


============= RESTART: C:/Users/admin/Desktop/python training/8.py =============

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
10
9
8
7
6
5
4
3
2
1

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER23R THE NUMBER6
6 * 0 = 0
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 =
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/9", line 8, in <module>
    a=int(input('ENTER THE FIRST NUMBER'))
ValueError: invalid literal for int() with base 10: '23R THE NUMBER6'













=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER23
ENTER THE second NUMBER45
0.5111111111111111
ENTER THE FIRST NUMBER23
ENTER THE second NUMBER67
0.34328358208955223
ENTER THE FIRST NUMBER56
ENTER THE second NUMBER78
0.717948717948718
ENTER THE FIRST NUMBER
=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:45
0.5111111111111111
Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/9", line 11, in <module>
    c=int(inpur('enter 2 for exit the loop:'))
NameError: name 'inpur' is not defined. Did you mean: 'input'?

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:45
0.5111111111111111
enter 2 for exit the loop:2
ENTER THE FIRST NUMBER:
=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:34
0.6764705882352942
enter 2 for exit the loop:2

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:45
0.5111111111111111
enter 2 for exit the loop:1
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:45
0.5111111111111111
enter 2 for exit the loop:2
THANK YOU

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
ENTER THE FIRST NUMBER:25
ENTER THE second NUMBER:45
0.5555555555555556
enter 2 for exit the loop or type 1 to continue:1
ENTER THE FIRST NUMBER:23
ENTER THE second NUMBER:67
0.34328358208955223
enter 2 for exit the loop or type 1 to continue:2
THANK YOU

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
*****
*****
*****
*****
*****

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
*
**
***
****
*****

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============

=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
*


























































































































































































Traceback (most recent call last):
  File "C:/Users/admin/Desktop/python training/9", line 31, in <module>
    print(a*'*')
KeyboardInterrupt
>>> 
=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
*
**
***
****
*****
******
*******
********
*********
>>> 
=============== RESTART: C:/Users/admin/Desktop/python training/9 ==============
**********
*********
********
*******
******
*****
****
***
**
