from flask import request, redirect, url_for
from flask_classful import route

from app.helpers.helper_flask_view import HelperFlaskView

from app.models import Location, Planet, Town, NatureNode, Building


class LocationView(HelperFlaskView):
    route_base = "/location"

    def index(self):
        return redirect(
            url_for("LocationView:show", id=self.player.current_location_id)
        )
        # return self.template()

    def show(self, id):
        self.location = Location.load(id)
        print(self.location.__class__)
        print(self.location.__class__.__name__)
        print(self.location._view_name)
        print(self.location.url)

        return redirect(self.location.url)


class PlanetView(HelperFlaskView):
    template_folder = "locations/planets"

    def show(self, id):
        self.planet = Planet.load(id)

        return self.template()


class TownView(HelperFlaskView):
    template_folder = "locations/towns"

    def show(self, id):
        self.town = Town.load(id)

        return self.template()


class BuildingView(HelperFlaskView):
    template_folder = "locations/buildings"

    def show(self, id):
        self.building = Building.load(id)

        return self.template()
