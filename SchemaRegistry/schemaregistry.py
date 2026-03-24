class SchemaRegistry:
    def __init__(self):
        self.schemas = {}
    
    def register(self,name, schema):
        if name in self.schemas:
            current_version = max(self.schemas[name])
            new_version = current_version + 1
            self.schemas[name][new_version]= schema
        else:
            self.schemas[name]= {1: schema}
            
    def get(self, name, version = None):
        if name not in self.schemas:
            raise KeyError("Name does not exist")
        if version == None:
           latest_version = max(self.schemas[name])
           return self.schemas[name][latest_version]
        else:
            return self.schemas[name][version]
        
        
    def list_versions(self, name):
        return self.schemas[name].keys()
    
    def list_schemas(self):
        return self.schemas.keys()
    
    def delete(self,name):
        del self.schemas[name]
        
        
    