-- ============================================================
--  ONE PIECE - Sistema de Tripulaciones y Aventuras
--  Script SQL completo: esquema + datos
-- ============================================================

PRAGMA foreign_keys = ON;

-- ------------------------------------------------------------
-- 1. TRIPULACIONES
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tripulaciones (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre  TEXT    NOT NULL,
    barco   TEXT    NOT NULL
);

-- ------------------------------------------------------------
-- 2. PIRATAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS piratas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          TEXT    NOT NULL,
    edad            INTEGER CHECK (edad > 0),
    recompensa      INTEGER DEFAULT 0 CHECK (recompensa >= 0),
    tripulacion_id  INTEGER NOT NULL,
    FOREIGN KEY (tripulacion_id) REFERENCES tripulaciones(id)
);

-- ------------------------------------------------------------
-- 3. ISLAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS islas (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    mar    TEXT NOT NULL
);

-- ------------------------------------------------------------
-- 4. VIAJES
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS viajes (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    pirata_id INTEGER NOT NULL,
    isla_id   INTEGER NOT NULL,
    fecha     TEXT    NOT NULL,
    FOREIGN KEY (pirata_id) REFERENCES piratas(id),
    FOREIGN KEY (isla_id)   REFERENCES islas(id)
);

-- ------------------------------------------------------------
-- 5. COMBATES
-- ------------------------------------------------------------
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

-- ------------------------------------------------------------
-- 6. RECOMPENSAS  (historial)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS recompensas (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    pirata_id INTEGER NOT NULL,
    monto     INTEGER NOT NULL CHECK (monto > 0),
    fecha     TEXT    NOT NULL,
    FOREIGN KEY (pirata_id) REFERENCES piratas(id)
);

-- ============================================================
--  DATOS
-- ============================================================

-- Tripulaciones (3)
INSERT INTO tripulaciones (nombre, barco) VALUES
    ('Sombrero de Paja',  'Thousand Sunny'),
    ('Corazon',           'Polar Tang'),
    ('Piratas Bestia',    'Onigashima');

-- Piratas (10)
INSERT INTO piratas (nombre, edad, recompensa, tripulacion_id) VALUES
    ('Monkey D. Luffy',   19, 3000000000, 1),
    ('Roronoa Zoro',      21, 1111000000, 1),
    ('Nami',              20,   66000000, 1),
    ('Usopp',             19,  200000000, 1),
    ('Vinsmoke Sanji',    21, 1032000000, 1),
    ('Trafalgar Law',     26, 3000000000, 2),
    ('Bepo',              23,   500000000, 2),
    ('Kaido',             59, 4611100000, 3),
    ('King',              47, 1390000000, 3),
    ('Queen',             56, 1320000000, 3);

-- Islas (5)
INSERT INTO islas (nombre, mar) VALUES
    ('Dressrosa',      'Grand Line'),
    ('Wano',           'Grand Line'),
    ('Marineford',     'Grand Line'),
    ('Enies Lobby',    'Grand Line'),
    ('Thriller Bark',  'Grand Line');

-- Viajes (15)
INSERT INTO viajes (pirata_id, isla_id, fecha) VALUES
    (1, 1, '2020-03-01'),
    (1, 2, '2021-06-15'),
    (1, 3, '2019-01-20'),
    (2, 1, '2020-03-05'),
    (2, 4, '2018-07-10'),
    (2, 2, '2021-06-18'),
    (3, 5, '2017-11-02'),
    (3, 1, '2020-04-12'),
    (4, 5, '2017-11-05'),
    (4, 4, '2018-07-15'),
    (5, 1, '2020-03-10'),
    (5, 2, '2021-07-01'),
    (6, 1, '2020-05-20'),
    (6, 2, '2021-08-05'),
    (7, 2, '2021-08-06');

-- Combates (10)
INSERT INTO combates (pirata1_id, pirata2_id, ganador_id, fecha) VALUES
    (1, 8,  1, '2021-11-01'),
    (2, 9,  2, '2021-10-28'),
    (5, 10, 5, '2021-10-30'),
    (1, 6,  1, '2020-06-14'),
    (6, 8,  6, '2020-07-03'),
    (2, 3,  2, '2019-09-01'),
    (1, 4,  1, '2018-04-22'),
    (3, 7,  3, '2021-08-10'),
    (4, 7,  7, '2021-08-12'),
    (9, 10, 9, '2021-09-05');

-- Recompensas (10) — historial de actualizaciones
INSERT INTO recompensas (pirata_id, monto, fecha) VALUES
    (1, 300000000,  '2016-01-01'),
    (1, 1500000000, '2019-06-01'),
    (1, 3000000000, '2022-01-01'),
    (2, 320000000,  '2016-01-01'),
    (2, 1111000000, '2022-01-01'),
    (5, 177000000,  '2016-01-01'),
    (5, 1032000000, '2022-01-01'),
    (6, 500000000,  '2015-01-01'),
    (6, 3000000000, '2022-01-01'),
    (8, 4611100000, '2010-01-01');
