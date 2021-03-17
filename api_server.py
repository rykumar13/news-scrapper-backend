from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
import db_helper as db


class Quotes(Resource):
    def get(self):
        connection = db.create_connection()
        results = db.get_data(connection)[0][0]
        print(results)
        return results


api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)