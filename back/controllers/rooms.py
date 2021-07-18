from flask_restful import Resource

class RoomsList(Resource):
    def get(self):
        return [{}, {}, {}]