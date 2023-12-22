

carros=["Uno","Gol","Strada","Fox"]
carros2= ["Polo", "Fusca", "Palio", "Celta"]

carros3= carros+carros2

print(carros3)




carros[3]= "CrossFox"

print(carros)

print(carros[0])

print(carros[-1])

carros.append("City")
carros.append("Compass")

print(carros)

print(str(len(carros)))

carros.remove("Uno")

print(carros)

carros.pop() #remove last value from the list

print(carros)

del carros[2] #removes the value according to the index

print(carros)



carros.clear() #delete all values from the list

print(carros)

print(carros2)

