import sys

class Entrada:
    def __init__(self, entrada_id, pelicula_id, funcion, cantidad):
        self.entrada_id = entrada_id
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
	instancia = None
	def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
		
    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = Singleton()
        return cls.instancia
		
    

        
class Funcion:
    def _init__(self, id, hora, minuto):
        self.id = id
        self.hora = hora
        self.minuto = minuto

        def ingresar_Funcion(self, funcion):
            self.funciones[funcion.id]= funcion
            

class Cine:
    def __init__(self):
        self.lista_peliculas = {}
        
        def listar_peliculas(self):
            return self.lista_peliculas

        def listar_funciones(self, pelicula_id):
            return self.lista_peliculas[int(pelicula_id)].funciones      

        def guardar_entrada(self, Entrada):
            return self.listar_entradas(entrada.pelicula_id, entrada.funcion_id)

			
class CineFactory:

	def Escoger_Cine(self, tipo_Cine):
		if tipo_Cine  == '1':
			return CinePlaneta()
		else:
			return CineStark()


class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula.get_instance
        peliculaHF = Pelicula.get_instance
        peliculaD = Pelicula.get_instance
        peliculaDeep = Pelicula.get_instance
		
		peliculaIT.id = 1
		peliculaIT.nombre = 'IT'
		peliculaHF.id = 2
		peliculaHF.nombre = 'La hora Final'
		peliculaD.id = 3
		peliculaD.nombre = 'Desaparecido'
		peliculaDeep.id = 4
		peliculaDeep.nombre = 'Deep el pulpo'

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    



class CineStark:
    def __init__(self):
        peliculaD = Pelicula.get_instance
        peliculaDeep = Pelicula.get_instance
		
		peliculaD.id = 1
		peliculaD.nombre = 'Desparecido'
		peliculaDeep.id = 2
		peliculaDeep.nombre = 'Deep El Pulpo'

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


class opcion_Principal:
			def obtener_opcion(self):
			print('Ingrese la opción que desea realizar')
			print('(1) Listar cines')
			print('(2) Listar cartelera')
			print('(3) Comprar entrada')
			print('(0) Salir')

class opcion_Uno:
			def obtener_opcion(self):
			print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
  
 class opcion_Dos:
			def obtener_opcion(self):
			print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
  
 class opcion_Tres:
			def obtener_opcion(self):
			print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
			
			
class OpcionFactory:

	def obtener_opcion(self, opcion):
		if opcion  == '1':
			return opcion_Uno()
		elif opcion == '2':
			return opcion_Dos()	
		elif opcion == '3':
			return opcion_Tres()
		else
			return opcion_Principal()

def main():
    terminado = False;
	
	cinefactory = CineFactory()
	
	opcionfactory = OpcionFactory()
	
    while not terminado:
        
		opcion = opcionfactory.obtener_opcion()
		
		opcion.obtener_opcion()
		
		opcion = input('Primero elija una opcion:')
		
		if opcion == '1':
			opcion = opcionfactory.obtener_opcion()
			opcion.obtener_opcion()
			
		elif opcion == '2':
			opcion = opcionfactory.obtener_opcion()
			opcion.obtener_opcion()
		
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')

        elif opcion == '3':
			opcion = opcionfactory.obtener_opcion()
			opcion.obtener_opcion()
		
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            
            #pelicula = obtener_pelicula(id_pelicula)
            
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
				
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        
		elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()
