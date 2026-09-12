from pathlib import Path
import pandas as pd

INPUT_FILE = Path("data/raw/dataset.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "dataset_clean.csv"


def clean_data():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include="number").columns
    text_columns = df.select_dtypes(include="object").columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    for column in text_columns:
        mode = df[column].mode()
        if not mode.empty:
            df[column] = df[column].fillna(mode.iloc[0])
        else:
            df[column] = df[column].fillna("desconocido")

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Archivo generado: {OUTPUT_FILE}")
    print(f"Filas: {len(df)}")
    print(f"Columnas: {len(df.columns)}")
    print(f"Nulos restantes: {int(df.isna().sum().sum())}")


if __name__ == "__main__":
    clean_data()