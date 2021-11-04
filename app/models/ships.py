from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class Ship(BaseModel, BaseMixin):
    __tablename__ = "ships"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    sensors = db.Column(db.Integer)
    firepower = db.Column(db.Integer)
    durability = db.Column(db.Integer)
    accomodation = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    @staticmethod
    def fill_database():
        from app.data.ships import ships

        for key, value in ships.items():
            quality = Ship(id=int(key), **value)
            quality.save()
