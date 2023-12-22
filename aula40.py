import re

txt = "Curso de Python do CFB Cursos, canal do youtube"

# res = re.findall("o",txt)

search = input("Find on txt: ")

res = re.findall(search,txt)



print(res)

print("Number of ocurrences:  " + str(len(res)))


for t in res:
    print(t)