"""
Initialize Flask app

"""
from flask import Flask
import os
import application.settings
from flask_restful import Api

app = Flask('__name__')
api = Api(app)

if os.getenv('FLASK_CONF') == 'TEST':
    app.config.from_object('application.settings.Testing')
else:
    app.config.from_object('application.settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Pull in URL dispatch routes
import application.urls
