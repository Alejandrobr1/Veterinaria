#Sistema Simple de Gestión para Veterinaria
import Animales, Personas, Historias

# Listas para almacenar los datos de la clínica veterinaria
nueva_mascota = []  # Almacena todas las mascotas registradas
nueva_consulta = []  # Almacena todas las consultas realizadas
nuevo_duenho = []  # Almacena todos los dueños registrados


def menu():
    """
    Función principal que muestra el menú de la clínica veterinaria y gestiona las diferentes opciones:
    1. Registro de nuevas mascotas
    2. Registro de consultas veterinarias
    3. Listado de mascotas registradas
    4. Visualización del historial médico de una mascota
    5. Salir del sistema
    """
    while True:
        print("=" * 60)
        print("=" * 60)
        print('Menu Principal:\n\n'
              '1. Registrar una mascota.\n'
              '2. Registrar una consulta.\n'
              '3. Listar mascotas.\n'
              '4. Ver historial de consultas de una mascota.\n'
              '5. Salir.\n')
        print("-" * 60)
        opcion = int(input('Seleccione una opcion: '))

        # Opción 1: Registro de nueva mascota y su dueño
        if opcion == 1:
            nombre_mascota = str(input('ingrese el nombre de la mascota: ')).lower().strip().capitalize()
            nombre_duenho = str(input('ingrese el nombre del dueño de la mascota: ')).lower().strip().capitalize()
            if validar_mascota_duenho(nombre_mascota, nombre_duenho):
                guardar_mascota_duenho(nombre_mascota, nombre_duenho)
                print(f"Felicidades! {nombre_mascota} fue añadido con exito\n")
            else:
                return print("la mascota ya esta registrada"), menu()

        # Opción 2: Registro de nueva consulta veterinaria
        elif opcion == 2:
            mascota_relacionada = str(
                input('ingrese el nombre de la mascota relacionada: ')).lower().strip().capitalize()
            if buscar_mascota(mascota_relacionada):
                fecha_consulta = str(input('ingrese la fecha de la consulta: ')).lower().strip().capitalize()
                motivo = str(input('ingrese el motivo de consulta: ')).lower().strip().capitalize()
                diagnostico = str(input('ingrese el diagnostico de la mascota: ')).lower().strip().capitalize()
                consulta = Historias.Consulta(fecha_consulta, motivo, diagnostico, mascota_relacionada)
                nueva_consulta.append(consulta)
                print("La consulta ha quedado registrada")
            else:
                print("No hay consultas asociadas a la mascota", mascota_relacionada)

        # Opción 3: Mostrar listado de mascotas y dueños
        elif opcion == 3:
            listar_mascota()
            listar_duenho()

        # Opción 4: Mostrar historial de consultas de una mascota
        elif opcion == 4:
            nombre_mascota = str(input('ingrese el nombre de la mascota: ')).lower().strip().capitalize()
            if buscar_mascota(nombre_mascota):
                for consulta in nueva_consulta:
                    print("Historial de consultas de la mascota: \n", nombre_mascota)
                    print("Fecha: ", consulta.fecha)
                    print("Motivo de la consulta", consulta.motivo)
                    print("Diagnostico de la mascota", consulta.diagnostico)
            else:
                print("No hay consultas asociadas a la mascota", nombre_mascota)

        # Opción 5: Salir del sistema
        elif opcion == 5:
            exit()
        else:
            print("Opcion no valida")


def guardar_mascota_duenho(nombre_mascota, nombre_duenho):
    """
    Registra una nueva mascota y su dueño en el sistema.
    Solicita y almacena información detallada de ambos.

    Args:
        nombre_mascota (str): Nombre de la mascota a registrar
        nombre_duenho (str): Nombre del dueño de la mascota

    Returns:
        tuple: Objetos mascota y dueño creados
    """
    especie = str(input('ingrese la especie de la mascota: ')).lower().strip().capitalize()
    raza = str(input('ingrese la raza de la mascota: ')).lower().strip().capitalize()
    edad = str(input('ingrese la edad de la mascota: ')).lower().strip().capitalize()
    print("Ahora ingrese los datos del dueño:")
    telefono = str(input('ingrese el telefono de la persona: ')).lower().strip().capitalize()
    direccion = str(input("ingrese la dirección del dueño: ")).lower().strip().capitalize()

    # Crear y guardar los objetos
    mascota = Animales.Mascota(nombre_mascota, especie, raza, edad, nombre_duenho)
    nueva_mascota.append(mascota)
    duenho = Personas.Duenho(nombre_duenho, telefono, direccion)
    nuevo_duenho.append(duenho)
    return mascota, duenho


def buscar_mascota(mascota_relacionada):
    """
    Verifica si una mascota está registrada en el sistema.

    Args:
        mascota_relacionada (str): Nombre de la mascota a buscar

    Returns:
        bool: True si la mascota existe, False en caso contrario
    """
    for mascota in nueva_mascota:
        if mascota.nombre_mascota == mascota_relacionada:
            return True
    return False


def validar_mascota_duenho(nombre_mascota, nombre_duenho):
    """
    Verifica que no exista una combinación duplicada de mascota y dueño.

    Args:
        nombre_mascota (str): Nombre de la mascota
        nombre_duenho (str): Nombre del dueño

    Returns:
        bool: True si la combinación es única, False si ya existe
    """
    for mascota in nueva_mascota:
        if mascota.nombre_mascota == nombre_mascota and mascota.duenho == nombre_duenho:
            return False
    return True


def listar_mascota():
    """
    Muestra en pantalla todas las mascotas registradas en el sistema
    con sus respectivos detalles.

    Returns:
        bool: False si no hay mascotas registradas
    """
    if not nueva_mascota:
        print("No hay mascotas registradas en el sistema")
        return False

    for i, mascota in enumerate(nueva_mascota, 1):
        print("=" * 60)
        print(f"Mascota {i}")
        print("=" * 60)
        print("Nombre de la mascota: ", mascota.nombre_mascota)
        print("Especie de la mascota: ", mascota.especie)
        print("Raza de la mascota: ", mascota.raza)
        print("Edad de la mascota: ", mascota.edad)
        print("Dueño de la mascota: ", mascota.duenho)
    return False


def listar_duenho():
    """
    Muestra en pantalla todos los dueños registrados en el sistema
    con sus respectivos detalles.

    Returns:
        bool: False si no hay dueños registrados
    """
    if not nuevo_duenho:
        print("No hay dueños registrados en el sistema")
        return False

    for i, duenho in enumerate(nuevo_duenho, 1):
        print("*" * 60)
        print(f"Dueño {i}")
        print("*" * 60)
        print("Nombre del dueño: ", duenho.nombre_duenho)
        print("Telefono: ", duenho.telefono)
        print("Direccion: ", duenho.direccion)
    return False


# Iniciar el programa
menu()