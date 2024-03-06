

class Colaborador:
    def __init__(self, Nombre, Codigo, Pin):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Pin = Pin
        ##pass


class Marcas:
    def __init__(self, Empleado, Codigo, Pin) -> None:
        self.RegistroHoras = {}
        
    def marcar(self, empleado, codigo, pin, tipo):
        if empleado.codigo == codigo and empleado.pin == pin:
            if tipo == "E":
                #######
                pass
            elif tipo == "S":
                #######
                pass
            else:
                print("Tipo de marca inválido. Debe ser 'entrada' o 'salida'.")
        else:
            print("Código o pin incorrectos.")

class Planilla:
    def __init__ (self):
        self.HorasTrabajadas = {}
        #agrega las horas trabajadas
    def AgregarHoras(self, dia, HorasTrabajadas):
        self.HorasTrabajadas[dia] = HorasTrabajadas
        ##pass
        #genera los datos de planilla general



    def GenerarPlanilla(self):

        ####Verificar que se registren marcas
        if not self.MarcasRegistradas: 
            print("Por favor, registre las marcas para acceder")
            return 
        
        ##Muestra los días y horas trabajados
        for dia, horas in self.HorasTrabajadas.items():
            print(f"Día {dia}: {horas} horas trabajadas")
    
##################################################
##################################################
##################################################
#Definición de menú y sus opciones
def Menu(self):

        while True:
            print("\nMenu: ")
            print("1. Marcas")
            print("2. Generar planilla")
            print("3. Reporte de planilla")
            print("4. Leer reporte de planilla")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Llama a un método que maneje las marcas
                #self.manejar_marcas()
                 print("Bienvenido")
                 Codigo = input("Ingrese su código: ")
                 Pin = input("Ingrese su PIN: ")
                 ###tipo = input("¿Es una marca de entrada o salida? (E/S): ")
                 
                 ###opcion = Menu()
                 #variable booleana para verificar la exitencia del empleado
                 Colaborador_Existe: False
                 #for Colaborador in ListaColaboradores:
                     ####verifica que el codigo del empleado y el pin existan en el sistema
                     #if Colaborador.Codigo == Codigo and Colaborador.Pin == Pin
                     #Colaborador_Existe = True
                     #break
                 
                  if Colaborador_Existe:
                  tipo = input("¿Es una marca de entrada o salida (E/S)?")
                     
            elif opcion == "2":
                # Llama a un método que genere la planilla
                self.generar_planilla()
            elif opcion == "3":
                # Llama a un método que genere el reporte de la planilla
                self.generar_reporte_planilla()
            elif opcion == "4":
                # Llama a un método que lea el reporte de la planilla
                self.leer_reporte_planilla()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")