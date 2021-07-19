from flask_restful import Resource
from utils import get_cursor

class RoomsList(Resource):
    def get(self):
        query = '''
            SELECT * FROM rooms 
        '''

        cursor = get_cursor('data.db')
        cursor.execute(query)

        rooms = cursor.fetchall()

        return rooms