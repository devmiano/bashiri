from flask import Flask
from flask_assets import Environment, Bundle
from config import config_options


def create_app(config_name):
  app = Flask(__name__, static_folder='assets')
  app.config.from_object(config_options[config_name])
  assets = Environment(app)
  assets.url = app.static_url_path
  sass = Bundle('sass/global.scss', 'sass/main.scss', 'sass/hero.scss', 'sass/navbar.scss', filters='pyscss', depends='sass/base/*.scss', output='styles/global.css')
  assets.register('sass_all', sass)
  sass.build()
  
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  from .requests import configure_request
  configure_request(app)
  
  
  
  return app
