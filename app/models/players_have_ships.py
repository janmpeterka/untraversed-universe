from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class PlayerHasShip(BaseModel, BaseMixin):
    __tablename__ = "players_have_ships"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    player_id = db.Column(db.ForeignKey("players.id"), nullable=False)
    ship_id = db.Column(db.ForeignKey("ships.id"), nullable=False)

    is_active = db.Column(db.Boolean, default=True)

    @staticmethod
    def load_by_player_and_ship(player, ship):
        return PlayerHasShip.query.filter_by(
            player_id=player.id, ship_id=ship.id
        ).first()
