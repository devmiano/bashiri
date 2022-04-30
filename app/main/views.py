from flask import render_template

from . import main

@main.route('/')
def index():
  title = 'Bashiri | News on the Fly'
  
  return render_template('index.html', title=title)
