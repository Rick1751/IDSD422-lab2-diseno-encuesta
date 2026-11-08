"""Auditoría descriptiva de las respuestas de la encuesta."""

from pathlib import Path

import pandas as pd


CSV_PATH = Path(__file__).resolve().parents[1] / "plantillas" / "encuesta_respuestas.csv"
INVITADOS = 30


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    print("Tipos por columna:")
    print(df.dtypes)
    print("\nDatos faltantes por columna:")
    print(df.isna().sum())

    reales = df[df["origen"].eq("real")]
    simuladas = df[df["origen"].eq("simulada")]
    respuestas_completas = len(reales)
    no_respuestas = INVITADOS - respuestas_completas
    tasa_no_respuesta = no_respuestas / INVITADOS

    print("\nResumen de recolección:")
    print(f"Personas invitadas: {INVITADOS}")
    print(f"Respuestas reales completas: {respuestas_completas}")
    print(f"Respuestas simuladas: {len(simuladas)}")
    print(f"No respuestas: {no_respuestas}")
    print(f"Tasa de no respuesta: {tasa_no_respuesta:.1%}")

    print("\nDistribución de frecuencia de compra (respuestas reales):")
    print(reales["frecuencia_compra_retailandina"].value_counts(dropna=False))
    print("\nDistribución de satisfacción de variedad saludable (respuestas reales):")
    print(reales["satisfaccion_variedad_saludable"].value_counts(dropna=False))

    print("\nInterpretación:")
    print(
        "- De 30 personas invitadas, 6 no entregaron una respuesta completa; "
        "la tasa de no respuesta es 20.0%."
    )
    print("- Muchos faltantes concentrados en un grupo también indicarían sesgo de no respuesta.")
    print("- Una concentración extrema de satisfacción alta podría indicar sesgo de respuesta.")


if __name__ == "__main__":
    main()
