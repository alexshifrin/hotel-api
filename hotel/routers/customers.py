from fastapi import APIRouter

from hotel.operations.customers import CustomerUpdateData, read_all_customers, read_customer, create_customer, CustomerCreateData, update_customer


router = APIRouter()

@router.get("/customers")
def api_read_all_customers():
    return read_all_customers()

@router.get("/customer/{customer_id}")
def api_read_customer(customer_id):
    return read_customer(customer_id)

@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)

@router.put("/customer/{customer_id}")
def api_update_customer(customer_id: int, data: CustomerUpdateData):
    return update_customer(customer_id, data)
