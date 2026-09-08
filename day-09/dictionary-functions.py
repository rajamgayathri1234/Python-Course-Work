Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #mutable ordered het dynamic unidu
>>> #dictionary
>>> d = {}
>>> d = dict()
>>> type(d)
<class 'dict'>
>>> d = {1:4,2:5,3:7,4:9}
>>> d
{1: 4, 2: 5, 3: 7, 4: 9}
>>> d = {]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> d = {}
>>> d[1] = 1
>>> d[12.3] = 1
>>> d['str'] = 1
>>> d[(1,2,3)] = 1
>>> d[(2+3j)] = 1
>>> d[True] = 1
>>> d[[1,2,3]] = 1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[[1,2,3]] = 1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
>>> d[False] = 1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
>>> d[1] = 1
>>> d[2] = 12.3
>>> d[3] = 'str'
>>> d[4] = 2+3j
>>> d[5] = True
>>> d[6] = [1,2,3]
>>> d[7] = (1,2,3)
>>> d[8] ={1,2,3}
>>> d[9] = frozenset({1,2,3})
>>> d[10] = {1:1,2:2}
>>> d[11] = None
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
>>> d = {}
>>> d[1] = 2
>>> d[1] = 3
d
{1: 3}
d = {'name': 'gayathri','course':'pfs', 'batch':65}
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65}
'name' in d
True
'gayathri, in d
SyntaxError: unterminated string literal (detected at line 1)
'gayathri' in d
False
'65' in d
False
data.get('name')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    data.get('name')
NameError: name 'data' is not defined
d.get('name')
'gayathri'
d.get('batch')
65
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65}
d.get('course')
'pfs'
d['name']
'gayathri'
d['course']
'pfs'
d['batch']
65
d.get('age','key is not present')
'key is not present'
d.get('batch','key is not present')
65
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65}
 d['age'] = 21
 
SyntaxError: unexpected indent
d['age'] = 21
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21}
d['phno'] = 32456789
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 32456789}
d.update({'email':'rajamg@gmail.com','py':2026})
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 32456789, 'email': 'rajamg@gmail.com', 'py': 2026}
id(d)
2235729136064
d['py']
2026
data['py'] = 2028
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    data['py'] = 2028
NameError: name 'data' is not defined
d['py'] = 2028
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 32456789, 'email': 'rajamg@gmail.com', 'py': 2028}
d['age'] = 20
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 20, 'phno': 32456789, 'email': 'rajamg@gmail.com', 'py': 2028}
d.popitem()
('py', 2028)
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 20, 'phno': 32456789, 'email': 'rajamg@gmail.com'}
d.pop(age)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d.pop(age)
NameError: name 'age' is not defined
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 20, 'phno': 32456789, 'email': 'rajamg@gmail.com'}
d.pop('age')
20
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'phno': 32456789, 'email': 'rajamg@gmail.com'}
d.pop('email')
'rajamg@gmail.com'
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'phno': 32456789}
len(d)
4
sorted(d)
['batch', 'course', 'name', 'phno']
max(d)
'phno'
min(d)
'batch'
d.clear()
d
{}
d = {1:2, 2:2,3:3,4:4}
d
{1: 2, 2: 2, 3: 3, 4: 4}
e = d
e[5] = 5
e
{1: 2, 2: 2, 3: 3, 4: 4, 5: 5}
d
{1: 2, 2: 2, 3: 3, 4: 4, 5: 5}
e = d.copy()
e
{1: 2, 2: 2, 3: 3, 4: 4, 5: 5}
e[6] =6
e
{1: 2, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
d
{1: 2, 2: 2, 3: 3, 4: 4, 5: 5}
d.keys()
dict_keys([1, 2, 3, 4, 5])
d.values()
dict_values([2, 2, 3, 4, 5])
d.items()
dict_items([(1, 2), (2, 2), (3, 3), (4, 4), (5, 5)])
sorted(d)
[1, 2, 3, 4, 5]
min(d)
1
max(d)
5
sum(d)
15
len(d)
5
d = {'name': 'gayathri','course':'pfs', 'batch':65,'age':21,'email':'gayatri34@gmail.com','py':2026}
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'gayatri34@gmail.com', 'py': 2026}
d.get('py')
2026
d.setdefault('py',2026)
2026
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'gayatri34@gmail.com', 'py': 2026}
data.setdefault('name',2026)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    data.setdefault('name',2026)
NameError: name 'data' is not defined
d.setdefault('name',2026)
'gayathri'
d.setdefault('email',2026)
'gayatri34@gmail.com'
d
{'name': 'gayathri', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'gayatri34@gmail.com', 'py': 2026}
dict.fromkeys{['python','c','java'],0}
SyntaxError: invalid syntax
dict.fromkeys[['python','c','java'],0]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    dict.fromkeys[['python','c','java'],0]
TypeError: 'builtin_function_or_method' object is not subscriptable
dict.fromkeys(['python','c','java'],0)
{'python': 0, 'c': 0, 'java': 0}
