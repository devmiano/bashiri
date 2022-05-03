import os

class Config:
  '''class to configure url parameters'''
  BASE_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={}'
  NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  TECH_API_URL = 'https://newsapi.org/v2/top-headlines/sources?category=technology&language=en&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
  
  
class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True
  ASSETS_DEBUG = True
  
config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
  