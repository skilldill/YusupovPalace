from flask_restful import Resource, request, abort
from utils import get_cursor, map_rooms
from env import APP_KEY
class RoomsList(Resource):
    def get(self):
        app_key = request.headers['appKey']

        if app_key != APP_KEY:
            abort(403, message='Forbidden')

        query = '''
            SELECT * FROM rooms 
        '''

        cursor = get_cursor('data.db')
        cursor.execute(query)

        rooms = cursor.fetchall()

        return map_rooms(rooms)