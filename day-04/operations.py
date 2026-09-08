Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
b = 20
a+b
30
a-b
-10
a+4
14
a*4
40
a/5
2.0
a//2
5
a%3
1
a**6
1000000
b/4
5.0
b**2
400
#comparission operator
a = 5
b =10
a<b
True
a>b
False
a<= b
True
a>=b
False
a == b
False
a!=b
True
#assignment operator
a = 8
a+= 1
a_=3
a
9
a -=3
a
6
a *=2
a
12
a /= 4
a
3.0
a +5
8.0
a += 5
a
8.0
a //= 2
a
4.0
a **=3
a
64.0
a %=2
a
0.0
#relational operators
a = True
b = False
a and b
False
a or b
True
s in 'aeiou'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s in 'aeiou'
NameError: name 's' is not defined
's' in 'aeiou'
False
's' not in 'aeiou'
True
3%2==0
False
not 3%2 == 0
True
4%5==0 and 3%6 == 0
False
4%5==0 or 3%6 == 0
False
5%4==0 and 6%2==0
False
5%4==0 or 6%2==0
True
6%2 == 0
True
5%4==0
False
#membership operator
#str list tuple set dict
s = 'python in programming'
'python' in s
True
'java' in s
False
'python' not in s
False
'java' not in s
True
l = [1, 2, 3, 5,4]
3 in  l
True
8 in l
False
3 not in l
False
1 not in l
False
2 in l
True
t = (11,22,33,44,55)
11 in l
False
11 not in l
True
23 in l
False
22 in l
False
33  not in l
True
set = {'blue','green','black','white'}
'white' in set
True
'blue' not in set
False
'black' not in set
False
'orange' in set
False
'purple' in set
False
'purple' not in set
True
data = {'name':'raju','no':09,'batch':2}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
data = {'name':'raju','no':9,'batch':2}
'raju' in data
False
>>> 'name' in data
True
>>> 'no' not in data
False
>>> 'age' in data
False
>>> #identity operation:
>>> l =[1,2,3,4]
>>> m =[1,2,3,4]
>>> id(l)
1829868827328
>>> id(m)
1829870117376
>>> l == m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> n in m
False
>>> n is m
True
>>> n is not m
False
>>> 10 & 12
8
>>> 12 | 13
13
>>> 10 ^ 8
2
>>> ~8
-9
>>> ~90
-91
>>> 2<<1
4
>>> 6<<8
1536
>>> 3>>6
0
>>> 90>5
True
>>> 90>>4
5
