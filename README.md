# ☠️ PRÁCTICA: Sistema de Tripulaciones y Aventuras en One Piece

> **Base de Datos Relacionales — SQLite + Python + pandas**  
> Diseño, implementación y análisis de una base de datos inspirada en el universo de One Piece.

---

## 🌊 Contexto

La Marina quiere analizar a los piratas del mundo: sus tripulaciones, recompensas, islas visitadas y combates para **identificar amenazas**.

---

## 🎯 Objetivos

- Diseñar un esquema relacional
- Crear tablas con restricciones
- Insertar datos coherentes
- Consultar la base de datos desde Python
- Realizar un análisis básico de datos

---

## 🗂️ Estructura de la Base de Datos

### Tablas

| Tabla | Descripción |
|---|---|
| `tripulaciones` | Nombre y barco de cada tripulación |
| `piratas` | Datos del pirata y su tripulación |
| `islas` | Islas del mundo y su mar |
| `viajes` | Registro de qué pirata visitó qué isla |
| `combates` | Enfrentamientos entre piratas y ganador |
| `recompensas` | Historial de recompensas por pirata |

### Relaciones

```
piratas.tripulacion_id  ──►  tripulaciones.id
viajes.pirata_id        ──►  piratas.id
viajes.isla_id          ──►  islas.id
combates.pirata1_id     ──►  piratas.id
combates.pirata2_id     ──►  piratas.id
combates.ganador_id     ──►  piratas.id
recompensas.pirata_id   ──►  piratas.id
```

### Datos insertados

| Tabla | Mínimo requerido | Insertados |
|---|:---:|:---:|
| Tripulaciones | 3 | ✅ 3 |
| Piratas | 10 | ✅ 10 |
| Islas | 5 | ✅ 5 |
| Viajes | 15 | ✅ 15 |
| Combates | 10 | ✅ 10 |
| Recompensas | 10 | ✅ 10 |

---

## 📋 Consultas implementadas

1. Piratas y su tripulación
2. Pirata con mayor recompensa
3. Número de combates ganados por pirata
4. Isla más visitada
5. Historial de recompensas por pirata

---

## 📊 Análisis (pandas)

- Promedio de recompensa por tripulación
- Ranking compuesto de piratas *(recompensa 60% · victorias 30% · viajes 10%)*

---

## 📁 Archivos del repositorio

| Archivo | Descripción |
|---|---|
| `onepiece_schema.sql` | DDL completo: creación de tablas e inserción de datos |
| `onepiece_practica.py` | Script Python con consultas y análisis |
| `resultados_consultas.txt` | Output de las 5 consultas SQL |
| `resultados_analisis.txt` | Output del análisis con pandas |
| `practica_onepiece.docx` | Documento de entrega completo |

---

## 👥 Equipo

**Garcia Garcia Soria López Dana Paola**  
Diseño de Bases de Datos — 2026-2
