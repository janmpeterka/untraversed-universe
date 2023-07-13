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
        viewonly=True,
    )

    player_qualities = db.relationship(
        "PlayerHasQuality",
        cascade="all,delete",
    )

    ships = db.relationship(
        "Ship",
        secondary="players_have_ships",
        primaryjoin="Player.id == PlayerHasShip.player_id",
        viewonly=True,
    )

    player_ships = db.relationship("PlayerHasShip", cascade="all,delete")

    current_location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    current_location = db.relationship("Location")

    def move_to(self, location):
        self.current_location = location
        self.edit()

    def add_quality(self, quality):
        from app.models.players_have_qualities import PlayerHasQuality

        phq = PlayerHasQuality(player_id=self.id, quality_id=quality.id)
        phq.save()

    def add_ship(self, ship):
        from app.models.players_have_ships import PlayerHasShip

        if ship in self.ships:
            return "Cannot add same ship multiple times"

        for ship in self.ships:
            self.deactivate_ship(ship)

        phs = PlayerHasShip(player_id=self.id, ship_id=ship.id)
        phs.save()

    def activate_ship(self, ship):
        from app.models.players_have_ships import PlayerHasShip

        phs = PlayerHasShip.load_by_player_and_ship(self, ship)
        phs.is_active = True
        phs.save()

    def deactivate_ship(self, ship):
        from app.models.players_have_ships import PlayerHasShip

        phs = PlayerHasShip.load_by_player_and_ship(self, ship)
        phs.is_active = False
        phs.save()

    @property
    def ship(self):
        active_ships = [ps.ship for ps in self.player_ships if ps.is_active]

        if not active_ships:
            return None

        return active_ships[0]
