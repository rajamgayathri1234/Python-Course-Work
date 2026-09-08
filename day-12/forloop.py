# string  list tuple set dict range
# for var in seq:
     #statements
'''
s = 'python programming'
for i in s:
    print(i)


list = [1,2,3,4,5,6,7]
for num in list:
    print(num)
    
tuple = (23,45,67,89,87,567)
for n in tuple:
    print(n)
    
set = {34,89,23,12,56,78,99}
for i in set:
    print(i)
    
dict = {1:2,3:5,9:0,5:8,2:7}
for num in dict:
    print(num)
    
name  = {'gayathri', 'anu', 'keerthana'}
for i in name:
    print(i)
# range(start,end+1,step):(0,,1)
for i in range(1,11):
    print(i)
   
for i in range(2,21,2):
    print(i)
    
for i in range(5,101,5):
    print(i)
    
for i in range(5,0,-1):
    print(i)
    
for i in range(19,0,-2):
    print(i)

dict = {1:2,3:5,9:0,5:8,2:7}
for num in dict:
    print(num,dict[num])
    
s = 'python programming'
for i in range(len(s)):
    print(i,s[i])

# range function is used for list, string, tuple.(it is used for ordered elements and indexing)


s = [23,45,67,99,78,67]
for i in enumerate(s):
    print(i[0],i[1])
    
d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
    
s = [1,2,3,4,5,6,7,8,9]
for i in enumerate(s):
    print(i)
    
for i in range(1,11):
    if i==5:
        break
    print(i)
    
for i in range(1,11):
    if i==5:
        continue
    print(i)
    
for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("End of the program")    
    
l = [12,13,14,15,16,17,18]
n = 26
for i in l:
    if i == n:
        print(i,'found')
        break
else:
    print(n,'not found')    

l = [12,13,14,15,16,17,18]
n = 26
for i in l:
    if i == n:
        print(i,'found')
    
else:
    print(n,'not found') 
pin = 123
for i in range(5):
    epin = int(input("Enter the phone"))
    if pin == epin:
        print("unlock the phone")
        break
    else:
        print('invalid pin')    
else:
    print("wait after 30 minutes")        
    
#prime number or not
n = int(input("Enter the number:"))
c =0
for i in range(1,n+1):
    if n % i == 0:
        c = c+1
if c == 2:
    print('prime')
else:
    print('not a prime')       '''
n = int(input('enter the value:'))
for i in range(2,n//2+1):
    if n%i == 0:
        print("not a prime")
        break
else:
    print("prime number")        
