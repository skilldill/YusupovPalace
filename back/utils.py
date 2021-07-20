import sqlite3

def get_cursor(db):
    conn = sqlite3.connect(db, check_same_thread=False)
    return conn.cursor()

def map_room(room):
    room_obj = {
        "id": room[0],
        "name": room[1],
        "description": room[2],
        "audio": room[3],
        "photo": room[4]
    }

    return room_obj


def map_rooms(rooms):
    maped_rooms = []

    for room in rooms:
        maped_rooms.append({
            "id": room[0], 
            "name": room[1],
            "preview": room[2]
        })

    return maped_rooms