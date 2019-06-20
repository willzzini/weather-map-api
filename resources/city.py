from flask_restful import Resource, reqparse
from security import require_appkey
from flasgger import swag_from
from models.city import CityModel
from weather.weather_map import city_weather, city_weather_forecast
from flask import request


class City(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'city_name',
        type=str,
        required=True,
        help="Every cities needs a name."
    )

    @swag_from("../docs/cities/cities_post.yml")
    @require_appkey
    def post(self):
        data = City.parser.parse_args()
        xapi_key = request.headers.get('X-Api-Key')
        if CityModel.find_by_city_name(data['city_name']):
            return {
                'message':
                "An city with this name '{}' already exists.".format(
                    data['city_name'])}, 400

        weather_map = city_weather(xapi_key, data['city_name'])
        if weather_map['cod'] != 200 or weather_map['name'] != data['city_name']:
            return {
                'message':
                "This city '{}' does not exist in Api.".format(
                    data['city_name'])}, 400

        city = CityModel(data['city_name'])

        try:
            city.save_to_db()
        except:
            return {
                "message": "An error occurred inserting the city."}, 500

        return city.json(), 201

    @swag_from("../docs/cities/cities_delete.yml")
    @require_appkey
    def delete(self):
        data = City.parser.parse_args()
        city = CityModel.find_by_city_name(data['city_name'])
        if city:
            city.delete_from_db()

        return {'message': 'City deleted'}


class CityList(Resource):
    @require_appkey
    def get(self):
        return {
            'cities':
            list(map(lambda x: x.json(), CityModel.query.all()))}


class Forecast(Resource):
    @require_appkey
    def get(self, name):
        xapi_key = request.headers.get('X-Api-Key')
        weather_forecast = city_weather_forecast(xapi_key, name)
        return {
            'cities':
            list(map(lambda x: x.json(), CityModel.query.all()))}

