# from flask import request, redirect, url_for
# from flask_classful import route

from app.helpers.helper_flask_view import HelperFlaskView


class PlayerView(HelperFlaskView):
    def index(self):
        return self.template()
