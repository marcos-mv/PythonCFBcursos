def subtrair1(num):
    res = 0
    
    for i in num:
        res -= i
    return res
    
lista = [1,2,5,8,33]

def valores (n):
    for i in n:
        print(i)
        
valores(lista)

print("Subtração: " + str(subtrair1(lista)))