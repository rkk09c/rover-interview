from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return 'hello world', 200
