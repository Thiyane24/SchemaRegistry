from SchemaRegistry.ChangeType import ChangeType

class SchemaEvolution():
    def compare(self, old, new):
        pass
    
    def _check_removed_fields(self,old,new):
        removed_fields = []
        for field in old.fields:
            if field.name not in new.field_names:
                removed_fields.append((field.name,ChangeType.BREAKING))
        
        return removed_fields
    
    def _check_type_changes(self,old,new):
        changed = []
        for field in old.fields:
            new_field = new.get_field(field.name)
            if new_field is not None and field.data_type != new_field.data_type :
                changed.append((field.data_type, ChangeType.BREAKING))
        return changed