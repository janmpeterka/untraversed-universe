from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class Player(BaseModel, BaseMixin):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    ship = None
