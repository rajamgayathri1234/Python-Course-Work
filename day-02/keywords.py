Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a= 10
a
10
a=b=c=10
a
10
b
10
c
10
>>> 
= RESTART: C:/Users/Gayathri rajam/OneDrive/Desktop/python-course-work/day-2/variable.py
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a,b,c = 10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c = 10
TypeError: cannot unpack non-iterable int object
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a =10
>>> b=20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
