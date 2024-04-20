from fastapi import FastAPI
from models import medico

app = FastAPI()

def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 database='db',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/medicos', methods=["POST"])
def create():

    data = request.get_json()

    medico = medico(data)

    connection = connection_mysql()

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO medico (nombre, apellido, usuario, email, contrasena, fecha_nacimiento, sexo, direccion, pais, ciudad, codigo_postal, telefono, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (paciente))
            connection.commit()

        return jsonify({'message': 'Creacion Exitosa'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
       

# Endpoint para listar todos los medicos
@app.route('/medicos', methods=['GET'])
def list():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM medico'
            cursor.execute(sql)
            result = cursor.fetchall()

            return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()


# Endpoint para actualizar los medicos
@app.route('/medicos', methods=["PUT"])
def update_user():
    data = request.get_json()
    connection = connection_mysql()

    # Verificar si los datos necesarios están presentes
    if 'id' not in data:
        return jsonify({'error': 'Se requiere id valido '}), 400

    try:
        with connection.cursor() as cursor:

            cursor.execute("UPDATE medico SET nombre = %s, apellido = %s, usuario = %s, email = %s, contrasena = %s, fecha_nacimiento = %s, sexo = %s, direccion = %s, pais = %s, ciudad = %s, codigo_postal = %s, telefono = %s, estado = %s", 
            (
             data['nombre'], 
             data['apellido'],
             data['usuario'],  
             data['email'],
             data['contrasena'], 
             data['fecha_nacimiento'],
             data['sexo'],  
             data['direccion'],
             data['pais'], 
             data['ciudad'],
             data['codigo_postal'],  
             data['telefono'],
             data['estado']
             ))

            connection.commit()

        return jsonify({'message': 'medico actualizado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Endpoint para borar los medicos
@app.route('/medicos', methods=["DELETE"])
def delete():
    data = request.get_json()
    connection = connection_mysql()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM medico WHERE id = %s", (data['id']))
           
            connection.commit()

        return jsonify({'message': 'medico Borrado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500