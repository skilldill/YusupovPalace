from flask import Flask
from flask_restful import Api

from controllers import RoomsList, Room

app = Flask(__name__)
api = Api(app)

api.add_resource(RoomsList, "/rooms", endpoint='rooms')
api.add_resource(Room, "/room/<room_id>", endpoint='room')

if __name__ == '__main__':
    app.run(debug=True)