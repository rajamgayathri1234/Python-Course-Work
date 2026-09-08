

#list comprehension
'''
l = []
for i in range(1,11):
    l.append(i)
print(l)

l =[i for i in range(1,11)]
print(l)

#factors
n = 12
f = [i for i in range(1,n+1) if n%i == 0]
print(f)


#even and odd
x = [1,2,3,4,5,6]
y = [ i if i%2==0 else 0 for i in x]
print(y)

#evev position 
m = [ i for i in range(2,11,2)]
print(m)


l =[]
for i in range(3):
    temp = []
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)    

l = [[j for j in range(1,4)] for i in range(3)]
print(l)
'''
#set comprehension
s = {i for i in range(1,11)}
print(s)

#dictionary compreshion
d = {i:i*i for i in range(1,11)}
print(d)