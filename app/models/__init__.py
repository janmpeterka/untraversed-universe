from .players import Player
from .qualities import Quality
from .players_have_qualities import PlayerHasQuality
from .ships import Ship
from .locations import Planet, NatureNode, Town, Building, Location
from .players_have_ships import PlayerHasShip

__all__ = [
    "Player",
    "Quality",
    "PlayerHasQuality",
    "Ship",
    "PlayerHasShip",
    "Planet",
    "NatureNode",
    "Town",
    "Building",
    "Location",
]

models_dict = {
    "Player": Player,
    "Quality": Quality,
    "PlayerHasQuality": PlayerHasQuality,
    "Ship": Ship,
    "PlayerHasShip": PlayerHasShip,
    "Planet": Planet,
    "NatureNode": NatureNode,
    "Town": Town,
    "Building": Building,
    "Location": Location,
}
