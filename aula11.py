a = False

if a:
    print("Marcos")


b = 5
c = 9

op = "&"

res = 0

if b < c:
    print("Menor")

print("Fim do Programa")

if op == "+":
    res = b+c

elif op == "-":
    res = b-c

elif op == "*":
    res = b*c

elif op == "/":
    res = b+c
else:
    print("Operador Inválido")

print("Operação: " + op + " = ", res)


clima = "sol"
lugar = ""
dinheiro=500


if clima == 'sol' or (dinheiro >= 300 and dinheiro <= 600):
    lugar="clube"
else:
    lugar = "cinema"
    
print("Vou ao "+lugar)
