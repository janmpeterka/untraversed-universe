from flask import request, redirect, url_for
from flask_classful import route

from app.helpers.helper_flask_view import HelperFlaskView

from app.models.ships import Ship


class ShipView(HelperFlaskView):
    route_base = "/deck"

    def index(self):
        return self.template()

    @route("choose_ship", methods=["POST"])
    def choose_ship(self):
        self.player.add_ship(Ship.load(request.form["ship"]))

        from app.models import Planet

        self.player.move_to(Planet.generate())

        return redirect(url_for("ShipView:index"))
