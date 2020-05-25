from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from scraper import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/offsec')
def offsec():
    scraper = OffSecSpider()
    scraper.run()
    return render_template('offsec.html', news=scraper.results)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)