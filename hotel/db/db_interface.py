from typing import Any, Dict, List, Protocol, Type

from hotel.db.engine import DBSession
from hotel.db.models import Base


DataObject = Dict[str, Any]

class DBInterface:
    def __init__(self, db_class: Type[Base]) -> None:
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        return result.dict()
    
    def read_all(self) -> List[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [r.dict() for r in results]

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)
        session.add(result)
        session.commit()
        session.refresh(result)
        return result.dict()

    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        for key, value in data.items():
            setattr(result, key, value)
        session.commit()
        session.refresh(result)
        return result.dict()
    
    def delete(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        session.delete(result)
        session.commit()
        return result.dict()
