from flask import Flask, request
from flask_cors import CORS
from flask.views import MethodView
import json

from services.find_moves import find_moves

app = Flask(__name__)

class FindMoves(MethodView):
    def post(self):
        board = json.loads(request.data)
        # print (board['1']['a'])
        return find_moves(board)

app.add_url_rule('/findmoves', view_func=FindMoves.as_view('findmoves'))

# enables cors
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
