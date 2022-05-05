from typing import Any, Dict, List, Protocol


DataObject = Dict[str, Any]

class DataInterface(Protocol):
    def read_by_id(self, id: int) -> DataObject:
        ...
    
    def read_all(self) -> List[DataObject]:
        ...

    def create(self, data: DataObject) -> DataObject:
        ...

    def update(self, id: int, data: DataObject) -> DataObject:
        ...
    
    def delete(self, id: int) -> DataObject:
        ...
