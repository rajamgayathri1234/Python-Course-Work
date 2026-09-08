'''
i = 1
while i<=10:
    print(i)
    i += 1
    
i = 10
while i>0:
    print(i)
    i -= 1

i = 5
while i <= 50:
    print(i)
    i += 5
    
s = 'while loop'
i = 0
while i<len(s):
    print(s[i])
    i += 1
    
s = 'while loop'
i = len(s)-1
while i>=0:
    print(s[i])
    i -= 1

l = [345,456,567,678,789]
i = 0
while i<len(l):
    print(l[i])
    i += 1
    
# elabrate thr integer
n = 8765
while n>0:
    print(n%10)
    n //=10

#sum the integers
n = 455678
sum = 0
while  n>0:
    sum += n%10
    n//=10
print("sum of digits:",sum)

# product of integers
n = 4567
prod = 1
while n>0:
    prod *= n%10
    n//=10
print('product of integer:',prod)    

# reverse thr integer
n = 23456
res = 0
while n>0:
    rem = n%10
    res = res * 10 + rem
    n //=10
print(res)    

# sum even of integers
n = 234568
res = 0
while n>0:
    rem = n%10
    if rem%2 == 0:
        res += rem
    n //=10
print(res)

l = [7,9,2,3,4,0,0,0,8,9,1,0,4,8,0,4,0,9,1,0,7]
while 0 in l:
    l.remove(0)
print(l)
'''
# sum of first and last numbers
l = [2,3,4,7,9,7,12,6,10,12,10]
i = 0
j = len(l) - 1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i += 1
    j -=1
            
