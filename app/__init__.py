from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from turbo_flask import Turbo


db = SQLAlchemy(session_options={"autoflush": False})
migrate = Migrate()
turbo = Turbo()

from flask_sqlalchemy.model import DefaultMeta  # noqa: E402

BaseModel: DefaultMeta = db.Model


def create_app(config_name="default"):
    application = Flask(__name__, instance_relative_config=True)

    from jinja2 import select_autoescape

    application.jinja_options = {
        "autoescape": select_autoescape(
            enabled_extensions=("html", "html.j2", "xml"),
        )
    }

    # CONFIG
    from config import configs

    application.config.from_object(configs[config_name])

    print(f"DB INFO: using {application.config['INFO_USED_DB']}")

    # APPS
    db.init_app(application)
    migrate.init_app(application, db)
    turbo.init_app(application)

    # CONTROLLERS
    from .controllers import register_all_controllers  # noqa: F401

    register_all_controllers(application)

    # from .controllers import register_error_handlers  # noqa: F401

    # register_error_handlers(application)

    return application
