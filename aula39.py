import json

with open('/home/marcos/Desktop/Python/jogador.json') as f:
    jogador= json.load(f)
    
for key, value in jogador.items():
    print(key,value)
    

    
for a in jogador["aeronaves"]:
    print(a["tipo"] + " --- "+ str(a["habilidade"]))