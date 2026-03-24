PRACTICA: Sistema de Tripulaciones y Aventuras en One Piece

Contexto:
La Marina quiere analizar a los piratas del mundo: sus tripulaciones, recompensas, islas visitadas y combates para identificar amenazas.

Objetivo:
- Diseñar un esquema relacional
- Crear tablas con restricciones
- Insertar datos coherentes
- Consultar la base de datos desde Python
- Realizar un análisis básico de datos

Parte 1: Diseño de la base de datos

Tablas a crear:

1. tripulaciones
Columnas:
- id
- nombre
- barco
Ejemplo:
1, Sombrero de Paja, Going Merry

2. piratas
Columnas:
- id
- nombre
- edad
- recompensa
- tripulacion_id
Ejemplo:
1, Monkey D. Luffy, 19, 1500000000, 1

3. islas
Columnas:
- id
- nombre
- mar
Ejemplo:
1, Dressrosa, Grand Line

4. viajes
Columnas:
- id
- pirata_id
- isla_id
- fecha
Ejemplo:
1, 1, 1, 2023-01-10

5. combates
Columnas:
- id
- pirata1_id
- pirata2_id
- ganador_id
- fecha
Ejemplo:
1, 1, 2, 1, 2023-02-01

6. recompensas
Columnas:
- id
- pirata_id
- monto
- fecha
Ejemplo:
1, 1, 500000000, 2020-01-01

Parte 2: Relaciones

- piratas.tripulacion_id -> tripulaciones.id
- viajes.pirata_id -> piratas.id
- viajes.isla_id -> islas.id
- combates.pirata1_id -> piratas.id
- combates.pirata2_id -> piratas.id
- combates.ganador_id -> piratas.id
- recompensas.pirata_id -> piratas.id

Parte 3: Creación de la base de datos

Requisitos:
- Usar SQLite o similar
- Definir PRIMARY KEY y FOREIGN KEY
- Crear al menos:
  - 3 tripulaciones
  - 10 piratas
  - 5 islas
  - 15 viajes
  - 10 combates
  - 10 recompensas

Parte 4: Inserción de datos

- Generar datos coherentes
- Mantener integridad referencial

Parte 5: Uso en Python

- Conectar a la base de datos
- Ejecutar consultas SQL
- Usar pandas para análisis

Parte 6: Consultas requeridas

1. Piratas y su tripulación
2. Pirata con mayor recompensa
3. Numero de combates ganados por pirata
4. Isla más visitada
5. Historial de recompensas por pirata

Parte 7: Análisis

- Promedio de recompensa por tripulación
- Ranking de piratas

Entregables:

1. Script SQL
2. Script o notebook en Python
3. Resultados de consultas
4. Resultados del Análisis

EQUIPO:
Garcia Garcia
Soria Lòpez Dana Paola
