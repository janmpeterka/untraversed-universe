import random
from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin
from app.presenters.base import BasePresenter
from flask import g


class Location(BaseModel, BaseMixin, BasePresenter):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)

    __mapper_args__ = {"polymorphic_on": category}


class Planet(Location):
    coordinate_x = db.Column(db.Integer)
    coordinate_y = db.Column(db.Integer)
    coordinate_z = db.Column(db.Integer)

    discovered_by = db.Column(db.Integer, db.ForeignKey("players.id"))
    discoverer = db.relationship("Player", foreign_keys=[discovered_by])

    __mapper_args__ = {"polymorphic_identity": "planet"}

    nodes = db.relationship(
        "PlanetNode",
        back_populates="planet",
        primaryjoin="Planet.id == PlanetNode.planet_id",
    )

    @staticmethod
    def generate():
        planet = Planet(discoverer=g.current_player)
        planet.name = f"Planet {random.randint(1, 1000)}"
        planet.save()

        for i in range(1, random.randint(1, 5)):
            planet_node = PlanetNode()
            planet_node.name = f"Planet Node {i}"
            planet_node.save()
            planet_node.planet = planet
            planet_node.save()

        for j in range(1, random.randint(1, 3)):
            town = Town()
            town.name = f"Town {j}"
            town.planet = planet
            town.save()

            for k in range(1, random.randint(2, 5)):
                building = Building()
                building.name = f"Building {k}"
                building.town = town
                building.save()

        return planet


class PlanetNode(Location):
    __mapper_args__ = {"polymorphic_identity": "planet_node"}

    planet_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    planet = db.relationship(
        "Planet",
        back_populates="nodes",
        uselist=False,
        foreign_keys=[planet_id],
        remote_side="Planet.id",
    )


class NatureNode(PlanetNode):
    __mapper_args__ = {"polymorphic_identity": "nature_node"}


class Town(PlanetNode):
    __mapper_args__ = {"polymorphic_identity": "town"}

    buildings = db.relationship(
        "Building", back_populates="town", primaryjoin="Town.id == Building.town_id"
    )


class Building(Location):
    __mapper_args__ = {"polymorphic_identity": "building"}

    town_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    town = db.relationship(
        "Town",
        back_populates="buildings",
        remote_side="Town.id",
        foreign_keys=[town_id],
    )
