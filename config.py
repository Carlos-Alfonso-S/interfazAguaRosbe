class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='p3plzcpnl454184.prod.phx3.secureserver.net'
    MYSQL_USER='Prueba01Carlos'
    MYSQL_PASSWORD='ResRosbe2022'
    MYSQL_DB='PruebaAguaRosbe'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}