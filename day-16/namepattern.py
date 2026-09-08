'''
n = int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end = " ")    
    print()    
o/p:
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0  or i == n-1 or j == n-1 or i == m:
            print("*",end=" ")
        else:
            print(" ", end = " ")
    print()             
o/p:
enter the value:5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == m or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()            
o/p:
enter the value:5
* * * * * 
*         
* * * * * 
*         
* * * * *     

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == m:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()  
o/p:
enter the value:5
* * * * * 
*         
* * * * * 
*         
*   

n = int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print() 
o/p:
 enter the value:5
* * * * * 
*         
*         
*         
* * * * * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or (j == n-1 and i > m) or (i ==m and j >= m):
            print("*",end=" ")
        else:
            print(" ",end= " ")
    print()             
o/p:
enter the value:5
* * * * * 
*         
*   * * * 
*       * 
* * * * *     

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == m:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()            
o/p:
enter the value:5
*       * 
*       * 
* * * * * 
*       * 
*       * 
    
n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print() 
o/p:
enter the value:5
* * * * * 
    *     
    *     
    *     
* * * * * 
      
n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == m or (i == n-1 and j <m) or (j == 0 and i >= m):
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()                    
o/p:
enter the value:5
* * * * * 
    *     
*   *     
*   *     
* * *       
 
n = int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()     
o/p:
enter the value:5
* * * * * 
      *   
    *     
  *       
* * * * *   

n = int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
           print("*",end =" ")
        else:
            print(" ",end =" ")
    print()        
o/p:
enter the value:5
*       * 
  *   *   
    *     
  *   *   
*       * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j == n-1 or (i==j and i <= m):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()            
o/p:
enter the value:5
*       * 
  *   *   
    *     
  *       
*         

n = int(input("entert the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or ( i==m and j <= m ) or (i+j == n-1 and i <= m ) or (i == j and i >= m):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()  
o/p:
entert the value:5
*       * 
*     *   
* * *     
*     *   
*       * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i >= m) or (i+j == n-1 and j <= m): 
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print() 
o/p:
enter the value:5
*       * 
*       * 
*   *   * 
* *   * * 
*       * 

n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= m) or (i+j == n-1 and j >= m): 
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print() 
o/p:
enter the value:5
*       * 
* *   * * 
*   *   * 
*       * 
*       * 
'''
n = int(input("enter the value:"))
m = n//2
for i in range(n):
    for j in range(n):
        if (j == 0 and i <= m) or (j == n-1 and i <= m) or (i-j == m) or (i+j == n+m -1) : 
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print() 