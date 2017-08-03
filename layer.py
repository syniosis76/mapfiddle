class layer:
    id = None
    name = None
    wkt = None
    
    def __init__(self, id, name, wkt):
        self.id = id
        self.name = name
        self.wkt = wkt

    def getresponse(self):
        return { 'id': self.id, 'name': self.name, 'wkt': self.wkt }
        
class layers:
    layers = []

    def add(self, id, name, wkt):
        self.layers.append(layer(id, name, wkt))
    
    def getlayerbyid(self, id):                
        for layeritem in self.layers:
            if layeritem.id == id:
                return layeritem
        
        return None
        
    def getlayerbyname(self, name):                
        for layeritem in self.layers:
            if layeritem.name == name:
                return layeritem
        
        return None