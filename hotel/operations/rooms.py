from hotel.db.engine import DBSession
from hotel.db.models import DBRoom


def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return rooms
