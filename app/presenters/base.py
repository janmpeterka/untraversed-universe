from flask import url_for
from markupsafe import escape, Markup

# from app.helpers.general import classproperty


class BasePresenter:
    @property
    def url(self) -> str:
        print("hehe")
        return url_for(f"{self._view_name}:show", id=self.id)

    # @property
    # def external_url(self) -> str:
    #     return url_for(f"{self._view_name}:show", id=self.id, _external=True)

    @property
    def _view_name(self):
        return f"{self.__class__.__name__}View"

    # @classproperty
    # def _class_view_name(cls):
    #     return f"{cls.__name__}View"

    @property
    def default_link_value(self):
        return escape(self.name)

    def path_to(self, action, **kwargs):
        if action == "show":
            return self.path_to_show(**kwargs)
        elif action == "edit":
            return self.path_to_edit(**kwargs)

        else:
            return url_for(f"{self._view_name}:{action}", id=self.id, **kwargs)

    def path_to_show(self, **kwargs):
        return url_for(f"{self._view_name}:show", id=self.id, **kwargs)
