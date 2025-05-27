from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 5. 
# 5.1 En una consulta, obtener todos los cursos.
# 5.2 Realizar un ciclo repetitivo para obtener en cada iteración
# las entregas por cada curso (con otra consulta), y presentar el
# promedio de calificaciones de las entregas

cursos = session.query(Curso).all()

for curso in cursos:
    # Obtener todas las entregas del curso actual
    entregas = session.query(Entrega).join(Tarea).filter(Tarea.curso_id == curso.id).all()
    
    # Calcular el promedio de calificaciones
    if entregas:  # Asegurarse de que haya entregas antes de calcular el promedio
        promedio = sum(entrega.calificacion for entrega in entregas) / len(entregas)
    else:
        promedio = 0  # Si no hay entregas, el promedio es 0
    
    # Mostrar resultados
    print(f"Curso: {curso.titulo} - Promedio de calificaciones: {promedio:.2f}")


 