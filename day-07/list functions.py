Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = []
l = list()
type(1)
<class 'int'>
l = [1,2,3,4,5,'string','python',[1,2,3,4],{1,2,34,5},3+9j,98]
l
[1, 2, 3, 4, 5, 'string', 'python', [1, 2, 3, 4], {1, 2, 34, 5}, (3+9j), 98]
l = [1,2,1,1,1,1,1,1]
l
[1, 2, 1, 1, 1, 1, 1, 1]
a = [1,2,3]
b = [9,7,5]
a+b
[1, 2, 3, 9, 7, 5]
a*7
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
'0'*9
'000000000'
a = [23, 89, 213, 145, 167, 254]
a
[23, 89, 213, 145, 167, 254]
a[1]
89
a[3]
145
a[0]
23
a[7]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[7]
IndexError: list index out of range
a[:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[:]
[23, 89, 213, 145, 167, 254]
a[1:4]
[89, 213, 145]
a[-1:-4:-1]
[254, 167, 145]
a[-3:]
[145, 167, 254]
a[-2:-5]
[]
a[-2:-5:-1]
[167, 145, 213]
a[::-1]
[254, 167, 145, 213, 89, 23]
a
[23, 89, 213, 145, 167, 254]
23 in a
True
145 in a
True
145 not in a
False
90 not in a
True
a = [12, 34 ,56 ,67, 56, 90, 60]
a
[12, 34, 56, 67, 56, 90, 60]
max(a)
90
min(a)
12
sotred(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sotred(a)
NameError: name 'sotred' is not defined. Did you mean: 'sorted'?
sorted(a)
[12, 34, 56, 56, 60, 67, 90]
len(a)
7
a
[12, 34, 56, 67, 56, 90, 60]
a.append(90)
a.append(89)
a
[12, 34, 56, 67, 56, 90, 60, 90, 89]
a.append(56)
ap.append(56)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ap.append(56)
NameError: name 'ap' is not defined. Did you mean: 'a'?
a.append(56)
a
[12, 34, 56, 67, 56, 90, 60, 90, 89, 56, 56]
a.pop()
56
a.pop()
56
a.pop(0)
12
a.pop()
89
a.remove(65)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove(65)
ValueError: list.remove(x): x not in list
a
[34, 56, 67, 56, 90, 60, 90]
a.remove(56)
a
[34, 67, 56, 90, 60, 90]
a.remove(60)
id(a)
1924239131840
del a[0]
a
[67, 56, 90, 90]
del a[:2]
a
[90, 90]
a.insert(89,6,90,23,34,54)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.insert(89,6,90,23,34,54)
TypeError: insert expected 2 arguments, got 6
>>> a.append(890)
>>> a
[90, 90, 890]
>>> a.insert(1,56)
>>> a
[90, 56, 90, 890]
>>> a.extend([1,2,3,4,5,6])
>>> a
[90, 56, 90, 890, 1, 2, 3, 4, 5, 6]
>>> a.pop()
6
>>> a.remove(5)
>>> a
[90, 56, 90, 890, 1, 2, 3, 4]
>>> del a[:3]
>>> a
[890, 1, 2, 3, 4]
>>> del a[]
SyntaxError: invalid syntax
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = [1, 2, 3, 4, 5. 6, 7, 8, 9, 10]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.clear()
>>> a
[]
>>> id(a)
1924239272384
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.index(8)
7
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
