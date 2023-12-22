texto = "Curso de Python "

palavra = "python"

valor = palavra in texto.lower()

print(valor)


nome = "marcos"

sobrenome = "Vinicius"

completo = nome.upper()+" "+sobrenome

print(completo)


curso = "Python 2023"

print(curso.strip())

print(curso.lower())

print(curso.upper())

print(curso.replace("Python", "Matemática"))

a = curso.split(' ')
print(a)
print("Split:" + a[1])

print(curso)

print(curso[2])

print(curso[0:7])

print(curso[5:10])

print("Tamanho: " + str(len(curso)))

resposta = "Curso" in curso

print(resposta)

resposta2 = "Curso" not in curso

print(resposta2)


dia=18
mes="Novembro"
ano=2023
cidade="Brasília"

cor= "Vermelho"

data = "{}, {} de {} de {}\n \"{}\""

print(data.format(cidade,dia,mes,ano,cor))
