from osgeo import ogr

class map_layer:
    id = None
    name = None
    layer = None
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def load_sqlite_file(self, path):
        self.driver = ogr.GetDriverByName('SQLite')
        self.data_source = self.driver.Open(path, 0)
        self.layer = self.data_source.GetLayer()    

    def get_geojson_stream(self):
        if self.layer is not None:
            yield bytes('{ "type": "FeatureCollection", "features": [ ', 'utf-8')
            
            first_feature = True    
            for feature in self.layer:
                geojson = feature.ExportToJson()
                if first_feature:
                    first_feature = False
                    yield bytes(geojson, 'utf-8')    
                else:
                    yield bytes(', ' + geojson, 'utf-8')
            
            yield bytes(' ] }', 'utf-8')
        
class map_layers:
    layers = []

    def add(self, map_layer):
        self.layers.append(map_layer)
    
    def get_layer_by_id(self, id):                
        for layeritem in self.layers:
            if layeritem.id == id:
                return layeritem
        
        return None
        
    def get_layer_by_name(self, name):                
        for layeritem in self.layers:
            if layeritem.name == name:
                return layeritem
        
        return None