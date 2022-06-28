from flask import Flask
app = Flask(__name__)
# index route


@app.route('/')
def index():
    return 'Hellow, this is PetFax!'


@app.route('/pets')
def pets():
    return 'These are our pets available for adopotion!'
