from warnings import filters
from flask import Flask
from flask_assets import Environment, Bundle
from config import config_options


def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config_options[config_name])
  
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  from .requests import configure_request
  configure_request(app)
  
  assets = Environment(app)
  sass = Bundle('sass/global.scss', filters='pyscss, cssmin', output='css/global.min.css')
  assets.register('sass_all', sass)
  sass.build()
  
  return app
