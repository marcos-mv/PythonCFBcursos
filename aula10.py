a = False

if a:
    print("Marcos")


b = 5
c = 9

op="*"

res = 0

if b < c:
    print("Menor")

print("Fim do Programa")

if op == "+":
    res = b+c
    
if op == "-":
    res = b-c

if op == "*":
    res = b*c
    
if op == "/":
    res = b+c

print("Operação: " + op + " = ",res)
