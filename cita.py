from fastapi import FastAPI, jsonify, request
from models import cita
import pymysql

app = FastAPI()

def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 database='db',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/citas', methods=["POST"])
def create():

    data = request.get_json()

    cita = cita(data)

    connection = connection_mysql()

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO citas (codigo_cita, nombre_paciente, medico, fecha, tiempo, email, numero_telefono, mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (cita))
            connection.commit()

        return jsonify({'message': 'Creacion Exitosa'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
       

# Endpoint para listar de citas
@app.route('/citas', methods=['GET'])
def list():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM citas'
            cursor.execute(sql)
            result = cursor.fetchall()

            return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()


@app.route('/citas', methods=["PUT"])
def update_user():
    data = request.get_json()
    connection = connection_mysql()

    # Verificar si los datos necesarios están presentes
    if 'id' not in data:
        return jsonify({'error': 'Se requiere id valido '}), 400

    try:
        with connection.cursor() as cursor:

            cursor.execute("UPDATE citas SET codigo_cita = %s, nombre_paciente = %s, especialidad = %s, medico = %s, fecha = %s, tiempo = %s, email = %s, numero_telefono = %s, mensaje = %s  WHERE id = %s", 
            (data['codigo_cita'], 
             data['nombre_paciente'],
             data['especialidad'],  
             data['medico'], 
             data['fecha'],  
             data['tiempo'],  
             data['numero_telefono'], 
             data['mensaje']  ))

            connection.commit()

        return jsonify({'message': 'citas actualizado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Endpoint para borar los cita
@app.route('/citas', methods=["DELETE"])
def delete():
    data = request.get_json()
    connection = connection_mysql()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM citas WHERE id = %s", (data['id']))
           
            connection.commit()

        return jsonify({'message': 'cita Borrado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500