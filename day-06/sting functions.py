Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = "codegnan"
s
'codegnan'
s = 'codegnan'
s
'codegnan'
type(s)
<class 'str'>
s =''
s
''
#concadanation
a = 'python'
b = ' programming'
a+b
'python programming'
fname = 'Gayathri'
lname = 'Rajam'
fname+lname
'GayathriRajam'
#repetation
a = 'python'
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
a ='python'
a[:3]
'pyt'
KeyboardInterrupt
KeyboardInterrupt
<class 'KeyboardInterrupt'>
names = 'raju ravi keerthana kalyani gayathri lokesh'
names[:4]
'raju'
name[5:8]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name[5:8]
NameError: name 'name' is not defined. Did you mean: 'fname'?
names[5:8]
'rav'
names[5:9]
'ravi'
names[10:19]
'keerthana'
names[-1:-7]
''
names[-1:7]
''
names = 'raju ravi keerthana kalyani gayathri lokesh'
raju in names
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    raju in names
NameError: name 'raju' is not defined
'raju' in names
True
'keerthana' in names
True
'n' in names
True
'z' in names
False
'gayathri' not in names
False
names = 'raju ravi keerthana kalyani gayathri lokesh'
len(names)
43
ord(a)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 6 found
ord('a')
97
ord('raju')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ord('raju')
TypeError: ord() expected a character, but string of length 4 found
ord('r')
114
ord('u')
117
char(78)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    char(78)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(78)
'N'
chr(108)
'l'
chr(189)
'½'
chr(40)
'('
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'e', 'e', 'e', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'j', 'k', 'k', 'k', 'l', 'l', 'n', 'n', 'o', 'r', 'r', 'r', 'r', 's', 't', 't', 'u', 'v', 'y', 'y']
max(names)
'y'
min(names)
' '
names[1:4]
'aju'
names[-1:-8]
''
names[-9:-16]
''
names[-1:-8:-1]
'hsekol '
names[-8:-1]
'i lokes'
names[-7:]
' lokesh'
s = 'python programminf language'
s.upper()
'PYTHON PROGRAMMINF LANGUAGE'
s.lower()
'python programminf language'
s.swapcase()
'PYTHON PROGRAMMINF LANGUAGE'
s.captialize()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
s.capitalize()
'Python programminf language'
s.title()
'Python Programminf Language'
s.casefold()
'python programminf language'
s = 'python  programming language'
s
'python  programming language'
s.center(50,'-')
'-----------python  programming language-----------'
s.center(50,'*')
'***********python  programming language***********'
s.center(40.'.')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.center(40,'.')
'......python  programming language......'
s.ljust(40,'.')
'python  programming language............'
s.rjust(40,'.')
'............python  programming language'
'1234'.zfill(4)
'1234'
'123'.zfill(4)
'0123'
s = 'python programming language'
s.find('python')
0
s.find('g')
10
s.find('m')
13
>>> s.rfind('a')
24
>>> s.rfind('m')
14
>>> s.find('z')
-1
>>> s.index('a')
12
>>> s.index('m')
13
>>> s.rindex('m')
14
>>> s.rindex('a')
24
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.count(a)
1
>>> s.count('m')
2
>>> s
'python programming language'
>>> s.replace('o',1)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s.replace('o',1)
TypeError: replace() argument 2 must be str, not int
>>> s.replace('o','1')
'pyth1n pr1gramming language'
>>> s.replace('m','2')
'python progra22ing language'
>>> s.replace('python','java')
'java programming language'
>>> s.maketrans('aeiou','#%^&*')
{97: 35, 101: 37, 105: 94, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#%^&*'))
'pyth&n pr&gr#mm^ng l#ng*#g%'
>>> text = 'hello'
>>> text.encode()
b'hello'
>>> b'hello'.decode()
'hello'
