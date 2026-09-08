Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '       Hell World       '
s.trip()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.trip()
AttributeError: 'str' object has no attribute 'trip'. Did you mean: 'strip'?
s.strip()
'Hell World'
s.lstrip()
'Hell World       '
s.lstrip()
'Hell World       '
s.rstrip()
'       Hell World'
s.replace(' ','')
'HellWorld'
s = 'java-python-flask-mysql-fastapi-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
s.rsplit('-',2)
['java-python-flask-mysql', 'fastapi', 'c']

l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
s = ['python'.'java'.'mysql'.'flask']
SyntaxError: invalid syntax
s = ['python','java','mysql','flask']
''.join(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ''.join(c)
NameError: name 'c' is not defined
''.join(s)
'pythonjavamysqlflask'
' '.join(s)
'python java mysql flask'
', '.join(s)
'python, java, mysql, flask'
'@ '.join(s)
'python@ java@ mysql@ flask'
'-'.join({1-2-3-4})
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    '-'.join({1-2-3-4})
TypeError: sequence item 0: expected str instance, int found
'-'.join({'1','2','3','4'})
'2-3-4-1'
a = 'strings.py'
a.partition('.')
('strings', '.', 'py')
a.partition('.')
('strings', '.', 'py')
a = 'string.py.java.png.txt'
a
'string.py.java.png.txt'
a.partition()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.partition()
TypeError: str.partition() takes exactly one argument (0 given)
a.partition('')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.partition('')
ValueError: empty separator
a.partition(' ')
('string.py.java.png.txt', '', '')
a.partition('.')
('string', '.', 'py.java.png.txt')
a = 'stringpython.py'
a.startswith("str")
True
a.endswith("py")
True
a.endswith("phy")
False
'python89'.islower()
True
a.endswith('.py")
           
SyntaxError: unterminated string literal (detected at line 1)
a.endswith(".py")
           
True
'python0807'.islower()
           
True
'plonthr'.isupper()
           
False
'Pyton90'.isupper()
           
False
'PYTHON236@rhth'.isupper()
           
False
'Pythoniedheo234@'.isupper()
           
False
"PYTHON
           
SyntaxError: unterminated string literal (detected at line 1)
"PYTHON".isupper()
           
True
'edefnwicv'isalpha()
           
SyntaxError: invalid syntax
'dbccuoc'.isalpha()
           
True
'ih cc787'.isalnum()
           
False
'hcanscijosn'.isalpha()
           
True
\
'12334456'.isalnum()
           
True
'           '.isspace()
           
True
>>> '   hello'.isspace()
...            
False
>>> 'Hlo Worls'.istitle()
...            
True
>>> 'Hello worlld'.istitle()
...            
False
>>> 
>>> 'my_var'.isidentifier()
...            
True
>>> 'my#val'.isidentifier()
...            
False
>>> 'mu78val'.isidentifier()
...            
True
>>> a.partition('.')
...            
('stringpython', '.', 'py')
>>> '1234567'.isdecimal'()
...            
SyntaxError: unterminated string literal (detected at line 1)
>>> '1234567'.isdecimal()
...            
True
>>> 'ERTYGVBGH567'.isdecimal()
...            
False
>>> '23456'.isdigit()
...            
True
>>> '987654'.isnmeric()
...            
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    '987654'.isnmeric()
AttributeError: 'str' object has no attribute 'isnmeric'. Did you mean: 'isnumeric'?
>>> '98765'isnumeric()
...            
SyntaxError: invalid syntax
>>> '123456'.isnumeric()
...            
True
