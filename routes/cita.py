from fastapi import FastAPI, HTTPException
import mysql.connector
from core.config import Connection
from models.cita import cita


app = FastAPI()


@app.post('/citas/')
async def create_cita(cita: cita):
    cursor = Connection.cursor()

    query = "INSERT INTO citas (codigo_cita, nombre_paciente, especialidad, medico, fecha, tiempo, email, numero_telefono, mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    value = (cita.codigo_cita, cita.nombre_paciente, cita.especialidad, cita.fecha, cita.tiempo, cita.email, cita.numero_telefono, cita.mensaje)
    
    try:
        cursor.execute(query, value)        
        Connection.commit()
        return {'message': 'Creacion Exitosa'}, 201
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de Campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar la cita {err}")
    finally: 
        cursor.close
       

# Endpoint para listar de citas
@app.get('/citas/')
async def get_cita():
    cursor = Connection.cursor(dictionary=True)
    query ='SELECT * FROM citas'
    
    try:
        cursor.execute(query)
        Citas = cursor.fetchall()
        return Citas
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="error al obtener datos de Citas")
    finally:
        cursor.close()

@app.put('/citas')
def update_cita(cita_id: int, cita_data: cita):
    cursor = Connection.cursor(dictionary=True)
    query ='SELECT * FROM citas'

    # Verificar si los datos necesarios están presentes
    if 'id' not in cita_data.dict():
            raise HTTPException(status_code=400, detail="Se requiere un id válido")
    try:
        connection = Connection()
        cursor = connection.cursor(dictionary=True)

        # Verificar si los datos necesarios están presentes
        if 'id' not in cita_data.dict():
            raise HTTPException(status_code=400, detail="Se requiere un id válido")

        cursor.execute("""
            UPDATE citas 
            SET 
                codigo_cita = %s, 
                nombre_paciente = %s, 
                especialidad = %s, 
                medico = %s, 
                fecha = %s,  
                tiempo = %s,  
                numero_telefono = %s, 
                mensaje = %s  
                WHERE id = %s""", 
                (
            cita_data.codigo_cita,
            cita_data.nombre_paciente,
            cita_data.especialidad,
            cita_data.medico,
            cita_data.fecha,
            cita_data.tiempo,
            cita_data.numero_telefono,
            cita_data.mensaje,
            cita_id
        ))

        connection.commit()
        cursor.close()

        return {'message': 'Cita actualizada correctamente'}
    except mysql.connector.Error as e:
        return {'error': str(e)}


@app.delete('/citas')
def delete_cita():
    
    connection = connection()
    
    try:
        with connection.cursor() as cursor:
                        
            cursor.execute("DELETE FROM citas WHERE id = %s", (cita['id']))
           
            connection.commit()

        return {'message': 'cita Borrado correctamente'}, 200
    except Exception as e:
        return {'error': str(e)}, 500