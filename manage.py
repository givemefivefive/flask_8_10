from urllib.request import localhost

from flask import render_template
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from apps import create_app

app = create_app()

manager = Manager(app)
manager.add_command('start', Server(port=8877, host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

@app.route('/')
def hello_world():
    # return app.send_static_file('static/index.html')
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
