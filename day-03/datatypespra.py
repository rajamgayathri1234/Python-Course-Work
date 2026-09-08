Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
b = 3.98
type(b)
<class 'float'>
c = 3+11j
print(c)
(3+11j)
type(c)
<class 'complex'>
s = 'python'
id(s)
2208860978848
s +=  'codegnan'
id(s)
2208873081840
l = [10,20,30,40,50,'str',5.6]
l
[10, 20, 30, 40, 50, 'str', 5.6]
id(l)
2208881707968
add.l(20)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    add.l(20)
NameError: name 'add' is not defined
l.add(90)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.add(90)
AttributeError: 'list' object has no attribute 'add'
l.append(67)
id(l)
2208881707968
t = (2,4,5,'str',9.7,7)
t
(2, 4, 5, 'str', 9.7, 7)
t.append(56)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.append(56)
AttributeError: 'tuple' object has no attribute 'append'
t.add(20)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.add(20)
AttributeError: 'tuple' object has no attribute 'add'
type(t)
<class 'tuple'>
s = [1,2,3,4,2,7,9]
s
[1, 2, 3, 4, 2, 7, 9]
id(s)
2208881842368
s.append(7)
s
[1, 2, 3, 4, 2, 7, 9, 7]
id(s)
2208881842368
d = {name:'raju',no:42,age:22}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d = {name:'raju',no:42,age:22}
NameError: name 'name' is not defined
d = {'name':'raju',no:42,age:22}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d = {'name':'raju',no:42,age:22}
NameError: name 'no' is not defined
>>> d = {'name':'raju','no':42,'age':22}
>>> id(d)
2208881677376
>>> id.append('group':"cse")
SyntaxError: invalid syntax
>>> d.append('group':"cse")
SyntaxError: invalid syntax
>>> set.add(6)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    set.add(6)
TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'int' object
>>> s.add(3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.add(3)
AttributeError: 'list' object has no attribute 'add'
>>> s = {1,2,3,4,5,6,7}
>>> s = frozenset({1,22,3,18,56,45,78})
>>> s
frozenset({1, 18, 3, 22, 56, 45, 78})
>>> a = true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = True
>>> b
3.98
>>>  a = True
...  
SyntaxError: unexpected indent
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> a = {}
>>> l = []
>>> t = ()
>>> s = ''
>>> s = None
>>> s
>>> type(s)
<class 'NoneType'>
