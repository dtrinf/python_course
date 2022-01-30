

from tkinter import SE


class Serie():

    def __init__(self, titulo = '', numero_temporadas = 3, entregado = False, genero = '', creador = ''):
        self.__titulo = titulo
        self.__numero_temporadas = numero_temporadas
        self.__entregado = entregado
        self.__genero = genero
        self.__creador = creador

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
        return f"Titulo: {self.__titulo}\nNumero de temporadas: {self.__numero_temporadas}\nEntregado: {self.__entregado}\nGenero: {self.__genero}\nCreador: {self.__creador}"


class Videojuego():
    
    def __init__(self, titulo = "", horas_estimadas = 10, entregado = False, genero = "", company = "") -> None:
        self.__titulo = titulo
        self.__horas_estimadas = horas_estimadas
        self.__entregado = entregado
        self.__genero = genero
        self.__company = company

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
        return f"Titulo: {self.__titulo}\nNumero de horas estimadas de juego: {self.__horas_estimadas}\nEntregado: {self.__entregado}\nGenero: {self.__genero}\nCompañia: {self.__company}"


class Entregable(Serie, Videojuego):

    def __init__(self, titulo='', numero_temporadas=3, entregado=False, genero='', creador='', horas_estimadas = 10, company = ''):
        Serie.__init__(self,titulo, numero_temporadas, entregado, genero, creador)
        Videojuego.__init__(self, titulo, horas_estimadas, entregado, genero, company)

    def entregar(self):
        self.__entregado = True

    def devolver(self):
        self.__entregado = False
    
    def isEntregado(self):
        return self.__entregado

    def compareTo(self, a):
        # if isinstance(a,Videojuego):
        if self.company != '' and a.company != '':
            diferencia_horas = self.horas_estimadas - a.horas_estimadas
            if diferencia_horas >= 0:
                print(f"El otro juego tiene {diferencia_horas} horas menos de juego")
            else:
                print(f"El otro juego tiene {diferencia_horas*-1} horas mas de juego")
        elif self.creador != '' and a.creador != '':
            diferencia_temporadas = self.numero_temporadas - a.numero_temporadas
            if diferencia_temporadas >= 0:
                print(f"La otra serie tiene {diferencia_temporadas} temporadas menos ")
            else:
                print(f"La otra serie tiene {diferencia_temporadas*-1} temporadas mas")
        else:
            print("Estas comparando series y peliculas, no es una comparacion valida")

    def __str__(self) -> str:
        if self.company != '':
            return Videojuego.__str__(self)
        return Serie.__str__(self)


serie = Serie("Salvados", 7, True, "Misterio", "XX")
# print(serie.titulo)
# print(serie)

juego1 = Videojuego("Carmagedon", 500, False, "Coches", "XX")

# juego1.compareTo(juego2)
# juego1.compareTo(juego3)

entregable1 = Entregable(titulo="Salvados", numero_temporadas=7, entregado=True, genero="Misterio", creador="XX")
entregable2 = Entregable(titulo="Fringe", numero_temporadas=8, entregado=True, genero="Misterio", creador="XX")
entregable3 = Entregable(titulo="Carmagedon", horas_estimadas=500, entregado=False, genero="Coches", company="XX")
entregable4 = Entregable(titulo="Carmagedon2", horas_estimadas=400, entregado=False, genero="Coches", company="XX")


print(entregable1)
print("---------------")
print(entregable2)
print("---------------")
entregable1.compareTo(entregable2)
print("---------------")
entregable3.compareTo(entregable4)
print("---------------")
entregable3.compareTo(entregable2)



if __name__ == "__main__":

    peliculas = []
    videojuegos = []

    for i in range(5):
        peliculas.append(Serie(f"Serie {i}", 7+i, True, "Misterio", "XX"))
        videojuegos.append(Videojuego(f"Juego {i}", 500+i, False, "Coches", "XX"))
    
    
    
    