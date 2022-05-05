from datetime import date
from pydantic import BaseModel

from hotel.db.engine import DBSession
from hotel.db.models import DBBooking, DBRoom


class InvalidDatesException(Exception):
    pass

class BookingCreateData(BaseModel):
    from_date: date
    to_date: date
    room_id: int
    customer_id: int

def read_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return bookings

def read_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    return booking

def create_booking(data: BookingCreateData):
    session = DBSession()
    booking_dict = data.dict()
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDatesException("Invalid dates.")
    room = session.query(DBRoom).get(data.room_id)
    booking_dict["price"] = days * room.price
    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    session.refresh(booking)
    return booking

def delete_booking(booking_id):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return booking