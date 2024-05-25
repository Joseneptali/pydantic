from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi import APIRouter, Depends
from core.auth_token import MyHTTPBearer
from models import medico
from pydantic import BaseModel
import pymysql
from jose import jwt

router = APIRouter()
bearer = MyHTTPBearer()

app = FastAPI()

def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 database='ulaapp',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.post("/medicos", status_code=status.HTTP_201_CREATED)
async def create(request:Request):

    data = await request.json()

    medico = medico(data)

    connection = connection_mysql()

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO medico (nombre, apellido, usuario, email, contrasena, fecha_nacimiento, sexo, direccion, pais, ciudad, codigo_postal, telefono, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (medico))
            connection.commit()

        return ({'message': 'Creacion Exitosa'}), 201
    except Exception as e:
        return ({'error': str(e)}), 500
       

# Endpoint para listar todos los medicos
@app.get("/medicos")
def list():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM medico'
            cursor.execute(sql)
            result = cursor.fetchall()

            return ({'data': result}), 200
    except Exception as e:
        return ({'error': str(e)}), 500
    finally:
        connection.close()


# Endpoint para actualizar los medicos
@app.put("/medicos")
def update_user():
    data = Request.get_json()
    connection = connection_mysql()

    # Verificar si los datos necesarios están presentes
    if 'id' not in data:
        return ({'error': 'Se requiere id valido '}), 400

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

        return ({'message': 'medico actualizado correctamente'}), 200
    except Exception as e:
        return ({'error': str(e)}), 500
    

# Endpoint para borar los medicos
@app.route("/medicos")
def delete():
    data = Request.get_json()
    connection = connection_mysql()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM medico WHERE id = %s", (data['id']))
           
            connection.commit()

        return ({'message': 'medico Borrado correctamente'}), 200
    except Exception as e:
        return ({'error': str(e)}), 500