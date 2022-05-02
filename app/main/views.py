from flask import render_template
from ..requests import get_news, get_headlines, get_source, get_sources

from . import main

@main.route('/')
def index():
  title = 'News on the Fly'
  headlines = get_headlines()
  sources_list = get_sources()
  
  return render_template('index.html', title=title, headlines=headlines, sources=sources_list)


@main.route('/news/wired')
def wired():
  name = 'wired'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news, sources=sources)

@main.route('/news/the-verge')
def verge():
  name = 'the-verge'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news, sources=sources)

@main.route('/news/the-next-web')
def next():
  name = 'the-next-web'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/techradar')
def techradar():
  name = 'techradar'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/techcrunch')
def techcrunch():
  name = 'techcrunch'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/recode')
def recode():
  name = 'recode'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/hacker-news')
def hacker_news():
  name = 'hacker-news'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/engadget')
def engadget():
  name = 'engadget'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/crypto-coins-news')
def crypto_coins_news():
  name = 'crypto-coins-news'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

@main.route('/news/ars-technica')
def ars_technica():
  name = 'ars-technica'
  news = get_news(name)
  sources = get_sources()
  
  return render_template('source.html', name=name, news=news,  sources=sources)

