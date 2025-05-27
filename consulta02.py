from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 .
# En función de los departamentos, presentar el nombre del departamento y el número
# de cursos que tiene cada departamento
departamentos = (session.query(Departamento)  
    .join(Curso)  # Relacionar Departamento con Curso
    .join(Tarea)  # Relacionar Curso con Tarea
    .join(Entrega)  # Relacionar Tarea con Entrega
    .filter(Entrega.calificacion <= 0.3)  # Filtrar solo las entregas con calificación <= 0.3
    .all())

# Diccionario para almacenar el nombre del departamento y la cantidad de cursos
resultado = {}

for departamento in departamentos:
    # Contamos la cantidad de cursos en el departamento
    resultado[departamento.nombre] = len(departamento.cursos)

# Imprimimos los resultados
for nombre, num_cursos in resultado.items():
    print(f"{nombre} - {num_cursos} cursos")




 