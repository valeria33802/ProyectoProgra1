

class Colaborador:
    def __init__(self, Nombre, Codigo, Pin):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Pin = Pin
        ##pass


class Marcas:
    def __init__(self, Empleado, Codigo, Pin) -> None:
        self.RegistroHoras = {}
        
    def Marcar(self, Tipo):
        pass
        #ESTE CODIGO MUY PROBABLEMENTE NO LO USEMOS PORQUE LA VALIDACION DEL PIN Y CODIGO ESTÁ EN EL MENÚ
        # if Empleado.Codigo == Codigo and Empleado.Pin == Pin:
        if Tipo == "E":
                 #######
                pass
        elif Tipo == "S":
                 #######
                 pass
        #     else:
        #         print("Por favor intente de nuevo")
        else:
        #     print("Código o pin incorrectos.")
            pass

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
        
    def CargarHoras():
        pass

    def CalcularSalarioBruto():
        pass

    def CalcularDeduccion():
        pass

    def GenerarPlanilla():
        pass

    def ImprimirMatriz():
        pass

    def ReportePlanilla():
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
            Opcion = input("Seleccione una opción: ")

            if Opcion == "1":
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
                 
            elif Opcion == "2":
                # # Llama a un método que genere la planilla
                # if not self.Planilla.MarcasRegistradas:  # Verifica si se han registrado marcas antes de generar la planilla
                #  print("Error: Debes registrar las marcas primero.")
                # else:
                # self.GenerarPlanilla()
                pass
            elif Opcion == "3":
                if not self.Planilla.self.GenerarPlanilla():  # Verifica si se ha generado planilla antes de hacer el reporte
                #  print("Error: Debes registrar las marcas primero.")
                # else:
                # self.GenerarPlanilla()
                # Llama a un método que genere el reporte de la planilla
                    self.GenerarPlanilla()
            elif Opcion == "4":
                # Llama a un método que lea el reporte de la planilla
                self.LeerReportePlanilla()
            elif Opcion == "5":
                break
            else:
                print("Opción inválida.")
