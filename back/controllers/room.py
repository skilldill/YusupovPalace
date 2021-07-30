from flask_restful import Resource, request, abort
from utils import get_cursor, map_room
from env import APP_KEY

class Room(Resource):
    def get(self, room_id):
        app_key = request.headers['appKey']

        if app_key != APP_KEY:
            return abort(403, message='Forbidden')

        query = '''
            SELECT room_id, name, description, audio, photo
            FROM rooms_data
            WHERE room_id = (?)
        '''

        cursor = get_cursor('data.db')
        cursor.execute(query, (room_id,))
        room_data = cursor.fetchone()

        return map_room(room_data)