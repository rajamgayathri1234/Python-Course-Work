Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 5
>>> b = 25.1
>>> c = 'codegnan'
>>> print(a,b,c)
5 25.1 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 5 b= 25.1 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=5b=25.1c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep=\n)
SyntaxError: unexpected character after line continuation character
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
5
b=
25.1
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	5	b=	25.1	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='\n\n')
a=	5	b=	25.1	c=	codegnan

>>> print(f'a={a} b={b} c={c}')
a=5 b=25.1 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=5 b=25.100000 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=5 b=25.1 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=25.1 b=codegnan c=5
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=5 b=25.1 c=codegnan
>>> print('a={1} b={0} c={2}'.format(a,b,c))
a=25.1 b=5 c=codegnan
