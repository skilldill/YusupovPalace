from flask_restful import Resource
from utils import get_cursor
class Room(Resource):
    def get(self, room_id):
        query = '''
            SELECT room_id, description, audio, photo
            FROM rooms_data
            WHERE room_id = (?)
        '''

        cursor = get_cursor('data.db')
        cursor.execute(query, (room_id,))
        room_data = cursor.fetchone()

        return room_data