from flask import Flask, request, make_response
from flask_restful import Resource, Api
import db_helper as db
import database_creds as creds

app = Flask(__name__)
api = Api(app)


class Quotes(Resource):
    def get(self):
        if request.authorization and request.authorization.username == creds.api_username and request.authorization.password == creds.api_password:
            connection = db.create_connection()
            results = db.get_data(connection)[0][0]
            return results
        return make_response('Could not verify!', 401, {'WWW-Authentication': 'Basic realm="Login Required"'})


api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)
