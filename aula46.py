import re
import os
import time

name = "aula46.txt"

directory = "/home/marcos/Desktop/Python/"

if os.path.exists(directory+name):
    print("Arquivo Existente") 
else : 
    file = open(directory+name,"x")
    print("Arquivo Criado.")

# r - read - leitura

# a - append - anexar

# w - write - escrita

# x - create - criar

# t - text 

# b - binary

# print(file.read())


# for l in file:
#     print(l)

file.close()


time.sleep(5)

os.remove(directory+name)

print("Arquivo Excluído")




