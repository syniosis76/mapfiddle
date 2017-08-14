from server import api
import json
from layer import *
import uuid

import falcon
   
layers = map_layers()

class test:
    def on_get(self, req, resp):
        data = {
                "type": "FeatureCollection"
                , "features":
                    [
                        { "type": "Feature", "geometry": { "type": "Point", "coordinates": [174.7309471, -36.69405] }, "properties": { "name": "Home" } }
                        , { "type": "Feature", "geometry": { "type": "Point", "coordinates": [174.7214429, -36.73767] }, "properties": { "name": "Work" } }
                    ]
            }

        resp.body = json.dumps(data)

api.add_route('/data/test', test())

class bridge:
    def on_get(self, req, resp):
        layer = layers.get_layer_by_name('bridge')
        if layer is None:
            layer = map_layer(uuid.uuid4(), 'bridge')
            layer.load_sqlite_file('data\\Bridge-WGS84.sqlite')
            layers.add(layer)
                    
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"        
        resp.stream = layer.get_geojson_stream()

api.add_route('/data/bridge', bridge()) 
    

    
    