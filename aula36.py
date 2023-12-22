import json

carros_json = '{"marca":"honda", "modelo":"HrV", "cor":"prata"}'

carros = json.loads(carros_json)

print(carros)

print(carros["marca"])
print(carros["modelo"])

for key in carros:
    print(key)

for value in carros.values():
    print(value)

for key, value in carros.items():
    print(key, value)


pessoa = {"nome": "Marcos", 
          "idade": 31, 
          "peso": 105, 
          "altura": 1.83}

pessoa_json=json.dumps(pessoa)

print(pessoa_json)
