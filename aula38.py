import json

{"nome": "Bruno",
 "time": "aviador",
 "vivo": "True",
 "energia": 100,
 "mochila": ["corda", "linha", "arame", "escada"],
 "aeronaves": [
     {"tipo": "transporte", "habilidade": 80},
     {"tipo": "ataque", "habilidade": 100},
     {"tipo": "reconhecimento", "habilidade": 50},
     {"tipo": "defesa", "habilidade": 30}
 ]
 }

jogador_json = '{"nome": "Bruno", "time": "aviador", "vivo": "True", "energia": 100, "mochila": ["corda", "linha", "arame", "escada"], "aeronaves": [ {"tipo": "transporte", "habilidade": 80}, {"tipo": "ataque", "habilidade": 100}, {"tipo": "reconhecimento", "habilidade": 50}, {"tipo": "defesa", "habilidade": 30} ] }'


jogador = json.loads(jogador_json)

# for key in jogador:
#     print(key)
    
# for value in jogador.values():
#     print(value)
    
for key, value in jogador.items():
    print(key,value)
    
print(jogador["nome"])

#itens da mochila

for itens in jogador["mochila"]:
    print(itens)
    
# aeronaves

for a in jogador["aeronaves"]:
    print(a)
    
for a in jogador["aeronaves"]:
    print(a["tipo"] + str(a["habilidade"]))
    
