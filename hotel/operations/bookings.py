from datetime import date
from pydantic import BaseModel

from hotel.operations.interface import DataInterface, DataObject


class InvalidDatesException(Exception):
    pass

class BookingCreateData(BaseModel):
    from_date: date
    to_date: date
    room_id: int
    customer_id: int

def read_all_bookings(booking_interface: DataInterface):
    return booking_interface.read_all()

def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)

def create_booking(
    data: BookingCreateData,
    booking_interface: DataInterface,
    room_interface: DataInterface
) -> DataObject:
    # get room by id with interface
    room = room_interface.read_by_id(data.room_id)
    
    # calculate length of stay in days
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDatesException("Invalid dates.")
    
    # convert booking data into dict and add price
    booking_dict = data.dict()
    booking_dict["price"] = days * room["price"]

    # return newly created booking
    return booking_interface.create(booking_dict)

def delete_booking(booking_id, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)
