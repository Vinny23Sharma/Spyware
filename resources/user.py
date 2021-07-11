from flask_cors import cross_origin
from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel

class Data(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('key_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('data',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = Data.parser.parse_args()
        user = UserModel(data['key_name'], data['data'])
        user.save_to_db()


class Data_info(Resource):
    def get(self):
        return {'Data': list(map(lambda x: x.json(), UserModel.query.all()))}
