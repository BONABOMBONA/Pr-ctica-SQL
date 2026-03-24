"""
╔══════════════════════════════════════════════════════════════╗
║   ONE PIECE – Sistema de Tripulaciones y Aventuras           ║
║   Script Python: creación de BD, consultas y análisis        ║
╚══════════════════════════════════════════════════════════════╝
"""

import sqlite3
import pandas as pd

DB_PATH = "onepiece.db"

# ──────────────────────────────────────────────────────────────
# 1. CREACIÓN DE ESQUEMA Y DATOS
# ──────────────────────────────────────────────────────────────

DDL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tripulaciones (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre  TEXT    NOT NULL,
    barco   TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS piratas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          TEXT    NOT NULL,
    edad            INTEGER CHECK (edad > 0),
    recompensa      INTEGER DEFAULT 0 CHECK (recompensa >= 0),
    tripulacion_id  INTEGER NOT NULL,
    FOREIGN KEY (tripulacion_id) REFERENCES tripulaciones(id)
);

CREATE TABLE IF NOT EXISTS islas (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    mar    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS viajes (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    pirata_id INTEGER NOT NULL,
    isla_id   INTEGER NOT NULL,
    fecha     TEXT    NOT NULL,
    FOREIGN KEY (pirata_id) REFERENCES piratas(id),
    FOREIGN KEY (isla_id)   REFERENCES islas(id)
);

CREATE TABLE IF NOT EXISTS combates (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pirata1_id  INTEGER NOT NULL,
    pirata2_id  INTEGER NOT NULL,
    ganador_id  INTEGER NOT NULL,
    fecha       TEXT    NOT NULL,
    CHECK (pirata1_id <> pirata2_id),
    FOREIGN KEY (pirata1_id) REFERENCES piratas(id),
    FOREIGN KEY (pirata2_id) REFERENCES piratas(id),
    FOREIGN KEY (ganador_id) REFERENCES piratas(id)
);

CREATE TABLE IF NOT EXISTS recompensas (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    pirata_id INTEGER NOT NULL,
    monto     INTEGER NOT NULL CHECK (monto > 0),
    fecha     TEXT    NOT NULL,
    FOREIGN KEY (pirata_id) REFERENCES piratas(id)
);
"""

DATOS = {
    "tripulaciones": [
        (1, "Sombrero de Paja", "Thousand Sunny"),
        (2, "Corazon",          "Polar Tang"),
        (3, "Piratas Bestia",   "Onigashima"),
    ],
    "piratas": [
        (1,  "Monkey D. Luffy",  19, 3000000000, 1),
        (2,  "Roronoa Zoro",     21, 1111000000, 1),
        (3,  "Nami",             20,   66000000, 1),
        (4,  "Usopp",            19,  200000000, 1),
        (5,  "Vinsmoke Sanji",   21, 1032000000, 1),
        (6,  "Trafalgar Law",    26, 3000000000, 2),
        (7,  "Bepo",             23,  500000000, 2),
        (8,  "Kaido",            59, 4611100000, 3),
        (9,  "King",             47, 1390000000, 3),
        (10, "Queen",            56, 1320000000, 3),
    ],
    "islas": [
        (1, "Dressrosa",     "Grand Line"),
        (2, "Wano",          "Grand Line"),
        (3, "Marineford",    "Grand Line"),
        (4, "Enies Lobby",   "Grand Line"),
        (5, "Thriller Bark", "Grand Line"),
    ],
    "viajes": [
        (1,  1, 1, "2020-03-01"),
        (2,  1, 2, "2021-06-15"),
        (3,  1, 3, "2019-01-20"),
        (4,  2, 1, "2020-03-05"),
        (5,  2, 4, "2018-07-10"),
        (6,  2, 2, "2021-06-18"),
        (7,  3, 5, "2017-11-02"),
        (8,  3, 1, "2020-04-12"),
        (9,  4, 5, "2017-11-05"),
        (10, 4, 4, "2018-07-15"),
        (11, 5, 1, "2020-03-10"),
        (12, 5, 2, "2021-07-01"),
        (13, 6, 1, "2020-05-20"),
        (14, 6, 2, "2021-08-05"),
        (15, 7, 2, "2021-08-06"),
    ],
    "combates": [
        (1,  1, 8,  1, "2021-11-01"),
        (2,  2, 9,  2, "2021-10-28"),
        (3,  5, 10, 5, "2021-10-30"),
        (4,  1, 6,  1, "2020-06-14"),
        (5,  6, 8,  6, "2020-07-03"),
        (6,  2, 3,  2, "2019-09-01"),
        (7,  1, 4,  1, "2018-04-22"),
        (8,  3, 7,  3, "2021-08-10"),
        (9,  4, 7,  7, "2021-08-12"),
        (10, 9, 10, 9, "2021-09-05"),
    ],
    "recompensas": [
        (1,  1, 300000000,  "2016-01-01"),
        (2,  1, 1500000000, "2019-06-01"),
        (3,  1, 3000000000, "2022-01-01"),
        (4,  2, 320000000,  "2016-01-01"),
        (5,  2, 1111000000, "2022-01-01"),
        (6,  5, 177000000,  "2016-01-01"),
        (7,  5, 1032000000, "2022-01-01"),
        (8,  6, 500000000,  "2015-01-01"),
        (9,  6, 3000000000, "2022-01-01"),
        (10, 8, 4611100000, "2010-01-01"),
    ],
}


def crear_base_datos():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.executescript(DDL)

    for tabla, filas in DATOS.items():
        cols = {
            "tripulaciones": "(id, nombre, barco)",
            "piratas":       "(id, nombre, edad, recompensa, tripulacion_id)",
            "islas":         "(id, nombre, mar)",
            "viajes":        "(id, pirata_id, isla_id, fecha)",
            "combates":      "(id, pirata1_id, pirata2_id, ganador_id, fecha)",
            "recompensas":   "(id, pirata_id, monto, fecha)",
        }[tabla]
        placeholders = ",".join(["?"] * len(filas[0]))
        cur.executemany(
            f"INSERT OR IGNORE INTO {tabla} {cols} VALUES ({placeholders})", filas
        )

    con.commit()
    con.close()
    print("✅  Base de datos creada:", DB_PATH)


# ──────────────────────────────────────────────────────────────
# 2. UTILIDAD: ejecutar consulta → DataFrame
# ──────────────────────────────────────────────────────────────

def query(sql: str) -> pd.DataFrame:
    with sqlite3.connect(DB_PATH) as con:
        return pd.read_sql_query(sql, con)


# ──────────────────────────────────────────────────────────────
# 3. CONSULTAS REQUERIDAS
# ──────────────────────────────────────────────────────────────

def consulta_1_piratas_y_tripulacion():
    """1. Piratas y su tripulación"""
    sql = """
        SELECT p.nombre          AS pirata,
               p.edad,
               p.recompensa,
               t.nombre          AS tripulacion,
               t.barco
        FROM piratas p
        JOIN tripulaciones t ON p.tripulacion_id = t.id
        ORDER BY p.recompensa DESC;
    """
    df = query(sql)
    print("\n═══ CONSULTA 1 · Piratas y su Tripulación ═══")
    print(df.to_string(index=False))
    return df


def consulta_2_mayor_recompensa():
    """2. Pirata con mayor recompensa"""
    sql = """
        SELECT p.nombre    AS pirata,
               t.nombre    AS tripulacion,
               p.recompensa
        FROM piratas p
        JOIN tripulaciones t ON p.tripulacion_id = t.id
        ORDER BY p.recompensa DESC
        LIMIT 1;
    """
    df = query(sql)
    print("\n═══ CONSULTA 2 · Pirata con Mayor Recompensa ═══")
    print(df.to_string(index=False))
    return df


def consulta_3_combates_ganados():
    """3. Número de combates ganados por pirata"""
    sql = """
        SELECT p.nombre    AS pirata,
               COUNT(c.id) AS victorias
        FROM piratas p
        LEFT JOIN combates c ON c.ganador_id = p.id
        GROUP BY p.id
        ORDER BY victorias DESC;
    """
    df = query(sql)
    print("\n═══ CONSULTA 3 · Combates Ganados por Pirata ═══")
    print(df.to_string(index=False))
    return df


def consulta_4_isla_mas_visitada():
    """4. Isla más visitada"""
    sql = """
        SELECT i.nombre AS isla,
               i.mar,
               COUNT(v.id) AS visitas
        FROM islas i
        JOIN viajes v ON v.isla_id = i.id
        GROUP BY i.id
        ORDER BY visitas DESC;
    """
    df = query(sql)
    print("\n═══ CONSULTA 4 · Islas Más Visitadas ═══")
    print(df.to_string(index=False))
    return df


def consulta_5_historial_recompensas():
    """5. Historial de recompensas por pirata"""
    sql = """
        SELECT p.nombre    AS pirata,
               r.monto,
               r.fecha
        FROM recompensas r
        JOIN piratas p ON r.pirata_id = p.id
        ORDER BY p.nombre, r.fecha;
    """
    df = query(sql)
    print("\n═══ CONSULTA 5 · Historial de Recompensas por Pirata ═══")
    print(df.to_string(index=False))
    return df


# ──────────────────────────────────────────────────────────────
# 4. ANÁLISIS CON PANDAS
# ──────────────────────────────────────────────────────────────

def analisis_promedio_recompensa_tripulacion():
    """Promedio de recompensa por tripulación"""
    sql = """
        SELECT t.nombre        AS tripulacion,
               p.nombre        AS pirata,
               p.recompensa
        FROM piratas p
        JOIN tripulaciones t ON p.tripulacion_id = t.id;
    """
    df = query(sql)

    resumen = (
        df.groupby("tripulacion")["recompensa"]
        .agg(miembros="count", promedio="mean", total="sum", maximo="max")
        .reset_index()
    )
    resumen["promedio"] = resumen["promedio"].round(0).astype(int)
    resumen["total"]    = resumen["total"].astype(int)
    resumen["maximo"]   = resumen["maximo"].astype(int)

    print("\n═══ ANÁLISIS · Promedio de Recompensa por Tripulación ═══")
    print(resumen.to_string(index=False))
    return resumen


def analisis_ranking_piratas():
    """Ranking de piratas (recompensa + victorias + viajes)"""
    recompensas_df = query("""
        SELECT p.id,
               p.nombre          AS pirata,
               t.nombre          AS tripulacion,
               p.recompensa
        FROM piratas p
        JOIN tripulaciones t ON p.tripulacion_id = t.id;
    """)

    victorias_df = query("""
        SELECT ganador_id AS id, COUNT(*) AS victorias
        FROM combates
        GROUP BY ganador_id;
    """)

    viajes_df = query("""
        SELECT pirata_id AS id, COUNT(*) AS viajes
        FROM viajes
        GROUP BY pirata_id;
    """)

    df = (
        recompensas_df
        .merge(victorias_df, on="id", how="left")
        .merge(viajes_df,    on="id", how="left")
        .fillna(0)
    )
    df["victorias"] = df["victorias"].astype(int)
    df["viajes"]    = df["viajes"].astype(int)

    # Puntuación compuesta (normalizada)
    df["score_recompensa"] = df["recompensa"] / df["recompensa"].max()
    df["score_victorias"]  = df["victorias"]  / (df["victorias"].max() or 1)
    df["score_viajes"]     = df["viajes"]     / (df["viajes"].max() or 1)
    df["puntuacion"]       = (
        df["score_recompensa"] * 0.6 +
        df["score_victorias"]  * 0.3 +
        df["score_viajes"]     * 0.1
    ).round(4)

    ranking = (
        df[["pirata", "tripulacion", "recompensa", "victorias", "viajes", "puntuacion"]]
        .sort_values("puntuacion", ascending=False)
        .reset_index(drop=True)
    )
    ranking.index += 1
    ranking.index.name = "rank"

    print("\n═══ ANÁLISIS · Ranking de Piratas ═══")
    print(ranking.to_string())
    return ranking


# ──────────────────────────────────────────────────────────────
# 5. MAIN
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    crear_base_datos()

    print("\n" + "=" * 60)
    print("  PARTE 6: CONSULTAS REQUERIDAS")
    print("=" * 60)
    df_c1 = consulta_1_piratas_y_tripulacion()
    df_c2 = consulta_2_mayor_recompensa()
    df_c3 = consulta_3_combates_ganados()
    df_c4 = consulta_4_isla_mas_visitada()
    df_c5 = consulta_5_historial_recompensas()

    print("\n" + "=" * 60)
    print("  PARTE 7: ANÁLISIS")
    print("=" * 60)
    df_a1 = analisis_promedio_recompensa_tripulacion()
    df_a2 = analisis_ranking_piratas()

    print("\n✅  Práctica completada.")
