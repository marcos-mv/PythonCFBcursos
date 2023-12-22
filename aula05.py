import random
num_i = 10
num_f = 85.52
num_c = 5j

x = num_i
y = num_f
z = num_c

a = int(num_f)

print(a)

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
print("Valor: " + str(y) + " - Tipo: " + str(type(y)))
print("Valor: " + str(z) + " - Tipo: " + str(type(z)))

num_r=random.randrange(0,59)

lista_randomica=[random.randrange(0,10),
                 random.randrange(0,10),
                 random.randrange(0,10),
                 random.randrange(0,10),
                 random.randrange(0,10),
                 random.randrange(0,10),                 
                 ]

print(lista_randomica)

print(num_r)