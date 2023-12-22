import re

txt = "Curso de Python do CFB Cursos, canal do youtube"

# res = re.search("Curso",txt)

search = input("Find on txt: ")

res = re.search(search,txt)

if res != None:
    pi = res.start()
    pf= res.end()

    tam = pf-pi

    print(tam)
    print(res.start())
    print(res.end())
else :
     print("Palavra não encontrada.")
    
