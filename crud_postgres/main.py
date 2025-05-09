from .crud import (
    obtener_registros,
    obtener_registro_por_id,
    obtener_registros_por_id,
    crear_registro,
    crear_registros,
    actualizar_registro,
    actualizar_registros,
    eliminar_registro,
    eliminar_registros,
)

def mostrar_menu():
    print('\n--- Menú CRUD ---')
    print('1. Obtener todos los registros')
    print('2. Obtener un registro por ID')
    print('3. Obtener varios registros por ID')
    print('4. Crear un registro')
    print('5. Crear varios registros')
    print('6. Actualizar un registro')
    print('7. Actualizar varios registros')
    print('8. Eliminar un registro')
    print('9. Eliminar varios registros')
    print('0. Salir')

def main():
    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            obtener_registros()
        elif opcion == '2':
            obtener_registro_por_id()
        elif opcion == '3':
            obtener_registros_por_id()
        elif opcion == '4':
            crear_registro()
        elif opcion == '5':
            crear_registros()
        elif opcion == '6':
            actualizar_registro()
        elif opcion == '7':
            actualizar_registros()
        elif opcion == '8':
            eliminar_registro()
        elif opcion == '9':
            eliminar_registros()
        elif opcion == '0':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Intente de nuevo.')

if __name__ == '__main__':
    main()
