from flask import render_template
from ..requests import get_news, get_headlines, get_source, get_sources

from . import main

@main.route('/')
def index():
  '''function that renders the homepage and the headlines'''
  title = 'News on the Fly'
  headlines = get_headlines()
  sources_list = get_sources()
  
  return render_template('index.html', title=title, headlines=headlines, sources=sources_list)


@main.route('/news/wired')
def wired():
  '''function that renders the wired news source'''
  name = 'wired'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news, sources=sources)

@main.route('/news/the-verge')
def verge():
  '''function that renders the verge news source'''
  name = 'the-verge'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news, sources=sources)

@main.route('/news/the-next-web')
def next():
  '''function that renders the next web page news source'''
  name = 'the-next-web'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/techradar')
def techradar():
  '''function that renders the techradar news source'''
  name = 'techradar'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/techcrunch')
def techcrunch():
  '''function that renders the techcrunch news source'''
  name = 'techcrunch'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/recode')
def recode():
  '''function that renders the recode news source'''
  name = 'recode'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/hacker-news')
def hacker_news():
  '''function that renders the hacker news source'''
  name = 'hacker-news'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/engadget')
def engadget():
  '''function that renders the engadget news source'''
  name = 'engadget'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/crypto-coins-news')
def crypto_coins_news():
  '''function that renders the crypto coins news source'''
  name = 'crypto-coins-news'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/ars-technica')
def ars_technica():
  '''function that renders the ars technica news source'''
  name = 'ars-technica'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

