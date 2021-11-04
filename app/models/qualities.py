from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class Quality(BaseModel, BaseMixin):
    __tablename__ = "qualities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
