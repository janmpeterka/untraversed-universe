from flask import request, redirect, url_for
from flask_classful import route

from app.helpers.helper_flask_view import HelperFlaskView


class PlayerView(HelperFlaskView):
    route_base = "/you"

    def index(self):
        return self.template()

    @route("choose_background", methods=["POST"])
    def choose_background(self):
        from app.models.qualities import Quality

        self.player.add_quality(
            Quality.load_by_category_and_name("Background", request.form["background"])
        )
        self.player.save()

        return redirect(url_for("ShipView:index"))

    def delete_player(self):
        self.player.delete()
        return redirect(url_for("IndexView:index"))
