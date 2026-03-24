from dataclasses import dataclass, asdict
from SchemaRegistry.field import Field 

@dataclass
class Schema:
    name : str
    fields : list
    version : int = 1
    
  
    def to_dict(self):
        return{
            "name": self.name,
            "version": self.version,
            "fields": [asdict(field) for field in self.fields]
        }
    
    @classmethod
    def from_dict(cls,d):
        name = d["name"]
        version = d["version"]
        fields = [Field(**f) for f in d["fields"]]
        return cls(name, fields, version)
        
        
    def get_field(self, name):
        for field in self.fields:
            if field.name == name:
                return field
        return None
            
    @property
    def field_names(self):
        return [field.name for field in self.fields]