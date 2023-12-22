import json

airplane_dictionary = {
    "marca": "Embraer",
    "modelo": "E2",
    "cor": "azul"
}

#dictionary -> objeto json

planes_list = ["Boeing", "Airbus", "Bombardier", "Embraer", "Cesna"]

#list -> array json

planes_tuple = ("Boeing", "Airbus", "Bombardier", "Embraer", "Cesna")

#tupla -> array json

airplane_j= json.dumps(airplane_dictionary,indent=4,separators=(":","="),sort_keys=True)

print(airplane_j)

planes_j= json.dumps(planes_list, indent=4)

print(planes_j)

planesT_j= json.dumps(planes_tuple)

print(planesT_j)


