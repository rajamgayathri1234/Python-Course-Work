Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
float(a)
10.0
liat(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    liat(a)
NameError: name 'liat' is not defined. Did you mean: 'list'?
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
str(a)
'10'
f = 64.8
int(f)
64
complex(f)
(64.8+0j)
set(f)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
c = 23+ 8j
int(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(c)
True
set(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
str(c)
'(23+8j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s = 'codegnan'
a ='12345'
int(a)
12345
int(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(a)
12345.0
bool(a)
True
bool(s)
True
set(s)
{'g', 'a', 'c', 'e', 'd', 'o', 'n'}
set(a)
{'3', '4', '1', '2', '5'}
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
list(a)
['1', '2', '3', '4', '5']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
tuple(a)
('1', '2', '3', '4', '5')
dict(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
set = {1,3,5,22,4,3,5,9}
int(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
bool(s)
True
str(s)
'codegnan'
s = {2,1,4,5,7,3,2,0}
int(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
bool(s)
True
complex(s)]
SyntaxError: unmatched ']'
str(s)
'{0, 1, 2, 3, 4, 5, 7}'
list(s)
[0, 1, 2, 3, 4, 5, 7]
tuple(s)
(0, 1, 2, 3, 4, 5, 7)
dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
l = [1,2,3,4,5,6,7,1,2,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
bool(l)
True
str(l)
'[1, 2, 3, 4, 5, 6, 7, 1, 2, 4]'
list(l)
[1, 2, 3, 4, 5, 6, 7, 1, 2, 4]
tuple(l)
(1, 2, 3, 4, 5, 6, 7, 1, 2, 4)
dict(l)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
t = (1,3,7,88,34,56,90)
int(t)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
bool(t)
True
complex(t)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
tuple(t)
(1, 3, 7, 88, 34, 56, 90)
str(t)
'(1, 3, 7, 88, 34, 56, 90)'
set(t)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    set(t)
TypeError: 'set' object is not callable
list(t)
[1, 3, 7, 88, 34, 56, 90]
dict(t)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
dict = {1:2,5:9,6:8}
int(d)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
float(d)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
str(d)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    str(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
set(d)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    set(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d = {1:2,5:9,6:8}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> bool(d)
True
>>> str(d)
'{1: 2, 5: 9, 6: 8}'
>>> set(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    set(d)
TypeError: 'set' object is not callable
>>> list(d)
[1, 5, 6]
>>> tuple(d)
(1, 5, 6)
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(d)
TypeError: 'dict' object is not callable
>>> set(d)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(d)
TypeError: 'set' object is not callable
