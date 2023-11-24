Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(14,'xyz',32.7,100)
type(t)
<class 'tuple'>
t1=14,'sxy'34.5,200
SyntaxError: invalid syntax
t1=14,'sxy',34.5,200
type(t)
<class 'tuple'>
t1
(14, 'sxy', 34.5, 200)
t
(14, 'xyz', 32.7, 100)
len(t)
4
len(t1)
4
2*t
(14, 'xyz', 32.7, 100, 14, 'xyz', 32.7, 100)
t+t1
(14, 'xyz', 32.7, 100, 14, 'sxy', 34.5, 200)
4*t+3*t1
(14, 'xyz', 32.7, 100, 14, 'xyz', 32.7, 100, 14, 'xyz', 32.7, 100, 14, 'xyz', 32.7, 100, 14, 'sxy', 34.5, 200, 14, 'sxy', 34.5, 200, 14, 'sxy', 34.5, 200)
t[1]
'xyz'
t
(14, 'xyz', 32.7, 100)
t[4:0:-1]
(100, 32.7, 'xyz')
t[5:0:-1]
(100, 32.7, 'xyz')
t[5:-1:-1]
()
t[5:-0:-1]
(100, 32.7, 'xyz')
t2=(12, 34 , 56(23, 'aryan',34,56))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t2=(12, 34 , 56(23, 'aryan',34,56))
TypeError: 'int' object is not callable
t2=(12, 34 , 56,(23, 'aryan',34,56))
t2
(12, 34, 56, (23, 'aryan', 34, 56))
t2[3][1][2]
'y'
t2
(12, 34, 56, (23, 'aryan', 34, 56))
t2+100
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t2+100
TypeError: can only concatenate tuple (not "int") to tuple
t2
(12, 34, 56, (23, 'aryan', 34, 56))
x=[2,3]
x+100
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x+100
TypeError: can only concatenate list (not "int") to list
x+=100
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x+=100
TypeError: 'int' object is not iterable
x.append(100)
x
[2, 3, 100]
x.extend(100)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x.extend(100)
TypeError: 'int' object is not iterable
t2
(12, 34, 56, (23, 'aryan', 34, 56))









































t2
(12, 34, 56, (23, 'aryan', 34, 56))
t2+=100,
t2
(12, 34, 56, (23, 'aryan', 34, 56), 100)
t2.count(56)
1
t2.index(12)
0
t2.index(56)
2
t2.count(23)
0
max(t2)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    max(t2)
TypeError: '>' not supported between instances of 'tuple' and 'int'
t1=12,34,56
t1
(12, 34, 56)
max(t1)
56
min(t1)
12
t1.sort()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t1.sort()
AttributeError: 'tuple' object has no attribute 'sort'
x
[2, 3, 100]
x.sort()
x
[2, 3, 100]
d={'name':'Aryan','Roll No.':19}
print(d)
{'name': 'Aryan', 'Roll No.': 19}
d
{'name': 'Aryan', 'Roll No.': 19}
type(d)
<class 'dict'>
len(d)
2
d.keys()
dict_keys(['name', 'Roll No.'])
d.values()
dict_values(['Aryan', 19])
d.items()
dict_items([('name', 'Aryan'), ('Roll No.', 19)])
d[1]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d[1]
KeyError: 1
d[name]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d[name]
NameError: name 'name' is not defined
d['name']
'Aryan'
d1={'name':['Aryan','Aditya','Ayush','Manaktala'],'Roll No.':[18,19,20,21]}
d1
{'name': ['Aryan', 'Aditya', 'Ayush', 'Manaktala'], 'Roll No.': [18, 19, 20, 21]}
d2={'name':['Aryan','Aditya','Ayush','Manaktala'],'Roll No.':[18,19,20,21],'age':[32,12,28,22]}
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'Manaktala'], 'Roll No.': [18, 19, 20, 21], 'age': [32, 12, 28, 22]}
d2['name']
['Aryan', 'Aditya', 'Ayush', 'Manaktala']
d2['name'][0][5:0:-1]
'nayr'
d2['name'][0][::-1]
'nayrA'
d1['Branch']=['IT','ECE','CIVIL','CSE']
d2['Branch']=['IT','ECE','CIVIL','CSE']
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'Manaktala'], 'Roll No.': [18, 19, 20, 21], 'age': [32, 12, 28, 22], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2['name']
['Aryan', 'Aditya', 'Ayush', 'Manaktala']
d2['name'][3]
'Manaktala'
d2['name'][3]+='arya'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'Manaktalaarya'], 'Roll No.': [18, 19, 20, 21], 'age': [32, 12, 28, 22], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2['name'][3]='arya'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'age': [32, 12, 28, 22], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2['age']
[32, 12, 28, 22]
d2['age']=del
SyntaxError: invalid syntax
del d2['age']
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2['branch']='stream'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE'], 'branch': 'stream'}
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE'], 'branch': 'stream'}
d2.pop('Roll No.')
[18, 19, 20, 21]
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE'], 'branch': 'stream'}
d2.pop('branch')
'stream'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d2.pop('branch')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    d2.pop('branch')
KeyError: 'branch'
d2.pop('Branch')
['IT', 'ECE', 'CIVIL', 'CSE']
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya']}
d2['name']
['Aryan', 'Aditya', 'Ayush', 'arya']
d2['name']+='singhal'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l']}
d2['name']+'singhal'
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    d2['name']+'singhal'
TypeError: can only concatenate list (not "str") to list
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l']}
d2['name']+['singhal']
['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l', 'singhal']
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l']}
d2['name'].append('singhal')
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l', 'singhal']}
d2.pop('s', 'i', 'n', 'g', 'h', 'a', 'l',)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d2.pop('s', 'i', 'n', 'g', 'h', 'a', 'l',)
TypeError: pop expected at most 2 arguments, got 7
d2.pop('s', 'i')
'i'
d2
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya', 's', 'i', 'n', 'g', 'h', 'a', 'l', 'singhal']}
d3={'name': ['Aryan', 'Aditya', 'Ayush', 'arya'],'Branch':['it','cse','ece']}
d3
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Branch': ['it', 'cse', 'ece']}
d3['stream']=d3.pop('Branch')
d3
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'stream': ['it', 'cse', 'ece']}
d1
{'name': ['Aryan', 'Aditya', 'Ayush', 'Manaktala'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE']}
d1+d3
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    d1+d3
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
d1.update(d3)
d1
{'name': ['Aryan', 'Aditya', 'Ayush', 'arya'], 'Roll No.': [18, 19, 20, 21], 'Branch': ['IT', 'ECE', 'CIVIL', 'CSE'], 'stream': ['it', 'cse', 'ece']}
'age' in d1
False
'Roll No.' in d1
True



>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 
>>> s1={22,33,4,56,78,55,55,55,78,,88,99,99,99}
SyntaxError: invalid syntax
>>> s1={22,33,4,56,78,55,55,55,78,88,99,99,99}
>>> s1
{33, 99, 4, 78, 22, 55, 56, 88}
>>> s2=
SyntaxError: invalid syntax
>>> s2={100,7,10,12,34}
>>> s2
{34, 100, 7, 10, 12}
>>> s1.union(s2)
{33, 34, 99, 4, 100, 7, 10, 12, 78, 22, 55, 56, 88}
>>> s1.intersection(s2)
set()
>>> s1.add(200)
>>> s1
{33, 99, 4, 200, 78, 22, 55, 56, 88}
>>> s1.sub(33)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s1.sub(33)
AttributeError: 'set' object has no attribute 'sub'
>>> s1.remove(33)
>>> s1
{99, 4, 200, 78, 22, 55, 56, 88}
>>> s1.discard(4)
>>> s1
{99, 200, 78, 22, 55, 56, 88}
>>> s1.pop()
99
>>> s1
{200, 78, 22, 55, 56, 88}
