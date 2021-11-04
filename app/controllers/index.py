from flask import request, redirect, url_for

from app.helpers.helper_flask_view import HelperFlaskView

# from flask_classful import FlaskView

from app.models.players import Player
from app.models.qualities import Quality


class IndexView(HelperFlaskView):
    route_base = "/"

    def before_request(self, name, *args, **kwargs):
        self.index = True
        super().before_request(self)

    def index(self):
        return self.template(template_name="index/index.html.j2")

    def post(self):
        if "name" in request.form:
            self.player = Player(name=request.form["name"])
            self.player.save()

        if "background" in request.form:

            if request.form["background"] == "law":
                self.player.add_quality(Quality.load_by_category_and_name("Background", "Running from law"))
                self.player.save()

            return redirect(url_for("IndexView:index"))
