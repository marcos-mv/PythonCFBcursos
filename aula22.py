soma = lambda a,b:a+b

mult = lambda a,b,c:soma(a,b)*c

m = mult(10,2,3)

r= soma(2,5)

print(r)

print(m)

print((lambda a,b:a-b)(5,8))

x = lambda x,func:x+func(x)

y= x(4,lambda x:x*x)

print(y)

