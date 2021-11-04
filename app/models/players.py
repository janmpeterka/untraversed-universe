from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class Player(BaseModel, BaseMixin):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    qualities = db.relationship(
        "Quality",
        secondary="players_have_qualities",
        primaryjoin="Player.id == PlayerHasQuality.player_id",
        # viewonly=True,
    )

    ship = None

    def add_quality(self, quality):
        from app.models.players_have_qualities import PlayerHasQuality

        phq = PlayerHasQuality(player_id=self.id, quality_id=quality.id)
        phq.save()
