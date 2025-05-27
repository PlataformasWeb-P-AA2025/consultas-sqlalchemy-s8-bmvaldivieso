from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte.
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento
entregas = (session.query(Entrega)
    .join(Tarea)  # Relacionar Entrega con Tarea
    .join(Estudiante)  # Relacionar Entrega con Estudiante
    .join(Inscripcion, Inscripcion.estudiante_id == Estudiante.id)  # Relacionar Estudiante con Inscripción
    .join(Curso, Curso.id == Inscripcion.curso_id)  # Relacionar Inscripción con Curso
    .join(Departamento, Departamento.id == Curso.departamento_id)  # Relacionar Curso con Departamento
    .join(Instructor, Instructor.id == Curso.instructor_id)  # Relacionar Curso con Instructor
    .filter(Departamento.nombre.like("%Arte%"))  # Filtrar solo por departamento de Arte
    .all())

for entrega in entregas:
    print(f"{entrega.tarea.titulo} - {entrega.estudiante.nombre} - {entrega.calificacion} - {entrega.tarea.curso.instructor.nombre} - {entrega.tarea.curso.departamento.nombre}")


 