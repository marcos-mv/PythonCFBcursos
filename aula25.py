class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome: " + self.nome)
        print("Time: " + str(self.time))
        print("Forca: " + str(self.forca))
        print("Municao: " + str(self.municao))
        print("Estado: " + ("Vivo" if self.vivo else "Morto"))
        print("Energia: " + str(self.energia)+" \n")


class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200

        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):

    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20

        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC):

    def __init__(self, nome, time):
        self.forca = 500
        self.municao = 300
        super().__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super().info()


s1 = Guarda("Mario", 1)
s2 = Elite("Maria", 1)
s3 = Soldado("Paulo", 2)
s4 = Soldado("Fafael", 2)
s5 = Elite("Fernando", 1)
s6 = Guarda("Neto", 2)

s1.vivo = False
s1.energia = 5500

s1.info()
s2.inf()
s3.info()
s4.info()
s5.inf()
s6.info()
