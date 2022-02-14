

from tkinter import SE


class Entregable():

    def __init__(self, entregado):
        self.__entregado = entregado

    def entregar(self):
        self.__entregado = True

    def devolver(self):
        self.__entregado = False
    
    def isEntregado(self):
        return self.__entregado

    def compareTo(self, a):
        pass

    def __str__(self) -> str:
        pass


class Serie(Entregable):

    def __init__(self, titulo = '', numero_temporadas = 3, entregado = False, genero = '', creador = ''):
        self.__titulo = titulo
        self.__numero_temporadas = numero_temporadas
        self.__genero = genero
        self.__creador = creador
        Entregable.__init__(self, entregado)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def numero_temporadas(self):
        return self.__numero_temporadas

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @numero_temporadas.setter
    def numero_temporadas(self, num):
        self.__numero_temporadas = num

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @creador.setter
    def creador(self, creador):
        self.__creador = creador

    def __str__(self) -> str:
        return f"Titulo: {self.__titulo}\nNumero de temporadas: {self.__numero_temporadas}\nEntregado: {self.isEntregado()}\nGenero: {self.__genero}\nCreador: {self.__creador}"

    def compareTo(self, a):
        diferencia_temporadas = self.__numero_temporadas - a.__numero_temporadas
        if diferencia_temporadas >= 0:
            print(f"La otra serie tiene {diferencia_temporadas} temporadas menos ")
        else:
            print(f"La otra serie tiene {diferencia_temporadas*-1} temporadas mas")



class Videojuego(Entregable):
    
    def __init__(self, titulo = "", horas_estimadas = 10, entregado = False, genero = "", company = "") -> None:
        self.__titulo = titulo
        self.__horas_estimadas = horas_estimadas
        self.__genero = genero
        self.__company = company
        Entregable.__init__(self, entregado)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas_estimadas(self):
        return self.__horas_estimadas

    @property
    def genero(self):
        return self.__genero

    @property
    def company(self):
        return self.__company

    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @horas_estimadas.setter
    def horas_estimadas(self, horas_estimadas):
        self.__horas_estimadas = horas_estimadas

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @company.setter
    def company(self, company):
        self.__company = company

    def __str__(self) -> str:
        return f"Titulo: {self.__titulo}\nNumero de horas estimadas de juego: {self.__horas_estimadas}\nEntregado: {self.isEntregado()}\nGenero: {self.__genero}\nCompañia: {self.__company}"

    def compareTo(self, a):
        diferencia_horas = self.__horas_estimadas - a.__horas_estimadas
        if diferencia_horas >= 0:
            print(f"El otro juego tiene {diferencia_horas} horas menos de juego")
        else:
            print(f"El otro juego tiene {diferencia_horas*-1} horas mas de juego")



# serie = Serie("Salvados", 7, True, "Misterio", "XX")
# # print(serie.titulo)
# # print(serie)

# juego1 = Videojuego("Carmagedon", 500, False, "Coches", "XX")

# # juego1.compareTo(juego2)
# # juego1.compareTo(juego3)

serie1 = Serie(titulo="Salvados", numero_temporadas=7, entregado=True, genero="Misterio", creador="XX")
serie2 = Serie(titulo="Fringe", numero_temporadas=8, entregado=True, genero="Misterio", creador="XX")
videjuego1 = Videojuego(titulo="Carmagedon", horas_estimadas=500, entregado=False, genero="Coches", company="XX")
videjuego2 = Videojuego(titulo="Carmagedon2", horas_estimadas=400, entregado=False, genero="Coches", company="XX")


# print(serie1)
# print("---------------")
# print(serie2)
# print("---------------")
# serie1.compareTo(serie2)
# print("---------------")
# videjuego1.compareTo(videjuego2)

# print(serie1)
# print(serie1.entregar())
# print(serie1.isEntregado())
# print(serie1.devolver())
# print(serie1.isEntregado())

# print(videjuego1)
# print(videjuego1.entregar())
# print(videjuego1.isEntregado())
# print(videjuego1.devolver())
# print(videjuego1.isEntregado())


if __name__ == "__main__":

    series = []
    videojuegos = []

    # Data inizialization
    for i in range(5):
        series.append(Serie(f"Serie {i}", 7+i, False, "Misterio", "XX"))
        videojuegos.append(Videojuego(f"Juego {i}", 500+i, False, "Coches", "XX"))
    
    # Deliver some series and games
    for i in range(len(series)):
        if i%2 == 0:
            series[i].entregar()

    for i in range(len(videojuegos)):
        if i%2 == 0:
            videojuegos[i].entregar()
    
    # Count delivered series and games
    delivered_series = 0
    delivered_games = 0

    for i in range(len(series)):
        if series[i].isEntregado():
            delivered_series += 1
            

    for i in range(len(videojuegos)):
        if videojuegos[i].isEntregado():
            delivered_games += 1

    print(f"Se han entregado {delivered_series} series y {delivered_games} videojuegos")

    # Search longest game and serie
    longest_serie = series[0]
    longest_game = videojuegos[0]

    for i in range(len(series)):
        if series[i].numero_temporadas > longest_serie.numero_temporadas:
            longest_serie = series[i]
            

    for i in range(len(videojuegos)):
        if videojuegos[i].horas_estimadas > longest_game.horas_estimadas:
            longest_game = videojuegos[i]

    print(f"El videojuego mas largo es {longest_game}")
    print(f"La serie con mas capitulos es {longest_serie}")


    