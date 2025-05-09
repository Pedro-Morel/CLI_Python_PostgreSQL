from .database import get_connection

# Obtener todos los registros
def obtener_registros():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona'
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                print(registros)
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()

# Obtener un unico registro
def obtener_registro_por_id():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona WHERE id = %s'
                id = input('Introduzca el id: ')
                cursor.execute(sentencia, (id,))
                registro = cursor.fetchone()
                print(registro)
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()

# Obtener varios registros por id
def obtener_registros_por_id():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                entrada = input('Introduzca los id separados por coma: ')
                ids = tuple(entrada.strip().split(','))
                sentencia = 'SELECT * FROM persona WHERE id IN %s'
                cursor.execute(sentencia, (ids,))
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()

# Insertar un unico registro
def crear_registro():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia ='INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
                entrada = input('Ingrese los datos: nombre, apellido, email (separados por coma): ')
                valores = tuple(entrada.strip().split(','))
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

# Insertar varios registros
def crear_registros():
    try: 
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
                print('Ingrese cada registro en una línea, separados por coma (nombre,apellido,email). Escriba "fin" para terminar.')
                valores = []
                while True:
                    entrada = input()
                    if entrada.lower() == 'fin':
                        break
                    valores.append(tuple(entrada.strip().split(',')))
                cursor.executemany(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

# Actualizar un unico registro
def actualizar_registro():
    try: 
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
                entrada = input('Ingrese los datos: nombre, apellido, email, id (separados por coma): ')
                valores = tuple(entrada.strip().split(','))
                cursor.execute(sentencia, valores)
                registro_actualizado = cursor.rowcount
                print(f'Registro actualizado: {registro_actualizado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

# Actualizar registros
def actualizar_registros():
    try: 
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
                print('Ingrese cada registro en una línea, separados por coma (nombre,apellido,email,id). Escriba "fin" para terminar.')
                valores = []
                while True:
                    entrada = input()
                    if entrada.lower() == 'fin':
                        break
                    valores.append(tuple(entrada.strip().split(',')))
                cursor.executemany(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Registros actualizados: {registros_actualizados}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

# Eliminar registro
def eliminar_registro():
    try: 
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM persona WHERE id=%s'
                id = input('Introduzca el id: ')
                cursor.execute(sentencia, (id,))
                registro_eliminado = cursor.rowcount
                print(f'Registro eliminado: {registro_eliminado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

# Eliminar varios registros
def eliminar_registros():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                entrada = input('Introduzca los id separados por coma: ')
                ids = tuple(entrada.strip().split(','))
                sentencia = 'DELETE FROM persona WHERE id IN %s'
                cursor.execute(sentencia, (ids,))
                registros_eliminados = cursor.rowcount
                print(f'Registros eliminados: {registros_eliminados}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()
