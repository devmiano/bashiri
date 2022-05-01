import urllib.request,json
from .models import Article, Source

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
    source = article.get('id', 'name')
    title = article.get('title')
    description = article.get('description')
    url = article.get('url')
    urlToImage = article.get('urlToImage')
    publishedAt = article.get('publishedAt')
    
    if urlToImage:
      news_object = Article(source, title, description, url, urlToImage, publishedAt)
      news_results.append(news_object)
      
  return news_results


  
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

