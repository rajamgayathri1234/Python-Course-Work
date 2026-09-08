Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
t = (1,2,3,4,5,6)
t
(1, 2, 3, 4, 5, 6)
t = (1)
t
1
t = (6)
t
6
t = (1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t = (1,2,3.4,'string','6)
     
SyntaxError: unterminated string literal (detected at line 1)
t
     
(1, 1, 1, 1, 1)
t = (1,2,3.4,'string',6)
     
t
     
(1, 2, 3.4, 'string', 6)
type(t)
     
<class 'tuple'>
t = (1,2,3,4,2.4,5.6,'str',[1,2,3],[6,7,8,9],{3,7,5,9},True)
     
t
     
(1, 2, 3, 4, 2.4, 5.6, 'str', [1, 2, 3], [6, 7, 8, 9], {9, 3, 5, 7}, True)
(1,2,3)+(4,5,6)
     
(1, 2, 3, 4, 5, 6)
(3,4,5)*5
     
(3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5)
t
     
(1, 2, 3, 4, 2.4, 5.6, 'str', [1, 2, 3], [6, 7, 8, 9], {9, 3, 5, 7}, True)
t(0)
     
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t(0)
TypeError: 'tuple' object is not callable
t[0]
     
1
t[-1]
     
True
t[6]
     
'str'
t94]
SyntaxError: unmatched ']'
t[11]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t[11]
IndexError: tuple index out of range
t[-3]
[6, 7, 8, 9]
t[:5]
(1, 2, 3, 4, 2.4)
t[3:7]
(4, 2.4, 5.6, 'str')
t[6:9]
('str', [1, 2, 3], [6, 7, 8, 9])
2 in t
True
True in t
True
str in t
False
5.6 in t
True
90 in t
False
2.4 not in t
False
t = (1,34,56,78,23,456,90,78,94,56,13,56,78,90)
t
(1, 34, 56, 78, 23, 456, 90, 78, 94, 56, 13, 56, 78, 90)
sorted(t)
[1, 13, 23, 34, 56, 56, 56, 78, 78, 78, 90, 90, 94, 456]
max(t)
456
min(t)
1
len(t)
14
t
(1, 34, 56, 78, 23, 456, 90, 78, 94, 56, 13, 56, 78, 90)
t.index(90)
6
t.count(90)
2
sum(t)
1203
all(13,90,23)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    all(13,90,23)
TypeError: all() takes exactly one argument (3 given)
all((13,90,23))
True
any((23,99,00))
True
any(00,11,78))
SyntaxError: unmatched ')'
any((00,11,78))
True
all((999,0))
False
#packed and unpcked
t = (1,2,3)
t
(1, 2, 3)
a,b,c = t
a
1

b
2
c
3
t = (1,2,3,4,[3,2,1],7,8)
t
(1, 2, 3, 4, [3, 2, 1], 7, 8)
t[4]
[3, 2, 1]
t[4].append(5)
t
(1, 2, 3, 4, [3, 2, 1, 5], 7, 8)






#set
s = {}
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,7,8,9,22,55,78,56}
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 22, 55, 56}
s = {1,1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s
{1}
s.add(12.3)
s
{1, 12.3}
s.add("str")
s
{1, 'str', 12.3}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1:2})
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s.add({1:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s
{1, 'str', 12.3}
#only immutable items are allowed
s.add(True)
s
{1, 'str', 12.3}
s.add(False)
s
{False, 1, 'str', 12.3}
a = {1,2,3,4}
b = {3,5,6,7}
2 in a4 in a
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    2 in a4 in a
NameError: name 'a4' is not defined. Did you mean: 'a'?
6 in b
True
a | b
{1, 2, 3, 4, 5, 6, 7}
a & b
{3}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 5, 6, 7}
a<= {1,2}
False
a<={1}
False
a <={3,4,5}
False
c = {4,5,6}
d = {1,2,3}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
c.isdisjoint(d)
True
a.isdisjoint(c)
False
a = {1,2,3,4,5,6,7,8,9}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
sorted(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
min(a)
1
max(a)
9
len(a)
9
a.index(a)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.count(a)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.count(a)
AttributeError: 'set' object has no attribute 'count'
all({1,2,3})
True
all({1,2,9})
True
any({1,0,99})
True
any({23,45,99})
True
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
sum(a)
45
a = {1,2,3,4}
>>> b = a
>>> b.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> b
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4, 5}
>>> c = a.copy()
>>> c
{1, 2, 3, 4, 5}
>>> c.add(6)
>>> c
{1, 2, 3, 4, 5, 6}
>>> a
{1, 2, 3, 4, 5}
>>> a.add(6)
>>> a.add(7)
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.remove(5)
>>> a
{1, 2, 3, 4, 6, 7}
>>> a.remove(7)
>>> a
{1, 2, 3, 4, 6}
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a.remove(5)
KeyError: 5
>>> a.discard(5)
>>> a
{1, 2, 3, 4, 6}
>>> a.pop(6)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop()
1
>>> a
{2, 3, 4, 6}
>>> a.clear()
>>> a
set()
