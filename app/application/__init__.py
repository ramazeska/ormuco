from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    if SQLALCHEMY_DATABASE_URI is None:
        raise Exception('SQLALCHEMY_DATABASE_URI os env must be set')
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app



"""TODO
1. create bootstrap frontpage : done
2. redirect to input valiidation - if failed - display error - otherwise return page with "submitted ok": done
2. add sql alchemy
3. add mysql db via 2
4. add config to run flask via gunicorn
5. check via aws - ssl / create self signed certificate
6. check how to add fw + lb with ssl termination on aws 
7. create ansible job to setup all on aws instance
7.1 add  "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDftZwLvh3prVYPxD01zBpehPA6NVlL+iDajlDR2PqzB3odo5gVrV+u6vTyw/TfFR70uOkzoLjxl6x7ZbwXpKBAXqD8ke8gIDOAL4wz8QSKtj1lcLiLOEW0ToKhlwHvlZnA0e/GATtCgt/2y4F+h+jG0VmO3Ae+8aayCOSPVHqKhXcdKt5Qa++/7SuUrTuBN6ApJNp7HmVbMGdSbrr4I1gxNDYONompBTwVvBswBy8ySA+BNaAnKUxsX5gJJCtNENcbtg44TMHufmn69XZeUajDtNGeOgeITAIWnuEiOY+3R70idXJZGSDRnZzs4sXYmP7k4PQq07sWuHqXVKUzYWI/ test"
to aws instance, add my key 
8. test
"""