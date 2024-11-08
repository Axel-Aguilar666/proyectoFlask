
class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config): #configuramos que nuestro servidor se active en modo debug o modo desarrollo 
    DEBUG = True