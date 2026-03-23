from dataclasses import dataclass


@dataclass
class Field:
    name:str
    data_type: str
    nullable: bool = True
    default : any = None
    
    
    def __post_init__(self):
      supported= ['int','float', 'bool','list', 'dict', 'str']
      if self.data_type not in supported:
          raise ValueError("Data type is not supported")
      
        