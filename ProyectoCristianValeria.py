

class Colaborador:
    def __init__(self, Nombre, Codigo, Pin):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Pin = Pin
        ##pass


class Marcas:
    def __init__(self, Empleado, Codigo, Pin) -> None:
        self.RegistroHoras = {}
        
    def Marcar(self, empleado, codigo, pin, tipo):
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
    def __init__(self):
        self.HorasTrabajadas = {}
        self.MarcasRegistradas = False  # Atributo para rastrear si se han registrado marcas

    def AgregarHoras(self, dia, horastrabajadas):
        self.HorasTrabajadas[dia] = horastrabajadas

    def GenerarPlanilla(self):
        if not self.MarcasRegistradas:  # Verifica si se han registrado marcas antes de generar la planilla
            print("Por favor, ingrese sus marcas.")
            return
        
        for dia, horas in self.HorasTrabajadas.items():
            print(f"Día {dia}: {horas} horas trabajadas")

    def MarcasRegistradas(self):
        self.MarcasRegistradas = True

    def GenerarReportePlanilla():
        pass

    def LeerReportePlanilla():
        pass
        
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
                 print("Bienvenido/a")
                 Codigo = input("Ingrese su código: ")
                 Pin = input("Ingrese su PIN: ")
                 
                 
                 ###opcion = Menu()
                 #variable booleana para verificar la exitencia del empleado
                 #Colaborador_Existe: False
                 #for Colaborador in ListaColaboradores:
                     ####verifica que el codigo del empleado y el pin existan en el sistema
                     #if Colaborador.Codigo == Codigo and Colaborador.Pin == Pin
                     #Colaborador_Existe = True
                     #break
                 
                  #if Colaborador_Existe:
                  #Tipo = input("¿Es una marca de entrada o salida (E/S)?")
                   #  self.marcas.marcar(Codigo, Pin, Tipo)
                    # self.Planilla.MarcasRegistradas()
                 #else 
                  #   print("Por favor, ingrese sus marcas")
                 
            elif opcion == "2":
                # # Llama a un método que genere la planilla
                # if not self.Planilla.MarcasRegistradas:  # Verifica si se han registrado marcas antes de generar la planilla
                #  print("Error: Debes registrar las marcas primero.")
                # else:
                # self.GenerarPlanilla()
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
