import re

txt = "Curso de Python do CFB Cursos, canal do youtube"

res = re.split("\s",txt)

print(res)

print(res[2])

for t in res:
    print(t)