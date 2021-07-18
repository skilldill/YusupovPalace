from flask_restful import Resource

class Room(Resource):
    def get(self, room_id):
        return {'name': 'Столовая', 'id': room_id, 'description': 'sample room'}