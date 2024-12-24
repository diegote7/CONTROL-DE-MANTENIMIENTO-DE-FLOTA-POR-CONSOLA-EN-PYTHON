from database import Database
import pandas as pd
import numpy as np

class Menu:
    def __init__(self, db):
        self.db = db


    def ejecutar(self):
        """
# ----------------------------------------------------------------
# Metodo que muestra el menu en consola y espera el ingreso de 
# un valor del menu para # llamar al metodo correspondiente.
# En caso de no haber coincidencia con ninguno, 
# imprime un mensaje de error y aguarda nuevo ingreso.
# ----------------------------------------------------------------
        """  
        

        self.alerta_mantenimiento()      
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.mostrar_altas()
            elif opcion == '2':
                self.mostrar_bajas()
            elif opcion == '3':
                self.programar_actividad()
            elif opcion == '4':
                self.historial_maquina()
            elif opcion == '5':
                self.historial_operario()
            elif opcion == '6':
                self.informe_almacen()
            elif opcion == '7':
                self.carga_horas_diarias()
            elif opcion == '8':
                self.ver_estadisticas_uso()
            elif opcion == '9':
                self.salir()
                break
            else:
                print("Opción no válida. Por favor, seleccione nuevamente.")


    def mostrar_menu(self):
        """
# -----------------------------------
# Despliega el menu de opciones
# -----------------------------------
        """       
        print("\nMenú de opciones:")
        print("1. Ingresar Submenu Altas")
        print("2. Ingresar Submenu Bajas")
        print("3. Programar Actividad")
        print("4. Historial Maquina")
        print("5. Historial Operario")
        print("6. Informe Almacen")
        print("7. Carga Diaria Horas")
        print("8. Estadisticas Generales")
        print("9. Salir")


    def mostrar_altas(self):
        """
        # -----------------------------------------------------------------------------
        # Despliega el submenu de altas, y aguarda el a eleccion de una opcion, 
        # llamando al metodo correspondiente.
        # En caso de opcion incorrecta imprime mensaje de error y regresa al menu principal. 
        # -----------------------------------------------------------------------------
        """
        print("\nSubMenú de Altas:")
        print("1. Alta Maquina")
        print("2. Alta Actividad")
        print("3. Alta Operario")
        print("4. Alta Repuesto")
        print("5. Alta Consumible")
        print("6. Alta Proveedor")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.alta_maquina()
        elif opcion == '2':
            self.alta_actividad()
        elif opcion == '3':
            self.alta_operario()
        elif opcion == '4':
            self.alta_repuesto()
        elif opcion == '5':
            self.alta_consumible()
        elif opcion == '6':
            self.alta_proveedor()
        elif opcion == '9':
            self.ejecutar()
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


    def mostrar_bajas(self):
        """
        # -----------------------------------------------------------------------------
        # Despliega el submenu de bajas, y aguarda el a eleccion de una opcion, 
        # llamando al metodo correspondiente.
        # En caso de opcion incorrecta imprime mensaje de error y regresa al menu principal. 
        # -----------------------------------------------------------------------------
        """        
        print("\nSubMenú de Altas:")
        print("1. Baja Maquina")
        print("2. Baja Actividad")
        print("3. Baja Operario")
        print("4. Baja Repuesto")
        print("5. Baja Consumible")
        print("6. Baja Proveedor")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.baja_maquina()
        elif opcion == '2':
            self.baja_actividad()
        elif opcion == '3':
            self.baja_operario()
        elif opcion == '4':
            self.baja_repuesto()
        elif opcion == '5':
            self.baja_consumible()
        elif opcion == '6':
            self.baja_proveedor()
        elif opcion == '9':
            self.ejecutar()
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


# ------------------------------------------------------------------------------------------------------------------
# Aqui comienza el codigo con los metodos para hacer las consultas sobre y hacia la base de datos:
# alta_maquina()
# alta_actividad()
# alta_operario()
# alta_repuesto()
# alta_consumible()
# alta_proveedor()
# baja_maquina()
# baja_actividad()
# baja_operario()
# baja_repuesto()
# baja_consumible()
# baja_proveedor()  
# programar_actividad()
# historial_maquina()
# historial_operario()
# informe_almacen()
# carga_horas_diarias()
# ver_estadisticas_uso()
# salir()    
# ------------------------------------------------------------------------------------------------------------------ 




##   FUNCIÓN PARA DAR DE ALTA UNA MAQUINARIA
##
    def alta_maquina(self):
        print("Para continuar debe seleccionar tipo de maquina:")
        print("1. COSECHADORA")
        print("2. TRACTOR")
        print("3. CAMION")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_maquina = 'COSECHADORA'
        elif seleccion == '2':
            tipo_maquina = 'TRACTOR'
        elif seleccion == '3':
            tipo_maquina = 'CAMION'

        nombre = input("Ingrese nombre de la maquina: ")
        chasis = input("Ingrese codigo de chasis: ")
        motor = input("Ingrese codigo de motor: ")
        modelo = input("Ingrese modelo año: ")
        horas = input("Ingrese cantidad de horas de trabajo: ")

        consulta = "insert into maquina (Tipo_maquina, Nombre, Chasis, Motor, Modelo, Horas_de_Trabajo) values(%s, %s, %s, %s, %s, %s)"
        valores = (tipo_maquina, nombre, chasis, motor, modelo, horas)
        self.db.ejecutar_consulta(consulta, valores)
        print("Maquina ingresada correctamente.")


        
##   FUNCIÓN PARA DAR DE ALTA UNA ACTIVIDAD
##
    def alta_actividad(self):
        print("Seleccione tipo de actividad: ")
        print("1. TRABAJO")
        print("2. MANTENIMIENTO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            Tipo = 'TRABAJO'
        elif seleccion == '2':
            Tipo = 'MANTENIMIENTO'

        descripcion = input("Ingrese la descripción de la actividad: ")
        lugar = input("Ingrese el lugar de la actividad: ")
        limite_horas = input("Si la actividad es 'mantenimiento', ingrese limite de horas: ")
        id_maquina = input("Ingrese la maquina afectada a la actividad: ")
        id_operario = input("Ingrese el operario afectado a la actividad: ")

        consulta = "insert into actividad  (Tipo, Descripcion, Lugar, Limite_horas, Maquina_id_Maquina, Operario_idOperario) values(%s, %s, %s, %s, %s, %s)"
        valores = (Tipo, descripcion, lugar, limite_horas, id_maquina, id_operario)
        self.db.ejecutar_consulta(consulta, valores)
        print("Actividad ingresada correctamente.")



##   FUNCIÓN PARA DAR DE ALTA UN OPERARIO
##
    def alta_operario(self):
        print("Seleccione categoria operario: ")
        print("1. CHOFER")
        print("2. MECANICO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            categoria = 'CHOFER'
        elif seleccion == '2':
            categoria = 'MECANICO'

        nombre = input("Ingrese nombre de operario: ")
        apellido = input("Ingrese apellido del operario: ")
        esExterno = input("Si el operario no pertenece a la firma ingrese 'si' de lo contrario ingrese 'no' ")
        
        consulta = "insert into Operario  (nombre, apellido, categoria, esExterno) values(%s, %s, %s, %s)"
        valores = (nombre, apellido, categoria, esExterno)
        self.db.ejecutar_consulta(consulta, valores)
        print("Actividad ingresada correctamente.")
        

## FUNCIÓN PARA DAR DE ALTA UN CODIGO DE ALMACEN
##
    def alta_almacen(self):
        print("Se agregara stock a almacen, ingrese los siguientes datos:")
        cantidad = input("Ingrese cantidad de articulos en stock: ")
        critico = input("Ingrese la cantidad minima requerida: ")
               
        consulta = "insert into almacen  (stock, reserva) values(%s, %s)"
        valores = (cantidad, critico)
        self.db.ejecutar_consulta(consulta, valores)
        print("Repuesto agregado exitosamente...")



## FUNCIÓN PARA DAR DE ALTA UN REPUESTO
##
    def alta_repuesto(self):
        
        Descripcion = input("Ingrese descripción del repuesto: ")
        Marca = input("Ingrese la marca del repuesto original: ")
        Alternativo = input("Ingrese la marca del repuesto alternativo: ")
        id_activad = input("Ingrese la actividad a realizar: ")
        id_proveedor = input("Ingrese el proveedor del repuesto: ")
        self.alta_almacen()
        id_almacen = input("Ingrese el codigo interno del almacen: ")
        
        consulta = "insert into Repuesto  (Descripcion, Marca, Alternativo, Actividad_id_Actividad, Proveedor_id_Proveedor, Almacen_id_Almacen) values(%s, %s, %s, %s,%s,%s)"
        valores = (Descripcion, Marca, Alternativo, id_activad,id_proveedor,id_almacen)
        self.db.ejecutar_consulta(consulta, valores)
        print("Repuesto agregado exitosamente...")



##   FUNCIÓN PARA DAR DE ALTA UN CONSUMIBLE
##
    def alta_consumible(self):
        Descripcion = input("Ingrese descripción del consumible: ")
        Marca = input("Ingrese la marca del consumible original: ")
        Alternativo = input("Ingrese la marca del consumible alternativo: ")
        id_activad = input("Ingrese la actividad a realizar: ")
        id_proveedor = input("Ingrese el proveedor del consumible: ")
        self.alta_almacen()
        id_almacen = input("Ingrese el codigo interno del almacen: ")
        
        consulta = "insert into Consumible (Descripcion, Marca, Alternativo, Actividad_id_Actividad, Proveedor_id_Proveedor, Almacen_id_Almacen) values(%s, %s, %s, %s,%s,%s)"
        valores = (Descripcion, Marca, Alternativo, id_activad,id_proveedor,id_almacen)
        self.db.ejecutar_consulta(consulta, valores)
        print("Consumible agregado exitosamente...")



##   FUNCIÓN PARA DAR DE ALTA UN PROVEEDOR
##    
    def alta_proveedor(self):
        Nombre = input("Ingrese el nombre del proveedor: ")
        Direccion = input("Ingrese la dirección del proveedor: ")
        Despacho = input("Ingrese el lugar despacho: ")
        Pago = input("Ingrese el pago realizado: ")
                
        consulta = "insert into Proveedor (Nombre, Direccion, Despacho, Pago) values(%s, %s, %s, %s)"
        valores = (Nombre, Direccion, Despacho, Pago)
        self.db.ejecutar_consulta(consulta, valores)
        print("Proveedor ingresado exitosamente...")



##   FUNCIÓN PARA DAR DE BAJA UNA MAQUINARIA
##        
    def baja_maquina(self):
        print("Para continuar debe seleccionar tipo de maquina a eliminar: ")
        print("1. COSECHADORA")
        print("2. TRACTOR")
        print("3. CAMION")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_maquina = 'COSECHADORA'
        elif seleccion == '2':
            tipo_maquina = 'TRACTOR'
        elif seleccion == '3':
            tipo_maquina = 'CAMION'
        else:
            print("Selección inválida.")
            return

        chasis = input("Ingrese codigo de chasis de la maquina a eliminar: ")

        # A continuación confirma que la maquinaria existe antes de intentar eliminarla para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM maquina WHERE Tipo_maquina = %s AND Chasis = %s"
        valores_verificacion = (tipo_maquina, chasis)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)

        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar la maquinaria {tipo_maquina} con chasis {chasis}? `s` para CONFIRMAR, `n` CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM maquina WHERE Tipo_maquina = %s AND Chasis = %s"
                valores_eliminacion = (tipo_maquina, chasis)
                self.db.ejecutar_consulta(consulta_eliminacion, valores_eliminacion)
                print("Maquinaria eliminada correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró una maquinaria con el tipo y chasis proporcionados.")




##   FUNCIÓN PARA DAR DE BAJA UNA ACTIVIDAD
##   
    def baja_actividad(self):
        print("Para continuar debe seleccionar tipo de actividad a eliminar: ")
        print("1. TRABAJO")
        print("2. MANTENIMIENTO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_actividad = 'TRABAJO'
        elif seleccion == '2':
            tipo_actividad = 'MANTENIMIENTO'
        else:
            print("Selección inválida.")
            return
        descripcion_actividad = input("Ingrese la descripción de la actividad a eliminar: ")

    # A continuación, confirma que la actividad existe antes de intentar eliminar para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM actividad WHERE Tipo = %s AND Descripcion = %s"
        valores_verificacion = (tipo_actividad, descripcion_actividad)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)

        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar la actividad {tipo_actividad} con descripción '{descripcion_actividad}'? `s` para CONFIRMAR, `n` para CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM actividad WHERE Tipo = %s AND Descripcion = %s"
                valores_eliminacion = (tipo_actividad, descripcion_actividad)
                self.db.ejecutar_consulta(consulta_eliminacion, valores_eliminacion)
                print("Actividad eliminada correctamente.")
            else:
               print("Operación cancelada.")
        else:
            print("No se encontró una actividad con el tipo y descripción proporcionados.")




##   FUNCIÓN PARA DAR DE BAJA UN OPERARIO
##
    def baja_operario(self):
        print("Para continuar debe seleccionar tipo de operario: ")
        print("1. CHOFER")
        print("2. MECANICO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            categoria = 'CHOFER'
        elif seleccion == '2':
            categoria = 'MECANICO'

        nombre = input("Ingrese nombre de operario: ")
        apellido = input("Ingrese apellido del operario: ")
        
        # A continuación, confirma que el operario existe antes de intentar eliminar para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM Operario WHERE nombre = %s AND apellido = %s"
        valores_verificacion = (categoria, nombre, apellido)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)
        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar al operario {nombre} con descripción '{apellido}'? `s` para CONFIRMAR, `n` para CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM actividad WHERE Tipo = %s AND Descripcion = %s"
                valores_eliminacion = (nombre, apellido)
                self.db.ejecutar_consulta(consulta_eliminacion, valores_eliminacion)
                print("Operario eliminado correctamente.")
            else:
               print("Operación cancelada.")
        else:
            print("No se encontró un operario con el nómbre y apellido proporcionados.")
        



##   FUNCIÓN PARA DAR DE BAJA UN REPUESTO
##
    def baja_repuesto(self):
        consulta = "SELECT id_Repuesto, Descripcion, Marca, Alternativo FROM Repuesto"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            print("\nLista actual de repuestos disponibles: ")
            for repuestos in resultados:
                print(repuestos)
        else:
            print("No se encontraron repuestos en stock.")

        eliminar = input("Seleccione el repuesto que desea eliminar segun su ID: ")
        confirma_eliminar = input(f"Esta seguro que desea eliminar el repuesto: {eliminar}? (s/n)\n")
        if  confirma_eliminar == 's':
            consulta = "DELETE FROM Repuesto WHERE id_Repuesto = %s"
            self.db.ejecutar_consulta(consulta, tuple(eliminar))
            print("Repuesto eliminado. ")
        elif confirma_eliminar == 'n':
            print("Solicitud cancelada. ")
        else: 
            print("Por favor confirme correctamente la eliminación ingresando 's' o 'n' \n , intente nuevamente.")
            

        consulta = "SELECT id_Repuesto, Descripcion, Marca, Alternativo FROM Repuesto"
        resultados = self.db.obtener_resultados(consulta)
        print("\nLista actual de repuestos disponibles en stock: ")
        for stock in resultados:
            print(stock)




##   FUNCIÓN PARA DAR DE BAJA UN CONSUMIBLE
##         
    def baja_consumible(self):
        consulta = "SELECT id_Consumible, Descripcion, Marca, Alternativo FROM Consumible"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            print("\nLista actual de consumibles disponibles: ")
            for consum in resultados:
                print(consum)
        else:
            print("No se encontraron consumibles disponibles en stock.")

        eliminar = input("Seleccione el consumible que desea eliminar segun su ID: ")
        confirma_eliminar = input(f"Esta seguro que desea eliminar el consumible: {eliminar}? (s/n)\n")
        if  confirma_eliminar == 's':
            consulta = "DELETE FROM Consumible WHERE id_Consumible = %s"
            self.db.ejecutar_consulta(consulta, tuple(eliminar))
            print("Consumible eliminado. ")
        elif confirma_eliminar == 'n':
            print("Solicitud cancelada. ")
        else: 
            print("Por favor confirme correctamente la eliminación ingresando 's' o 'n' \n , intente nuevamente.")
            

        consulta = "SELECT id_Consumible, Descripcion, Marca, Alternativo FROM Consumible"
        resultados = self.db.obtener_resultados(consulta)
        print("\nLista actual de consumibles disponibles en stock: ")
        for stockcons in resultados:
            print(stockcons)
 
 
 
            
##   FUNCIÓN PARA DAR DE BAJA UN PROVEEDOR
##
    def baja_proveedor(self):
        print("A continuacion se detallara los proveedores activos: ")
        consulta = "SELECT id_Proveedor, Nombre, Direccion FROM Proveedor"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            print("\nUltima lista vigente: ")
            for provee in resultados:
                print(provee)
        else:
            print("No se encontraron proveedores activos.")

        eliminar = input("Seleccione el proveedor que desea eliminar segun su ID: ")
        confirma_eliminar = input(f"Esta seguro que desea eliminar el proveedor: {eliminar}? (s/n)\n")
        if  confirma_eliminar == 's':
            consulta = "DELETE FROM Proveedor WHERE id_Proveedor = %s"
            self.db.ejecutar_consulta(consulta, tuple(eliminar))
            print("El proveedor fue eliminado.")
        elif confirma_eliminar == 'n':
            print("Solicitud cancelada. ")
        else: 
            print("Por favor confirme correctamente la eliminación ingresando 's' o 'n' \n , intente nuevamente.")
            

        consulta = "SELECT id_Proveedor, Nombre, Direccion FROM Proveedor"
        resultados = self.db.obtener_resultados(consulta)
        print("\nLista actual de proveedores activos: ")
        for i in resultados:
            print(i)
 

    def programar_actividad(self):
        print("Seleccione tipo de actividad a programar:")
        print("1. TRABAJO")
        print("2. MANTENIMIENTO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            Tipo = 'TRABAJO'
        elif seleccion == '2':
            Tipo = 'MANTENIMIENTO'
        else:
            print("Selección inválida.")
            return

        descripcion = input("Ingrese la descripción de la actividad: ")
        lugar = input("Ingrese el lugar de la actividad: ")
        id_maquina = input("Ingrese la ID de la máquina afectada a la actividad: ")
        id_operario = input("Ingrese la ID del operario afectado a la actividad: ")

        consulta = "insert into actividad (Tipo, Descripcion, Lugar, Maquina_id_Maquina, Operario_idOperario) values(%s, %s, %s, %s, %s)"
        valores = (Tipo, descripcion, lugar, id_maquina, id_operario)
        self.db.ejecutar_consulta(consulta, valores)
        print("Actividad programada correctamente.")


    def historial_maquina(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por y sobre la maquina
# ---------------------------------------------------------------------------------         
        """
        print("A continuación se detalla lista de maquinas para mostrar su historial: ")
        consulta = "SELECT id_maquina, Nombre, Chasis FROM maquina"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            # Convertir resultados a un DataFrame de pandas
            tabla_maquina = pd.DataFrame(resultados, columns=['id_Maquina', 'Nombre', 'Chasis'])
            print(tabla_maquina.to_string(index=False, justify= 'center'))
        else:
            print("No se encontraron máquinas en la base de datos.")

        hist_id = input("Seleccione la maquina que desea consultar: ")
        
        consulta = """SELECT M.id_Maquina, M.Nombre, M. Chasis, A.Tipo, A.Descripcion, O.Nombre, O.apellido 
                    FROM maquina M, actividad A, operario O 
                    WHERE M.id_Maquina = A.Maquina_id_Maquina AND O.idOperario = A.Operario_idOperario"""

        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            print("\nHistorial de Máquina:")
            # Convertir resultados a un DataFrame de pandas
            df_historial = pd.DataFrame(resultados, columns=['id_Maquina', 'Nombre', 'Chasis', 'Tipo', 'Descripcion', 'Operario_Nombre', 'Operario_Apellido'])
            print(df_historial.to_string(index=False, justify= 'center'))
        else:
            print(f"No se encontró historial para la máquina con id {hist_id}.")


    def historial_operario(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por un operario 
# --------------------------------------------------------------------------------- 
# """   
        print("A continuación se detalla lista de operarios para mostrar su historial: ")
        consulta = "SELECT idOperario, Nombre, Apellido FROM operario"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            # Convertir resultados a un DataFrame de pandas
            tabla_maquina = pd.DataFrame(resultados, columns=['idOperario', 'Nombre', 'Apellido'])
            print(tabla_maquina.to_string(index=False, justify= 'center'))
        else:
            print("No se encontraron máquinas en la base de datos.")     
        id_operario = input("Ingrese el ID del operario para consultar su historial: ")
        consulta = """
        SELECT a.Tipo, a.Descripcion, a.Lugar, a.Limite_horas, m.Nombre AS Maquina, o.nombre AS Operario, o.apellido
        FROM actividad a
        JOIN maquina m ON a.Maquina_id_Maquina = m.id_Maquina
        JOIN Operario o ON a.Operario_idOperario = o.idOperario
        WHERE o.idOperario = %s
        """
        valores = (tuple(id_operario))
        resultados = self.db.obtener_resultados(consulta, valores)
        
        if resultados:
            print(f"\nHistorial de actividades para el operario ID {id_operario}:")
            for actividad in resultados:
                print(f" Tipo: {actividad[0]},\nDescripción: {actividad[1]},\nLugar: {actividad[2]},\n"
                      f"Límite de horas: {actividad[3]},\nMáquina: {actividad[4]},\n"
                      f"Operario: {actividad[5]} {actividad[6]}\n")
        else:
            print(f"No se encontraron actividades para el operario ID {id_operario}.")

    def informe_almacen(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar el stock del almacen discriminado en cantidad actual y
# cantidad critica.
# ---------------------------------------------------------------------------------         
        """        
        print("Informe de Almacen, reporte de stock y cantidades criticas")
        consulta = "SELECT * FROM almacen"
        resultados = self.db.obtener_resultados(consulta)
        if resultados:
            print("\nInforme Almacen")
            # Convertir resultados a un DataFrame de pandas
            df_almacen = pd.DataFrame(resultados, columns=['id_Almacen', 'stock', 'cantidad critica'])
            print(df_almacen.to_string(index=False, justify= 'center'))
        else:
            print("No se puede mostrar almacen, falta de datos.")


    def alerta_mantenimiento(self, id_maquina):
        """
# ---------------------------------------------------------------------------------
# Esta consulta chequea posibles tareas de mantenimiento para una maquina en particular
# ---------------------------------------------------------------------------------         
    """
        consulta = """
        SELECT a.Descripcion, a.Limite_horas, m.Horas_de_Trabajo, m.Nombre, m.chasis
        FROM actividad a
        JOIN maquina m ON a.Maquina_id_Maquina = m.id_Maquina
        WHERE m.id_Maquina = %s AND a.Limite_horas IS NOT NULL
        """
        valores = (tuple(id_maquina))
        resultados = self.db.obtener_resultados(consulta, valores)

        for actividad in resultados:
            if actividad[2] >= actividad[1]:
                print(f"Alerta: La máquina {actividad[3]}, chasis {actividad[4]},\n ha alcanzado el límite de horas para la actividad '{actividad[0]}' ({actividad[1]}).")



    def alerta_mantenimiento(self):
        """
# ---------------------------------------------------------------------------------
# Esta consulta chequea posibles tareas de mantenimiento
# ---------------------------------------------------------------------------------         
    """
        consulta = """
        SELECT a.Descripcion, a.Limite_horas, m.Horas_de_Trabajo, m.Nombre, m.chasis
        FROM actividad a
        JOIN maquina m ON a.Maquina_id_Maquina = m.id_Maquina
        WHERE a.Limite_horas IS NOT NULL AND a.Limite_horas > 0
        """
        resultados = self.db.obtener_resultados(consulta,)

        for actividad in resultados:
            if actividad[2] >= actividad[1]:
                print(f"Alerta: La máquina {actividad[3]}, chasis {actividad[4]},\n ha alcanzado el límite de horas para la actividad '{actividad[0]}' ({actividad[1]}).")



    def carga_horas_diarias(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario cargara la cantidad de horas trabajadas por una maquina al finalizar
# la jornada de trabajo. 
# Este metodo arroja una alarma de actividad pendiente si se alcanza el limite de horas 
# para dicha actividad.
# ---------------------------------------------------------------------------------         
        """          
        print("Generar consulta para actualizar el contador de horas a una maquina determinada")
        print("llamar al metodo alerta de mantenimiento")
        id_maquina = input("Ingrese el ID de la máquina: ")
        horas_trabajadas = input("Ingrese la cantidad de horas trabajadas hoy: ")

        # Actualizar las horas trabajadas de la máquina
        consulta_actualizar = "UPDATE maquina SET Horas_de_Trabajo = Horas_de_Trabajo + %s WHERE id_Maquina = %s"
        valores_actualizar = (horas_trabajadas, id_maquina)
        self.db.ejecutar_consulta(consulta_actualizar, valores_actualizar)

        # Verificar si se ha alcanzado el límite de horas para alguna actividad
        print("chequeo si tienen actividad pendiente")
        self.alerta_mantenimiento(id_maquina)
        


    def ver_estadisticas_uso(self):
        """
# ---------------------------------------------------------------------------------
# Esta consulta imprime estadisticas generales de la Flota
# ---------------------------------------------------------------------------------         
        """ 
        print("generar una consulta para tirar estadisticas ")
        consulta = "SELECT tipo_maquina, COUNT(*) AS cantidad, AVG(horas_de_trabajo) AS promedio_horas FROM maquina GROUP BY tipo_maquina"
        resultados = self.db.obtener_resultados(consulta)

        if resultados:
            print("\nInforme estadisticas generales")
            # Convertir resultados a un DataFrame de pandas
            df_estad = pd.DataFrame(resultados, columns=['tipo_maquina', 'cantidad', 'promedio_horas'])
            print(df_estad.to_string(index=False, justify= 'center'))
        else:
            print("No se puede mostrar estadisticas, falta de datos.")

 
    
    def alerta_almacen(self, id_almacen):
        consulta = """
        SELECT r.Descripcion, r.Marca, r.Alternativo, c.Descripcion, c.Marca, c.Alternativo
        FROM Repuesto r
        LEFT JOIN Consumible c ON r.Almacen_id_Almacen = c.Almacen_id_Almacen
        WHERE r.Almacen_id_Almacen = %s
        """
        valores = (id_almacen,)
        resultados = self.db.obtener_resultados(consulta, valores)

        for repuesto, consumible in resultados:
            print(f"Repuesto - Descripción: {repuesto[0]}, Marca: {repuesto[1]}, Alternativo: {repuesto[2]}")
            if consumible:
               print(f"Consumible - Descripción: {consumible[0]}, Marca: {consumible[1]}, Alternativo: {consumible[2]}")

    def compra_semanal(self):
        consulta_repuesto = """
        SELECT r.Descripcion, a.Cantidad_Critica - a.Cantidad_Actual as Cantidad_Reponer
        FROM Repuesto r
        JOIN Almacen a ON r.Almacen_id_Almacen = a.id_Almacen
        WHERE a.Cantidad_Actual < a.Cantidad_Critica
        """

        consulta_consumible = """
        SELECT c.Descripcion, a.Cantidad_Critica - a.Cantidad_Actual as Cantidad_Reponer
        FROM Consumible c
        JOIN Almacen a ON c.Almacen_id_Almacen = a.id_Almacen
        WHERE a.Cantidad_Actual < a.Cantidad_Critica
        """

        resultados_repuesto = self.db.obtener_resultados(consulta_repuesto)
        resultados_consumible = self.db.obtener_resultados(consulta_consumible)

        if resultados_repuesto or resultados_consumible:
           print("Reporte de compra semanal:")
        for item in resultados_repuesto:
           print(f"Repuesto - {item[0]}: {item[1]} unidades a reponer")
        for item in resultados_consumible:
           print(f"Consumible - {item[0]}: {item[1]} unidades a reponer")
        else:
            print("No hay insumos en estado crítico para reponer.")

    def salir(self): 
        print("Saliendo del programa... Hasta luego! ")
