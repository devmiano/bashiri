from flask import Flask
from flask_assets import Environment, Bundle
from config import config_options


def create_app(config_name):
  '''function to create and configure the Flask app'''
  app = Flask(__name__, static_folder='assets')
  app.config.from_object(config_options[config_name])
  assets = Environment(app)
  assets.url = app.static_url_path
  sass = Bundle('sass/global.scss', 'sass/main.scss', 'sass/hero.scss', 'sass/navbar.scss', filters='pyscss', depends='sass/base/*.scss', output='styles/global.css')
  assets.register('sass_all', sass)
  sass.build()
  
  '''import and register the main blueprint'''
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  '''import and configure the requests for use in the app'''
  from .requests import configure_request
  configure_request(app)
  
  
  
  return app
