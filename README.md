☠️ PRÁCTICA: Sistema de Tripulaciones y Aventuras en One Piece

Base de Datos Relacionales — SQLite + Python + pandas
Diseño, implementación y análisis de una base de datos inspirada en el universo de One Piece.


🌊 Contexto
La Marina quiere analizar a los piratas del mundo: sus tripulaciones, recompensas, islas visitadas y combates para identificar amenazas.

🎯 Objetivos

Diseñar un esquema relacional
Crear tablas con restricciones
Insertar datos coherentes
Consultar la base de datos desde Python
Realizar un análisis básico de datos


🗂️ Estructura de la Base de Datos
Tablas
TablaDescripcióntripulacionesNombre y barco de cada tripulaciónpiratasDatos del pirata y su tripulaciónislasIslas del mundo y su marviajesRegistro de qué pirata visitó qué islacombatesEnfrentamientos entre piratas y ganadorrecompensasHistorial de recompensas por pirata
Relaciones
piratas.tripulacion_id  ──►  tripulaciones.id
viajes.pirata_id        ──►  piratas.id
viajes.isla_id          ──►  islas.id
combates.pirata1_id     ──►  piratas.id
combates.pirata2_id     ──►  piratas.id
combates.ganador_id     ──►  piratas.id
recompensas.pirata_id   ──►  piratas.id
Datos insertados
TablaMínimo requeridoInsertadosTripulaciones3✅ 3Piratas10✅ 10Islas5✅ 5Viajes15✅ 15Combates10✅ 10Recompensas10✅ 10

📋 Consultas implementadas

Piratas y su tripulación
Pirata con mayor recompensa
Número de combates ganados por pirata
Isla más visitada
Historial de recompensas por pirata


📊 Análisis (pandas)

Promedio de recompensa por tripulación
Ranking compuesto de piratas (recompensa 60% · victorias 30% · viajes 10%)


📁 Archivos del repositorio
ArchivoDescripciónonepiece_schema.sqlDDL completo: creación de tablas e inserción de datosonepiece_practica.pyScript Python con consultas y análisisresultados_consultas.txtOutput de las 5 consultas SQLresultados_analisis.txtOutput del análisis con pandaspractica_onepiece.docxDocumento de entrega completo

▶️ Cómo ejecutar
bash# Instalar dependencia
pip install pandas

# Ejecutar (crea la BD automáticamente y muestra todos los resultados)
python onepiece_practica.py

👥 Equipo
Garcia Garcia Soria López Dana Paola
Diseño de Bases de Datos — 2026-2
