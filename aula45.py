import re

name = "aula45.txt"

file = open("/home/marcos/Desktop/Python/"+name,"rt")

# r - read - leitura

# a - append - anexar

# w - write - escrita

# x - create - criar

# t - text 

# b - binary

# print(file.read())


# for l in file:
#     print(l)
    

resp = file.readline()

print(resp)

res = re.sub(" ","-",file.readline())

print(res)

file = open("/home/marcos/Desktop/Python/"+name,"wt")

file.write(res)



file.close()



