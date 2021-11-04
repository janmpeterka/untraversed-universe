from app.helpers.helper_flask_view import HelperFlaskView


class ShipView(HelperFlaskView):
    def index(self):
        return self.template()
