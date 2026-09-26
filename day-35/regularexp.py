'''
# match function (it search the first element)
import re

pattern = r'[0-9]'
text = 'codegana2026'

res = re.match(pattern, text)
print(res.group() if res else "Pattren not matched")

# search Function(find the first digit)
import re

pattern = r'[0-9]'
text = 'codegana2026'

res = re.search(pattern, text)
print(res.group() if res else "Pattren not matched")

#findall(find all matching values.)
import re
pattren = r'[0-9]'
text = 'codegnan2026'
res  = re.findall(pattren,text)
print(res)

#finditer(find the all matches and return in their index value)
import re
pattren = r'[0-9]'
text = 'codegnan2026'
res  = re.finditer(pattren,text)
for i in res:
    print(i.group(),i.start())

#full match (it's all about matched)    
import re
pattren = r'[0-9]{10}'
text = '9876543210'

res = re.fullmatch(pattren,text)
print(res.group() if res else "pattren not matched")

#checks whether the entire string matches the pattern.
import re
pattern=r'[,@:;_&]'
text='java,python@c:flask_mysql&django'
res=re.split(pattern,text)
print(res)

#sub(sub is used to replace mt pattern in something else)
import re
pattren = r'[aeiou0-9]'
text = 'python 30 mysql 23 flask 20 django 80'
res = re.sub(pattren,'*',text)
print(res)
#.
import re
pattern = r'h.t'
text = 'hand loom hot hit hat hood wood'
res = re.findall(pattern,text)
print(res)

#^
import re
pattern = r'^[a-z]'
text = 'hand loom hot hit hat hood wood'
res = re.findall(pattern,text)
print(res)

import re
pattern = r'[a-z]$'
text = 'hand loom hot hit hat hood wood8'
res = re.findall(pattern,text)
print(res)

import re
pattren = r'ab+'
text = 'a ab abb abbb aaaaaabbbbbbb'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'^(91|0)'
text = '09876123456'
res = re.findall(pattren,text)
print(res)

import re
pattren = r'[A-Za-z0-9]'
text = 'asdefrGTHB1dfg45'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'(ae)'
text = 'aesdefrGTHB1dfg45'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'[0-9]{2}'
text = 'aesdefrGTHB1dfg45654'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'\w'
text = 'aesdefrGTH  B1dfg45654'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'\s'
text = 'aesdefrGTH  B1dfg45654'
res = re.findall(pattren, text)
print(res)

import re
pattren = r'\S'
text = 'aesdefrGTH  B1dfg45654'
res = re.findall(pattren, text)
print(res)

import re
name = input("Enter your name:")
pattren = r'^[a-zA-Z]{2, 25}( [a-zA-Z]{2,25})+$'
res = re.fullmatch(pattren,name)
print("valid name" if res else "Invalid name")

import re
email = input("Enter the email: ")
pattren = r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[A-Za-z]{2,}+$'
res = re.fullmatch(pattren,email)
print("valid name" if res else "Invalid name")

import re
number = input("Enter the numbwer: ")
pattren = r'^[6-9]\d{9}'
res = re.fullmatch(pattren,number)
print("valid number" if res else "Invalid number")
'''
import re
password = input("Enter the password: ")
pattren = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!*%?&])[A_Za-z\d@$!%*?&]{8,}$'
res = re.fullmatch(pattren,password)
print("Valid Password" if res else "Invalid Password")

import re
password = input("Enter the password: ")
pattern = r'^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[@$!%*?&_])[A-Za-z][A-Za-z0-9@$!%*?&_]{7,19}$'
res = re.fullmatch(pattren,password)
print("Valid Password" if res else "Invalid Password")