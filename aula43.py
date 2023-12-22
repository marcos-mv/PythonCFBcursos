import re

txt = "Curso de Python do CFB Cursos, canal do youtube"

res = re.sub(" ","-",txt)

res = re.sub(",",".",res)

print(res)

# for t in res:
#     print(t)