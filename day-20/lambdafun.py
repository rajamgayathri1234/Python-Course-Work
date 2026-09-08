'''
var = lambda arg: exp

wish = lambda name: f'Welcome to the course {name}'
print(wish("gayathri"))
print(wish("prasanna"))

gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(3,4,5))
print(avg(23,56,42))

iseven = lambda a: "evev" if a%2==0 else "Odd"
print(iseven(10))
print(iseven(53))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(5,8,2))
print(largest(6,3,8))

isvowel = lambda a:"Vowel" if a in 'aeiouAEIOU' else "Cons"
print(isvowel('u'))
print(isvowel('k'))

#update the every value in list
l = [1,2,3,4,5,6,7]
update = list(map(lambda i: i+10,l))
print(update)

#adding the discount in list of integers
t = (789,234,890,908,987,678)
discount = list(map(lambda i: i-i*0.3,t))
print(discount)

#access only odd  numbers
l = [1,2,3,4,5,6,7]
update = list(filter(lambda i: i%2!=0,l))
print(update)

t =(456,7890,2345,65432,123,678)
discount = list(filter(lambda i: i>1000,t))
print(discount)

l = ['sowmya@codegnan.com','sowmya@yahoo.com','sowmya@gmail.com','sowmya@outlook']
res = list(map(lambda i: i.split('@')[-1],l))
print(res)

from functools import reduce

l = [4,5,2,76,4,5,987,567,90,12]

res = reduce(lambda sum,i: sum+i,l)
print(res)

res1 = reduce(lambda pro,i: pro*i,l)
print(res1)
'''
seats = {'s1':True,
         's2':False,
         's3':False,
         's4':False,
         's5':True,
         's6':True
        }
aval = list(filter(lambda i: seats[i]!=True,seats))
print(aval)

products ={
    'eggs':80,
    'sugur':60,
    'salt':20,
    'butter':40,
    'milk':30
}
res = list(filter(lambda i: products[i]>50,products))
print(res)

products ={
    'eggs':80,
    'sugur':60,
    'salt':20,
    'butter':40,
    'milk':30
}
print(dict(sorted(products.items(),key= lambda i:i[1])))
print(dict(sorted(products.items(),key= lambda i:i[1],reverse=True)))
