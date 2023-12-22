# num = -10

# num = 2

num = True


if type(num) is not int:
    raise Exception("Valor Não permitido")

# if num < 1:
#     raise Exception("Valor Não permitido")



try:
    print(num)
# except NameError:
#     print("Variavel não Inicializada")
except:
    print("Erro desconhecido")
    
else:
    print("Programa Ok!")
    
finally:
    print("Fim do tratamento")
