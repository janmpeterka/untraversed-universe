import os


class Config(object):
    # UPLOAD_FOLDER = "/temporary"
    # ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_STRING")
    SQLALCHEMY_POOL_SIZE = 5

    APP_STATE = os.environ.get("APP_STATE")  # production, development, debug, shutdown

    TURBO_WEBSOCKET_ROUTE = None

    SENTRY_MONITORING = True
    INFO_USED_DB = "production db"


class LocalProdConfig(Config):
    INFO_USED_DB = "production db"
    TEMPLATES_AUTO_RELOAD = True


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("TESTING_DB_STRING")
    SECRET_KEY = os.environ.get("TESTING_SECRET_KEY")
    SENTRY_MONITORING = False

    INFO_USED_DB = "testing db"


class DevConfig(LocalProdConfig):
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_STRING")
    SENTRY_MONITORING = False

    INFO_USED_DB = "local db"
    # SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    INFO_USED_DB = "production db"


configs = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig,
    "local_production": LocalProdConfig,
    "default": ProdConfig,
}
