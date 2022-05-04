from pydantic import BaseModel

from hotel.db.engine import DBSession
from hotel.db.models import DBCustomer


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str

def read_all_customers():
    session = DBSession()
    customers = session.query(DBCustomer).all()
    return customers

def read_customer(customer_id: int):
    session = DBSession()
    customer = session.query(DBCustomer).get(customer_id)
    return customer

def create_customer(data: CustomerCreateData):
    session = DBSession()
    customer = DBCustomer(**data.dict())
    session.add(customer)
    session.commit()
    return customer
