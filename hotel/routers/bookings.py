from fastapi import APIRouter

from hotel.operations.bookings import read_all_bookings, read_booking, create_booking, delete_booking, BookingCreateData


router = APIRouter()

@router.get("/bookings")
def api_read_all_bookings():
    return read_all_bookings()

@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    return read_booking(booking_id)

@router.post("/booking")
def api_create_booking(data: BookingCreateData):
    return create_booking(data)

@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id):
    return delete_booking(booking_id)
