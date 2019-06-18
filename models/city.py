from db import db


class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(80))

    def __init__(
            self, city_name):
        self.city_name = city_name

    def json(self):
        return {
            'city_name': self.city_name
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_city_name(cls, city_name):
        return cls.query.filter_by(city_name=city_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
