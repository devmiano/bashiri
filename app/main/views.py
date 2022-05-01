from flask import render_template
from ..requests import get_news

from . import main

@main.route('/')
def index():
  title = 'Bashiri | News on the Fly'
  bbc_news = get_news('bbc-news')
  
  return render_template('index.html', title=title, bbc=bbc_news)
