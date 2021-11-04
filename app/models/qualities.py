from app import db, BaseModel
from app.helpers.base_mixin import BaseMixin


class Quality(BaseModel, BaseMixin):
    __tablename__ = "qualities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    @staticmethod
    def load_by_category_and_name(category, name):
        return Quality.query.filter_by(name=name, category=category).first()

    @staticmethod
    def fill_database():
        from app.data.qualities import qualities

        for key, value in qualities.items():
            quality = Quality(
                id=int(key), category=value["category"], name=value["name"]
            )
            quality.save()
