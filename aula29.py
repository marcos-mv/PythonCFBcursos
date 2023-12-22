carros = ["Polo", "Gol", "Uno", "Jetta", "Fox", "Sentra"]

# for i in carros:
#     print (i)
    
itCarros = iter(carros)

while itCarros:
    try: 
        print(next(itCarros))
    except StopIteration:
        break
    
    
# i = 0

# while i < len(carros):
#     print(carros[i])
#     i += 1