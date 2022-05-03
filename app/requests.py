import urllib.request,json
from .models import Article, Source
from datetime import datetime

apiKey = None
baseUrl = None
newsUrl = None
techUrl = None


def configure_request(app):
  global apiKey, baseUrl, newsUrl, techUrl
  apiKey = app.config['NEWS_API_KEY']
  baseUrl = app.config['BASE_API_URL']
  newsUrl = app.config['NEWS_API_URL']
  techUrl = app.config['TECH_API_URL']
  

def process_results(news_list):
  news_results = []
  for article in news_list:
    title = article.get('title')
    description = article.get('description')
    url = article.get('url')
    urlToImage = article.get('urlToImage')
    publishedAt = article.get('publishedAt')
    
    if urlToImage:
      news_object = Article(title, description, url, urlToImage, publishedAt)
      news_results.append(news_object)
      
  return news_results


def process_sources(sources_list):
  sources_results = []
  for source in sources_list:
    id = source.get('id')
    name = source.get('name')
    description = source.get('description')
    url = source.get('url')
    category = source.get('category')

    
    if category:
      sources_object = Source(id, name, description, url, category)
      sources_results.append(sources_object)
      
  return sources_results



def get_sources():
  get_sources_url = techUrl.format(apiKey)
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    
    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_sources(sources_results_list)
      
  return sources_results


def get_source():
  get_source_url = techUrl.format(apiKey)
  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    source_response = json.loads(get_source_data)
    
    source_obj = None
    
    if source_response:
      id = source_response.get('id')
      name = source_response.get('name')
      description = source_response.get('description')
      url = source_response.get('url')
      category = source_response.get('category')
      
      source_obj = Source(id, name, description, url, category)
      
  return source_obj


def get_headlines():
  get_headlines_url = baseUrl.format(apiKey)
  
  with urllib.request.urlopen(get_headlines_url) as url:
    get_headlines_data = url.read()
    get_headlines_response = json.loads(get_headlines_data)
    
    headlines_results = None
    
    if get_headlines_response['articles']:
      headlines_results_list = get_headlines_response['articles']
      headlines_results = process_results(headlines_results_list)
      
  return headlines_results


def get_news(sources):
  get_news_url = newsUrl.format(sources, apiKey)
  
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)
    
    news_results = None
    
    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
      news_results = process_results(news_results_list)
      
  return news_results