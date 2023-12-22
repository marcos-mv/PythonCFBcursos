import urllib.request

page = urllib.request.urlopen("https://www.pelando.com.br/")


texto = page.read().decode("utf8")

produto_pos_ini = texto.find("Pelando")

preco = texto[231:260]

print(produto_pos_ini)

print(preco)