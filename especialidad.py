from fastapi import FastAPI, jsonify, request
from models import especialidad
import pymysql

app = FastAPI()

def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 database='db',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/especialidades', methods=["POST"])
def create():

    data = request.get_json()

    especialidad = especialidad(data)

    connection = connection_mysql()

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO especialidades (especialidad, descripcion, estado) VALUES (%s, %s, %s)"
                cursor.execute(sql, (especialidad))
            connection.commit()

        return jsonify({'message': 'Creacion Exitosa'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
       

# Endpoint para listar loas especialidades
@app.route('/especialidades', methods=['GET'])
def list():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM especialidades'
            cursor.execute(sql)
            result = cursor.fetchall()

            return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()


# Endpoint para actualizar los especialidad
@app.route('/especialidades', methods=["PUT"])
def update_user():
    data = request.get_json()
    connection = connection_mysql()

    # Verificar si los datos necesarios están presentes
    if 'id' not in data:
        return jsonify({'error': 'Se requiere id valido '}), 400

    try:
        with connection.cursor() as cursor:

            cursor.execute("UPDATE especialidades SET especialidad = %s, descripcion = %s, estado = %s  WHERE id = %s", (data['especialidad'], 
                                                                                                                         data['descripcion'],
                                                                                                                         data['estado'],  
                                                                                                                         data['id']))

            connection.commit()

        return jsonify({'message': 'especialidad actualizado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Endpoint para borar los usuarios
@app.route('/especialidades', methods=["DELETE"])
def delete():
    data = request.get_json()
    connection = connection_mysql()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM especialidades WHERE id = %s", (data['id']))
           
            connection.commit()

        return jsonify({'message': 'especialid Borrado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500