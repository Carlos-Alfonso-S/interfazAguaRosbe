class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='ResidenteRosbe.mysql.pythonanywhere-services.com'
    MYSQL_USER='ResidenteRosbe'
    MYSQL_PASSWORD='ResRosbe2'
    MYSQL_DB='PruebaRosbeAgua'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}