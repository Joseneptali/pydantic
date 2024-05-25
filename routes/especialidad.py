from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import Connection
from models.especialidad import especialidad


app = FastAPI()

       
@app.get('/especialidades/')
async def get_especialidad():
    cursor = Connection.cursor(dictionary=True)
    query ='SELECT * FROM especialidades'
    
    try:
        cursor.execute(query)
        Especialidades = cursor.fetchall()
        return Especialidades
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="error al obtener datos de la Especialidad")
    finally:
        cursor.close()


@app.post('/especialidades/')
async def create_especialidad(especialidad: especialidad):
    cursor = Connection.cursor()

    query = "INSERT INTO especialidades (codigo_especialidad, nombre_especialidad, descripcion, estado) VALUES (%s, %s, %s, %s)"
    value = (especialidad.codigo_especialidad, especialidad.nombre_especialidad, especialidad.descripcion, especialidad.estado)
    
    try:
        cursor.execute(query, value)        
        Connection.commit()
        return {'message': 'Creacion Exitosa'}, 201
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de Campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar la Especialidad {err}")
    finally: 
        cursor.close

@app.put('/especialidades')
def update_especialidad(especialidad_id: int, especialidad_data: especialidad):
    cursor = Connection.cursor(dictionary=True)
    query ='SELECT * FROM especialidades'

    # Verificar si los datos necesarios están presentes
    if 'id' not in especialidad_data.dict():
            raise HTTPException(status_code=400, detail="Se requiere un id válido")
    try:
        connection = Connection()
        cursor = connection.cursor(dictionary=True)

        # Verificar si los datos necesarios están presentes
        if 'id' not in especialidad_data.dict():
            raise HTTPException(status_code=400, detail="Se requiere un id válido")

        cursor.execute("""
            UPDATE especialidades 
            SET 
                codigo_especialidad = %s, 
                nombre_especialidad = %s, 
                descripcion = %s, 
                estado = %s
            WHERE id = %s""", 
                (
            especialidad_data.codigo_especialidad,
            especialidad_data.nombre_especialidad,
            especialidad_data.descripcion,            
            especialidad_id
        ))

        connection.commit()
        cursor.close()

        return {'message': 'Especialidad actualizada correctamente'}
    except mysql.connector.Error as e:
        return {'error': str(e)}

@app.delete('/especialidades')
def delete_especialidad():
    
    connection = connection()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM especialidades WHERE id = %s", (especialidad['id']))
           
            connection.commit()

        return {'message': 'Especialidad Borrada correctamente'}, 200
    except Exception as e:
        return {'error': str(e)}, 500