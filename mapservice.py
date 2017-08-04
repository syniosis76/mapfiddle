from server import api
import json
import layer
import uuid
from osgeo import ogr
   
layers = layer.layers()
layers.add(uuid.UUID('02d427a6-fc61-40f1-8ec8-65e97d6803f3'), 'home', 'point (-36.69405,174.7309471)')
layers.add(uuid.UUID('201755ee-e5d9-4137-b76a-903e1a81ebe9'), 'work', 'point (-36.73767,174.7214429)')

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
        driver = ogr.GetDriverByName('SQLite')
        dataSource = driver.Open('data\\Bridge-WGS84.sqlite', 0)
        layer = dataSource.GetLayer()

        features = map(lambda feature: feature.ExportToJson(), layer)

        resp.body = '{ "type": "FeatureCollection", "features": [ ' + ','.join(features) + ' ] }'

api.add_route('/data/bridge', bridge()) 
    

    
    