from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api,reqparse


app = Flask(__name__)
api = Api(app)
CORS(app)

class Retrieve(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('latitude',type=float,required=True)
        parser.add_argument('longitude',type=float,required=True)
        args = parser.parse_args()
        try:
            return jsonify(args)
        except Exception as err:
            error_message = traceback.format_exc()
            return error_message
api.add_resource(Retrieve, '/retrieve')

class Store(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('make')
        parser.add_argument('model')
        parser.add_argument('length')
        parser.add_argument('latitude')
        parser.add_argument('longitude')
        args = parser.parse_args()
        try:
            return args
        except Exception as err:
            error_message = traceback.format_exc()
            return error_message
api.add_resource(Store, '/store')



@app.route("/")
def index():
    return 'HarborMoor API'


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True) #, , port=80 debug=True