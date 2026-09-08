'''
for i in range(5):
    for j in range(5):
        print("*",end='')
    print()  
o/p:
*****
*****
*****
*****
***** 
    
for i in range(5):
    for j in range(5):
        print(j%2,end='')
    print()
o/p:
01010
01010
01010
01010   

for i in range(5):
    for j in range(5):
        print(i%2,end = '')
    print() 
o/p:
00000
11111
00000
11111
00000      

for i in range(5):
    for j in range(5):
        print((i+j)%2,end=' ')
    print()
o/p:
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0     

for i in range(5):
    for j in range(5):
        print(i+j,end='')
    print()    
o/p:
01234
12345
23456
34567
45678    

c = 1
for i in range(5):
    for j in range(5):
        print(c,end="")
        c+=1
    print()    
o/p:
12345
678910
1112131415
1617181920
2122232425

for i in range(5):
    for j in range(i+1):
        print("*",end = '')
    print()    
o/p:
*
**
***
****
*****    
 
for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()    
o/p:
*****
****
***
**
*

for i in range(5):
    for spa in range(5-i-1):
        print(" ",end='')
    for j in range(i+1):
        print('*',end='')
    print()        
 o/p:
    *
   **
  ***
 ****
*****

n = int(input("enter the number:"))
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')    
    for j in range(5-i):
        print("*",end=" ")
    print()    
o/p:
 * * * * * 
  * * * * 
    * * * 
      * * 
        *    

n = int(input("enter the number:"))
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print("*",end=' ')
    else:
        for k in range(n-i):
            print("*",end=' ')
    print()  
    
n = int(input("enter the number:"))
m = n//2
for i in range(n):
    if i <= m:
        print("*"*(i+1),end=' ')
    else:
        print("*"*(n-i),end=' ')
    print() 
o/p:
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
* 

n = int(input("enter the number:"))
m = n//2
for i in range(n):
    if i <= m:
        print(' '*(m-i),'*'*(i+1),end=' ',sep='')
    else:
        print(' '*(i-m),'*'*(n-i),end=' ',sep='')    
    print()    
o/p:
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *     
    ''' 