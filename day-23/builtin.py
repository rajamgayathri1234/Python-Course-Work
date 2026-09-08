'''import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")


import platform

print(platform.system())
print(platform.release())
print(platform.processor())


import math

print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))  #greatest common divisor
print(math.sqrt(36))
print(math.pow(2,3))

import math
print(round(12.666666))
print(round(12.9999999))

print(math.ceil(12.000000001))
print(math.ceil(12.3))
print(math.ceil(12.66666))
print(math.ceil(12.99999))

print(math.floor(12.0000001))
print(math.floor(12.3))
print(math.floor(12.666666))
print(math.floor(12.9999999))

#random module is used to random numbers in program

import random
random.seed(9)

print(random.random())
print(random.randint(1000,9999))
print(random.uniform(1,6))

l = ['r','s','p']
print(random.choice(l))

lang = ['java','python','css','javascript']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)


#collection module
from collections import Counter

s = 'python programming'
res = Counter(s)
print(res)


s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)            


from collections import Counter,defaultdict

products = ['sugur','salt','milk']
res = defaultdict(list)

for i in products:
    res[i].append(['des','res','com'])
print(res)    

s = 'python program'
d = defaultdict(int)

for i in s:
    d[i]+=1
print(d)    


from collections import Counter,defaultdict,deque

l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()
print(l)
'''
from collections import Counter,defaultdict,deque

l = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)