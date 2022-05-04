from hotel.db.engine import DBSession
from hotel.db.models import DBCustomer


def read_all_customers():
    session = DBSession()
    customers = session.query(DBCustomer).all()
    return customers

def read_customer(customer_id: int):
    session = DBSession()
    customer = session.query(DBCustomer).get(customer_id)
    return customer
