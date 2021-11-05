from flask import request, redirect, url_for
from flask_classful import route

from app.helpers.helper_flask_view import HelperFlaskView

# from flask_classful import FlaskView

from app.models.players import Player


class IndexView(HelperFlaskView):
    route_base = "/"

    def before_request(self, name, *args, **kwargs):
        self.is_index = True
        super().before_request(self)

    def index(self):
        return self.template(template_name="index/index.html.j2")

    @route("choose_name", methods=["POST"])
    def choose_name(self):
        if "name" in request.form:
            self.player = Player(name=request.form["name"])
            self.player.save()
            return redirect(url_for("PlayerView:index"))
