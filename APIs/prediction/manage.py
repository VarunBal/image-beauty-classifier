from tdg import app
from flask_script import Manager,Server

manager = Manager(app)

manager.add_command('runserver',Server(app.config['HOST'],
									  app.config['PORT'],
									  app.config['DEBUG']))

if __name__ == '__main__':
    manager.run()
