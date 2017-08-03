import flask
from server import app

name = 'Spatial Convert Service'
version = '0.1.1.1'

@app.route('/about')
def about():    
    return flask.jsonify(**{ 'name': name, 'version': version })