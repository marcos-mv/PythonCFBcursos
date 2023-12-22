pessoas = {
    "Maria": {
        "Nome": "Maria rodrigues",
        "Idade": 55
    },
    "Jose": {
        "Nome": "Jose da Silva",
        "Idade": 88
    },
    "Felipe": {
        "Nome": "Felipe Macedo",
        "Idade": "10"
    }
}

print(pessoas["Felipe"]["Nome"], pessoas["Felipe"]["Idade"])


Maria = {
    "Nome": "Maria rodrigues",
    "Idade": 55
}
Jose = {
    "Nome": "Jose da Silva",
    "Idade": 88
}
Felipe = {
    "Nome": "Felipe Macedo",
    "Idade": "10"
}

pessoas = {
    "pessoa1": Maria,
    "pessoa2": Jose,
    "pessoa3": Felipe
}


print(pessoas["pessoa1"]["Nome"])
