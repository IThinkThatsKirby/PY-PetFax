from flask import Flask

# factory


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Howdy Howdy Howdy'
    # register pet Blueprint
    from . import pets
    app.register_blueprint(pet.bp)

    return app
