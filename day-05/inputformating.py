Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input formation
a = input()
codegnan
a
'codegnan'
a = input()
12345
a
'12345'
a = input("Enter the value: ")
Enter the value: gayathri
a
'gayathri'
marks = input("enter the marks:")
enter the marks:5678
marks
'5678'
marks = int(input("Enter the marks:"))
Enter the marks:8976
a
'gayathri'
marks
8976
price = float(input("enter the price"))
enter the price 657.89
price
657.89
cgpa = float(input("enter the cgpa:"))
enter the cgpa:5678
cgpa
5678.0
names = input('Enter the names:")
              
SyntaxError: unterminated string literal (detected at line 1)
names = input('Enter the names:')
              
Enter the names:raju ravi rani
names
              
'raju ravi rani'
names.split()
              
['raju', 'ravi', 'rani']
names = 'raju,ravi,rani'
              
names.split(',')
              
['raju', 'ravi', 'rani']
course = 'python-java-c++-flask'
              
course.split('-')
              
['python', 'java', 'c++', 'flask']
set(course)
              
{'k', 'a', '-', 'c', 't', 'v', '+', 'j', 's', 'f', 'y', 'l', 'p', 'n', 'o', 'h'}
a = set(input("enter the value:").split())
              
enter the value:2 3245678
a
              
{'2', '3245678'}
names = input("enter names:").split()
              
enter names:rju ravi rani
names
              
['rju', 'ravi', 'rani']
name = tuple(input('enter names:').split())
              
enter names:raju ravi rani
names
              
['rju', 'ravi', 'rani']
marks = input().split()
              
34 57 89 56 12 46 89
masrks
              
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    masrks
NameError: name 'masrks' is not defined. Did you mean: 'marks'?
marks
              
['34', '57', '89', '56', '12', '46', '89']
map(int,marks)
              
<map object at 0x0000028701263FC0>
marks
              
['34', '57', '89', '56', '12', '46', '89']
list(map(int,marks))
              
[34, 57, 89, 56, 12, 46, 89]
marks = list(map(int,input('enter the values:').split()))
              
enter the values:67 b5 89 67 34 89 99
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    marks = list(map(int,input('enter the values:').split()))
ValueError: invalid literal for int() with base 10: 'b5'
67 88 90 55 34
              
SyntaxError: invalid syntax
marks = list(map(int,input('enter the values:').split()))
              
enter the values:90 89 78 77 66 90 34 56
marks
              
[90, 89, 78, 77, 66, 90, 34, 56]
marks = tuple(map(int,input('enter the values:').split()))
              
enter the values:78 67 55 45 89 77 23 45 31
marks
              
(78, 67, 55, 45, 89, 77, 23, 45, 31)
marks = set(map(int,input('enter the values:').split))
              
enter the values:45 33 78 67 99 56 89 76
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    marks = set(map(int,input('enter the values:').split))
TypeError: 'builtin_function_or_method' object is not iterable
marks
              
(78, 67, 55, 45, 89, 77, 23, 45, 31)
marks = set(map(int,input('enter the values:').split()))
              
enter the values:56 45 34 78 56 22 89 56
marks
              
{34, 45, 78, 22, 56, 89}
marks = float(input('enter the values:').split())
              
enter the values:67 89 45.0 87.9 23.8
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    marks = float(input('enter the values:').split())
TypeError: float() argument must be a string or a real number, not 'list'
marks = list(map(float,input('enter the values:').split()))
              
enter the values:56 78 90.9 23.7 45.8
marks
              
[56.0, 78.0, 90.9, 23.7, 45.8]
#packing and unpacking
              
a,b =[1,2]
              
a
              
1
b
              
2
a,b,c = (1,1.2."str")
              
SyntaxError: invalid syntax
a,b,c = (1,1.2,"str")
              
a
              
1
b
              
1.2
c
              
'str'
email,password = input("Enter the email, password").split())
SyntaxError: unmatched ')'
email,password = input("Enter the email, password").split())

SyntaxError: unmatched ')'
email,password = input("Enter the email, password").split()
Enter the email, password gayathri@.in 897654
email
'gayathri@.in'
password
'897654'
name, marks = list(map(int,input("enter the marks:").split()))
enter the marks:45 67 22 89 56 78 45
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    name, marks = list(map(int,input("enter the marks:").split()))
ValueError: too many values to unpack (expected 2, got 7)
name, marks = list(map(int,input("enter the name, marks:").split()))
enter the name, marks:raju 89
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    name, marks = list(map(int,input("enter the name, marks:").split()))
ValueError: invalid literal for int() with base 10: 'raju'
name, marks = list(map(input("enter the marks:").split()))
enter the marks:rahju 89
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    name, marks = list(map(input("enter the marks:").split()))
TypeError: map() must have at least two arguments.
name,marks = list(map(int,input("enter the marks:").split()))
enter the marks:raju 89
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name,marks = list(map(int,input("enter the marks:").split()))
ValueError: invalid literal for int() with base 10: 'raju'
name,marks = list(map(input("enter the value:").split()))
enter the value:raju 89
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    name,marks = list(map(input("enter the value:").split()))
TypeError: map() must have at least two arguments.
>>> a,b,c = list(map(int,input().split()))
12 4 67
>>> a
12
>>> b
4
>>> c
67
>>> states = evl(input())
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    states = evl(input())
NameError: name 'evl' is not defined. Did you mean: 'eval'?
>>> states = eval(input())
4
>>> states
4
>>> name,marks=input("enter the name and marks:").split()
enter the name and marks:raju 89
>>> name
'raju'
>>> marks
'89'
>>> int(marks)
89
>>> status
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    status
NameError: name 'status' is not defined. Did you mean: 'states'?
>>> status = eval(input())
True
>>> type(status)
<class 'bool'>
>>> status = eval(input())
2+3j
>>> type(status)
<class 'complex'>
>>> ststus = eval(input())
[1,2,3,4,5]
>>> type(status)
<class 'complex'>
>>> type(ststus)
<class 'list'>
