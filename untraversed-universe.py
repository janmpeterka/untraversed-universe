import os

from app import create_app


env = os.environ.get("APP_STATE", "default")
application = create_app(config_name=env)


@application.context_processor
def utility_processor():
    def link_to(obj):
        try:
            return obj.link_to
        except Exception:
            raise NotImplementedError("This object link_to is probably not implemented")

    return dict(
        link_to=link_to,
    )
