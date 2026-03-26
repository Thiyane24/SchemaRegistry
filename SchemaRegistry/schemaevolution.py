from SchemaRegistry.ChangeType import ChangeType
from dataclasses import dataclass


class SchemaEvolution():
    
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
                changed.append((field.name, ChangeType.BREAKING))
        return changed
    
    def _check_nullable_changes(self,old,new):
        null_changes = []
        for field in old.fields:
            new_field = new.get_field(field.name)
            if new_field is not None and field.nullable == True and  new_field.nullable == False:
                null_changes.append((field.name, ChangeType.BREAKING))
        return null_changes
    
    def _check_added_fields(self,old,new):
        added= []
        for field in new.fields:
            if field.name not in old.field_names and field.nullable == True :
                added.append((field.name, ChangeType.NON_BREAKING))
            elif field.name not in old.field_names and  field.nullable == False:
                added.append((field.name, ChangeType.BREAKING))
        return added
    
    
    def compare(self,old,new):
        removed = self._check_removed_fields(old,new)
        type1 =self._check_type_changes(old,new)   
        null = self._check_nullable_changes(old,new)
        add = self._check_added_fields(old,new)
        change = removed + type1 + null + add
        if change == []:
            overall_type= ChangeType.NO_CHANGE.name
        elif any(c[1] == ChangeType.BREAKING for c in change):
            overall_type =  ChangeType.BREAKING.name
        else:
            overall_type= ChangeType.NON_BREAKING.name
        
        return EvolutionReport(changes = change, overall_type= overall_type)

@dataclass
class EvolutionReport:
    changes: list
    overall_type: ChangeType
        
    def summary(self):
        print("\n----Evolution Report----")
        for change in self.changes:
            print(f"Field:{change[0]} | Change: {change[1].name}")

