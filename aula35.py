import datetime

hoje = datetime.datetime.now()

nasc = datetime.datetime(1992,12,8)

nasc2 = datetime.datetime(1961,7,20)

print(nasc2.strftime("%A"))

print(hoje)

print(str(hoje.day) + "/" + str(hoje.month) +"/"+ str(hoje.year))

print(nasc.strftime("%A"))

# %a // texto dia da semana abreviado
# %A // texto dia da semana
# %w // dia da semana
# %d // dia do mes
# %b // texto mes abreviado
# %B // texto mes
# %m // numero do mes
# %y // Ano com dois digitos
# %Y // Ano com 4 dígitos
# %H // hora com 2 dígitos 00-23
# %I // 00-12
# %p // AM - PM
# %M minutos

