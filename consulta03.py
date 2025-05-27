from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las tareas asignadas a los siguientes estudiantes 

# Jennifer Bolton 
# Elaine Perez
# Heather Henderson
# Charles Harris

# En función de cada tarea, presentar el número de entregas que tiene

# Lista de nombres de los estudiantes que queremos filtrar
nombres_estudiantes = ["Jennifer Bolton", "Elaine Perez", "Heather Henderson", "Charles Harris"]

tareas = (session.query(Tarea)
    .join(Entrega)  # Relacionar Tarea con Entrega
    .join(Estudiante)  # Relacionar Entrega con Estudiante
    .filter(Estudiante.nombre.in_(nombres_estudiantes))  # Filtrar por los nombres de los estudiantes
    .all())

# Diccionario para almacenar el número de entregas por tarea
resultado = {}

for tarea in tareas:
    # Contamos las entregas por cada tarea
    resultado[tarea.titulo] = len(tarea.entregas)

# Imprimimos los resultados
for titulo, num_entregas in resultado.items():
    print(f"{titulo} - {num_entregas} entregas")



 