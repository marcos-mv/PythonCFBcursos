name = "aula44.txt"

file = open("/home/marcos/Desktop/Python/"+name,"at")

# r - read - leitura

# a - append - anexar

# w - write - escrita

# x - create - criar

# t - text 

# b - binary

txt = input("Write a text: ")

file.write(txt+"\n")

# file.write("Hello Marcos, How are you?\n")
# file.write("I am fine, and you?")

file.close()



