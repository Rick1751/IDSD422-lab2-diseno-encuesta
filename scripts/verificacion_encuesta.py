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

    satisfaccion = reales["satisfaccion_variedad_saludable"]
    proporcion_satisfaccion_alta = satisfaccion.ge(4).mean()
    media_satisfaccion = satisfaccion.mean()
    calificaciones_uno = satisfaccion.eq(1).sum()
    compra_reciente = reales["compra_reciente_retailandina"]

    print("\nInterpretación:")
    print(
        f"- En las {respuestas_completas} respuestas reales, el "
        f"{proporcion_satisfaccion_alta:.1%} calificó con 4 o 5 la variedad "
        f"saludable; la media fue {media_satisfaccion:.2f} y hubo "
        f"{calificaciones_uno} calificaciones de 1."
    )
    if proporcion_satisfaccion_alta >= 0.60 and calificaciones_uno == 0:
        print(
            "- La satisfacción es alta y no hay ninguna calificación 1. Esto "
            "podría indicar sesgo de respuesta por cortesía, pero con "
            f"n={respuestas_completas} y muestreo por conveniencia no se puede confirmar."
        )
    else:
        print(
            f"- La proporción de satisfacción alta es {proporcion_satisfaccion_alta:.1%} "
            "y el patrón observado no permite confirmar un sesgo de respuesta."
        )
    print(
        f"- compra_reciente_retailandina es «Sí» en todas las {len(compra_reciente)} "
        "filas reales porque quienes respondían «No» terminaban la encuesta "
        "(filtro de elegibilidad), por lo que no aporta variación."
    )
    print(
        f"- De la no respuesta ({no_respuestas} de {INVITADOS}, "
        f"{tasa_no_respuesta:.1%}) no se registró información de quienes no "
        "respondieron, así que no se puede comprobar si se concentra en algún "
        "subgrupo; es una limitación, no una conclusión."
    )
    print(
        "- En las filas simuladas satisfaccion_variedad_saludable nunca vale 1 "
        "porque el generador usa randint(2, 5); por eso las simuladas no sirven "
        "para interpretar sesgos."
    )


if __name__ == "__main__":
    main()
