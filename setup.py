from api import create_app, db
from api.book import models
from api.review import models


if __name__ == '__main__':
    db.create_all(app=create_app())
