from SchemaRegistry.schemaregistry import SchemaRegistry
from SchemaRegistry.base import Schema
from SchemaRegistry.field import Field


field1 = Field("Age", "int", True, None)
schema1 = Schema("Schema1", [field1], 1)
field2 = Field("Name", "str", False, None)
schema2 = Schema("Schema1", [field2], 2)


schema_registry= SchemaRegistry()

schema_registry.register(schema1.name, schema1)
schema_registry.register(schema2.name, schema2)
print(schema_registry.get("Schema1"))

print(schema_registry.list_versions("Schema1"))
print(schema_registry.list_schemas())
