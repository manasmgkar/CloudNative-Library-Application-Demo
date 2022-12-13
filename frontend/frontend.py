# main.py

from forms import BookSearchForm
from flask import Flask, flash, render_template, request, redirect
from jinja2 import Template
import requests
import json

app = Flask(__name__)
app.secret_key = "super secret key"
app.config.from_pyfile('/config/config.cfg')

@app.route('/', methods=['GET', 'POST'])
def index():
    search = BookSearchForm(request.form)
    if request.method == 'POST':
        if request.form.get("searchbutton") == "Search":
            return search_results(search)
        elif request.form.get("getallbooks") == "Get All Books":
            return allbooks()
    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    print(search_string)
    host = app.config['HOST']
    port = app.config['PORT']
    apiendpoint = host + port + "/library/" + search_string
    try:
        jsondata = requests.get(apiendpoint)
        if jsondata.status_code == 200 and len(jsondata.json()) != 0:
            booksdata = jsondata.json()
            return render_template('result.html', booksdata=booksdata)
        elif jsondata.status_code == 200 and len(jsondata.json()) == 0:
            flash('No results found!')
            return redirect('/')
        else:
            flash("Something went Wrong with Api Connection")
            return redirect('/')       
    except Exception as e :
        flash(e)
        return redirect('/')

@app.route('/allbooks')
def allbooks():
    results = []
    host = app.config['HOST']
    port = app.config['PORT']
    apiendpoint = host + port + "/library/" + "allbooks"
    try:
        jsondata = requests.get(apiendpoint)
        if jsondata.status_code == 200 and len(jsondata.json()) != 0:
            booksdata = jsondata.json()
            return render_template('result.html', booksdata=booksdata)
        elif jsondata.status_code == 200 and len(jsondata.json()) == 0:
            flash('No results found!')
            return redirect('/')
        else:
            flash("Something went Wrong with Api Connection")
            return redirect('/')       
    except Exception as e :
        flash(e)
        return redirect('/')

app.run(host="0.0.0.0", port=5001, debug=False)