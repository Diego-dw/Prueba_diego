class Libro:
    def __init__(self, id, titulo, paginas):
        self.__id = id
        self.__titulo = titulo
        self.__paginas = paginas
        self.lista = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id_nuevo):
        self.__id = id_nuevo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self,titulo_nuevo):
        self.__titulo = titulo_nuevo

    @property
    def paginas(self):
        return self.__paginas

    @paginas.setter
    def paginas(self,paginas_nuevo):
        self.__paginas = paginas_nuevo

    def clasificacion (self):
        if self.paginas < 100:
            return "corto"
        elif self.paginas >= 100 and self.paginas <= 300:
            return "mediano"
        else:
            return "largo"


    def imprimir(self):
     
        print(f"id: {self.id}")
        print(f"titulo: {self.titulo}")
        print(f"paginas: {self.paginas}")
        print(f"clasificacion: {self.clasificacion()}")

class Biblioteca:
    def __init__(self, id_biblioteca, nombre, costo_prestamo):
        self.__id_biblioteca = id_biblioteca
        self.__nombre = nombre
        self.__costo_prestamo = costo_prestamo
        self.lista_libros = [] 

    @property
    def id_biblioteca (self):
        return self.__id_biblioteca
    
    @id_biblioteca.setter
    def id_biblioteca (self, nuevo_id):
        self.__id_biblioteca = nuevo_id

    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def costo_prestamo (self):
        return self.__costo_prestamo
    
    @costo_prestamo.setter
    def costo_prestamo (self, nuevo_costo):
        self.__costo_prestamo = nuevo_costo

    def agregar_libro (self, libro):
        self.lista_libros.append(libro)
    
    def reporte_libros(self):
        print("Reporte de biblioteca!")
        print(f"biblioteca: {self.__nombre}")
        print(f"total de libros: {len(self.lista_libros)}")
        print(" ")
        
        for libro in self.lista_libros:
            print(f"{libro.titulo}, paginas: {libro.paginas}\n")


    def ganancia (self):
        total = 0

        for libro in self.lista_libros:
            if libro.paginas <= 100:
                costo = self.__costo_prestamo * 0.90
            else:
                costo = self.__costo_prestamo

            total += costo

            archivo = open("lista_libros.txt","w")
            archivo.write(f"Ganancia del prestamo de libros: {total}")
            archivo.close()

            print("Ganancias guardadas en el archivo: lista de libros! ")
            return total



libro1 = Libro(2, "jujutsu Kaisen", 100)
libro2 = Libro(3, "Blue lock", 100)

biblioteca1 = Biblioteca(5,"karina library",2000)

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

libro1.imprimir()
print(" ")
libro2.imprimir()
print(" ")

biblioteca1.reporte_libros()

biblioteca1.ganancia()