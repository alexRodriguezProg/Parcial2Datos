import pandas as pd
from sqlalchemy import create_engine, text

# ── Crear la base de datos como root ─────────────────────────
engine_root = create_engine('mysql+pymysql://root:123456@localhost:3306/')

with engine_root.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS vuelos2024"))
    conn.execute(text("GRANT ALL PRIVILEGES ON vuelos2024.* TO 'grafanar'@'%'"))
    conn.commit()

# ── Cargar el CSV en vuelos2024 ───────────────────────────────
engine = create_engine('mysql+pymysql://grafanar:123456@localhost:3306/vuelos2024')

df = pd.read_csv('flight_data_2024(act).csv', sep=';')

df.to_sql('flights', con=engine, if_exists='replace', index=False)

print(f"✓ Cargadas {len(df)} filas en la tabla 'flights' (base: vuelos2024)")
