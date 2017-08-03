import flask
from server import app
import layer
import uuid
from osgeo import ogr
   
layers = layer.layers()
layers.add(uuid.UUID('02d427a6-fc61-40f1-8ec8-65e97d6803f3'), 'home', 'point (-36.69405,174.7309471)')
layers.add(uuid.UUID('201755ee-e5d9-4137-b76a-903e1a81ebe9'), 'work', 'point (-36.73767,174.7214429)')

@app.route('/')
def default():
    return app.send_static_file('index.html')

@app.route('/data/<uuid:id>')
def databyid(id):
    print(id)
    layer = layers.getlayerbyid(id)
    if layer != None:
        return flask.jsonify(layer.getresponse())
    else:
        flask.abort(404)
        
@app.route('/data/<string:name>')
def databyname(name):
    layer = layers.getlayerbyname(name)
    if layer != None:
        return flask.jsonify(layer.getresponse())
    else:
        flask.abort(404)

@app.route('/data/test')
def test():
    return '{ "type": "FeatureCollection", "features": [' \
        '{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [174.7309471, -36.69405] }, "properties": { "name": "Home" } }' \
        ', { "type": "Feature", "geometry": { "type": "Point", "coordinates": [174.7214429, -36.73767] }, "properties": { "name": "Work" } }' \
        '] }'

@app.route('/data/bridge')
def bridge():     
    driver = ogr.GetDriverByName('SQLite')
    dataSource = driver.Open('data\\Bridge-WGS84.sqlite', 0)
    layer = dataSource.GetLayer()

    features = map(lambda feature: feature.ExportToJson(), layer)

    return '{ "type": "FeatureCollection", "features": [ ' + ','.join(features) + ' ] }'

    
    