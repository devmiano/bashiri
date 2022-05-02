from flask import render_template
from ..requests import get_news, get_headlines, get_source, get_sources

from . import main

@main.route('/')
def index():
  title = 'Bashiri | News on the Fly'
  headlines = get_headlines()
  
  return render_template('index.html', title=title, headlines=headlines)

@main.route('/bbc-news')
def source():
  title = 'Bashiri | News on the Fly'
  bbc_news = get_news('bbc-news')
  
  return render_template('source.html', title=title, bbc=bbc_news)


@main.route('/sources')
def sources():
  title = 'Bashiri | News on the Fly'
  all_sources = get_sources()
  
  return render_template('sources.html', title=title, all=all_sources)


@main.route('/news/<name>')
def news(name):
  
  source = get_source()
  name = f'{source.name}'
  all_sources = get_news('engadget')
  
  return render_template('news.html', source=source, title=name, all=all_sources)
