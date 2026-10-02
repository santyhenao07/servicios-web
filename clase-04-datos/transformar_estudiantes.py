# Importamos librerias necesarios
import csv
import json
from pathlib import Path
RUTA_JSON = Path("salida/estudiantes_resumen.json")
print("Hola, Aplicaciones y sevicios web")

estudiantes_transformados = []
def transformar_estudiante(estudiantes):
    estudiante_nuevo = {
        'id': estudiantes['codigo'],
        'nombre_completo': f"{estudiantes['nombre']} {estudiantes['apellido']}",
        'semestre': int(estudiantes['semestre']),
        'promedio': float(estudiantes['promedio']),
        'estado': 'Activo' if estudiantes['activo'].lower() == 'true' else 'Inactivo',
    }
    return estudiante_nuevo

def serializar_estudiantes(ruta: Path, estudiantes: list[dict]) -> None:
    """Serializa una lista de diccionarios Python a un archivo JSON UTF-8."""
    ruta.parent.mkdir(exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)

def deserializar_estudiantes(ruta: Path) -> list[dict]:
    """Deserializa un archivo JSON a una lista de diccionarios Python."""
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)

# Main
with open('datos/estudiantes.csv', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for row in lector:
        estudiantes_transformados.append(transformar_estudiante(row))

serializar_estudiantes(RUTA_JSON, estudiantes_transformados)
print(f"Archivo JSON generado: {RUTA_JSON}")

estudiantes_recuperados = deserializar_estudiantes(RUTA_JSON)

print("\nDatos recuperados desde el JSON:")
print(estudiantes_recuperados[0])
print(f"Total recuperado: {len(estudiantes_recuperados)}")