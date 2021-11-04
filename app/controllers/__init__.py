from .index import IndexView
from .ship import ShipView
from .player import PlayerView

from app.helpers.helper_flask_view import HelperFlaskView

__all__ = ["IndexView", "ShipView", "PlayerView"]


def register_all_controllers(application):
    IndexView.register(application, base_class=HelperFlaskView)
    ShipView.register(application, base_class=HelperFlaskView)
    PlayerView.register(application, base_class=HelperFlaskView)


# def register_error_handlers(application):
#     from .errors import error404
#     from .errors import error405
#     from .errors import error500

#     application.register_error_handler(403, error404)
#     application.register_error_handler(404, error404)
#     application.register_error_handler(405, error405)
#     application.register_error_handler(500, error500)
