"""Genera respuestas simuladas para probar la auditoría de la encuesta."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path


OUTPUT_PATH = Path(__file__).resolve().parents[1] / "plantillas" / "encuesta_simulada.csv"
FIELDS = [
    "respuesta_id",
    "fecha",
    "edad",
    "ocupacion",
    "compra_reciente_retailandina",
    "frecuencia_compra_retailandina",
    "frecuencia_ultraprocesados",
    "comer_distraido_pantallas",
    "tiempo_promedio_almuerzo",
    "lectura_etiquetas",
    "planificacion_menu_semanal",
    "satisfaccion_variedad_saludable",
    "origen",
]


def main() -> None:
    rng = random.Random(422)
    options = {
        "ocupacion": ["Estudiante", "Trabajador", "Ambos"],
        "frecuencia": [
            "Varias veces por semana",
            "Semanal",
            "Quincenal",
            "Mensual",
            "Menos de una vez al mes",
        ],
        "etiquetas": [
            "Ingredientes",
            "Tabla nutricional",
            "Sellos frontales",
            "Ingredientes;Tabla nutricional",
            "Ingredientes;Sellos frontales",
            "Tabla nutricional;Sellos frontales",
            "Ninguna",
        ],
    }
    start = date(2026, 11, 4)
    rows = []
    for index in range(1, 101):
        rows.append(
            {
                "respuesta_id": f"S{index:03d}",
                "fecha": (start + timedelta(days=(index - 1) // 4)).isoformat(),
                "edad": rng.randint(18, 25),
                "ocupacion": rng.choice(options["ocupacion"]),
                "compra_reciente_retailandina": "Sí",
                "frecuencia_compra_retailandina": rng.choice(options["frecuencia"]),
                "frecuencia_ultraprocesados": rng.randint(1, 5),
                "comer_distraido_pantallas": float(rng.randrange(0, 101, 5)),
                "tiempo_promedio_almuerzo": rng.randrange(15, 61, 5),
                "lectura_etiquetas": rng.choice(options["etiquetas"]),
                "planificacion_menu_semanal": rng.randint(1, 4),
                "satisfaccion_variedad_saludable": rng.randint(2, 5),
                "origen": "simulada",
            }
        )

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Se generaron {len(rows)} respuestas simuladas en {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
