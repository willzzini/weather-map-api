from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger

from resources.city import City, CityList

app = Flask(__name__)
cors = CORS(app, resorces={r'/*': {"origins": '*'}})
app.config['CORS_HEADERS'] = 'application/json'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'EiEiO'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['SWAGGER'] = {
    "uiversion": 3,
    "swagger_version": "3.0",
    "title": "Weather Map API",
    "specs_route": "/weather-api-docs/",
    "description": "This is the version 1 weather-map API",
}

Swagger(app)

api.add_resource(City, '/city')
api.add_resource(CityList, '/cities')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=8000, debug=True)
