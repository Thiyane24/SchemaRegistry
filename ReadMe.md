# Schema Registry

A schema management system built in Python as part of a 7-project OOP Data Engineering series. This project replicates the core concepts behind Apache Avro and the Confluent Schema Registry used with Kafka built from scratch, standard library only.

---

## What it does

Real pipelines break when schemas change without warning. A field gets renamed, a type changes, a required column gets dropped and suddenly your consumers are crashing with no clear reason why.

This project tackles that problem by giving you a system that:

- Defines and validates schemas with typed fields
- Versions schemas automatically as they evolve
- Detects and classifies changes as **breaking** or **non-breaking**
- Produces human-readable evolution reports so you always know what changed and why

---

## Project Structure

```
SchemaRegistry/
├── __init__.py
├── field.py          # Field dataclass with validation
├── base.py           # Schema dataclass with versioning support
├── ChangeType.py     # Enum for BREAKING, NON_BREAKING, NO_CHANGE
├── schemaregistry.py # Registry that stores and versions schemas
└── schemaevolution.py # Evolution engine that compares schemas
test.py
Dockerfile
README.md
```

---

## Core Classes

### Field
A single column definition. Validates that the data type is one of `int`, `str`, `float`, `bool`, `list`, or `dict`. Raises a `ValueError` on invalid input.

### Schema
A versioned collection of `Field` objects. Supports serialisation via `to_dict()` and reconstruction via `from_dict()` — a classmethod that acts as an alternative constructor.

### SchemaRegistry
Stores schemas by name and auto-increments versions on each update. Always returns the latest version by default.

### SchemaEvolution
Compares two schema versions and classifies every change:

| Change | Classification |
|---|---|
| Field removed | BREAKING |
| Field type changed | BREAKING |
| Nullable changed from True to False | BREAKING |
| New nullable field added | NON_BREAKING |
| New non-nullable field added | BREAKING |

### EvolutionReport
Structured report produced by `SchemaEvolution.compare()`. Lists every detected change with its field name and classification, and computes an overall verdict.

---

## Usage

```python
from SchemaRegistry.base import Schema
from SchemaRegistry.field import Field
from SchemaRegistry.schemaregistry import SchemaRegistry
from SchemaRegistry.schemaevolution import SchemaEvolution

# Define schemas
fields_v1 = [
    Field("user_id", "int", False),
    Field("name", "str", False),
    Field("age", "int", True)
]

fields_v2 = [
    Field("user_id", "int", False),
    Field("full_name", "str", False),  # renamed from name
    Field("age", "int", False),        # nullable changed
    Field("phone", "str", True)        # new field
]

schema_v1 = Schema("user_schema", fields_v1, 1)
schema_v2 = Schema("user_schema", fields_v2, 2)

# Register
registry = SchemaRegistry()
registry.register(schema_v1.name, schema_v1)
registry.register(schema_v2.name, schema_v2)

# Compare
evolution = SchemaEvolution()
report = evolution.compare(schema_v1, schema_v2)
report.summary()
```

**Output:**
```
----Evolution Report----
Field: name        | Change: BREAKING
Field: age         | Change: BREAKING
Field: full_name   | Change: BREAKING
Field: phone       | Change: NON_BREAKING

Overall: BREAKING
```

---

## Running with Docker

No environment setup needed. Just build and run:

```bash
docker build -t schemaregistry .
docker run schemaregistry
```

---

## Tech Stack

- Python 3.12
- OOP: abstract classes, dataclasses, enums, classmethods, properties
- Docker
- Standard library only, no third-party dependencies

---

## OOP Concepts Practised

| Concept | Where |
|---|---|
| `@dataclass` | `Field`, `Schema`, `EvolutionReport` |
| `@classmethod` | `Schema.from_dict()` as alternative constructor |
| `Enum` | `ChangeType` with fixed states |
| `@property` | `Schema.field_names` |
| Composition | `SchemaEvolution` operates on `Schema` objects without inheriting |

---

## About

Built by a Mozambican student studying at MAHSA University, Malaysia working through a hands-on OOP Data Engineering series to build real engineering intuition, one project at a time.

Project 4 of 7.
