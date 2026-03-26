from SchemaRegistry.schemaregistry import SchemaRegistry
from SchemaRegistry.base import Schema
from SchemaRegistry.field import Field
from SchemaRegistry.schemaevolution import SchemaEvolution
from SchemaRegistry.ChangeType import ChangeType

# Create schemas
fields_v1 = [
    Field("user_id", "int", False, None),
    Field("name", "str", False, None),
    Field("age", "int", True, None)
]
schema_v1 = Schema("user_schema", fields_v1, 1)

fields_v2 = [
    Field("user_id", "int", False, None),
    Field("first_name","str", False,None),
    Field("last_name", "str", False, None),
    Field("age", "int", False, None),        # nullable changed to False
    Field("phone", "str", True, None)        # new field
]
schema_v2 = Schema("user_schema", fields_v2, 2)

# Register
registry = SchemaRegistry()
registry.register(schema_v1.name, schema_v1)
registry.register(schema_v2.name, schema_v2)

# Test registry
print("Latest schema:", registry.get("user_schema").version)
print("Versions:", registry.list_versions("user_schema"))
print("All schemas:", registry.list_schemas())

# Test evolution
evolution = SchemaEvolution()
report = evolution.compare(schema_v1, schema_v2)

print("\nOverall Type:", report.overall_type)
report.summary()