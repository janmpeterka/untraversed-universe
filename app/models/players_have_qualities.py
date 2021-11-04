from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class PlayerHasQuality(BaseModel, BaseMixin):
    __tablename__ = "players_have_qualities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    player_id = db.Column(db.ForeignKey("players.id"), nullable=False)
    quality_id = db.Column(db.ForeignKey("qualities.id"), nullable=False)