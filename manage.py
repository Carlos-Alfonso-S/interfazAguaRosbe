
from flask_script import Manager, Server
from app.app import inicializarApp, db
from app.config import config


configuracion= config['development']
app=inicializarApp(configuracion)

manager=Manager(app)
app.config['DEBUG']= True
# manager.add_command('runserver', Server(host='localhost', port=5002))


if __name__ == '__main__':
    manager.run()

