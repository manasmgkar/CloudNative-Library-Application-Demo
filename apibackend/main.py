from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
import time

app = Flask(__name__)
app.config.from_pyfile('/config/config.cfg')

def connect_elasticsearch():
    eshosts = app.config['ESHOST']
    esport = app.config['ESPORT']
    esurl = eshosts + esport
    esconnect = Elasticsearch(hosts=esurl)
    if esconnect.ping(request_timeout=20000):
        print("Connected to Elasticsearch Database")
    else:
        print("Could not Connect to Elasticsearch Database")
    return esconnect

es = connect_elasticsearch()

@app.route('/', methods=['GET'])
def index():
    return "welcome to the Fast indexed library"


@app.route('/library/allbooks', methods=['GET'])
def allbooks():
    result = es.search(index='library', body={"query":{"match_all":{}}})
    return jsonify(result['hits']['hits'])


@app.route('/library/<string:search>', methods=['GET'])
def searchword(search):
    body = {
        "query": {
            "multi_match": {
                "query": search,
            }
        }
    }

    res = es.search(index="library", body=body)
    return jsonify(res['hits']['hits'])


@app.route('/library/<string:author>', methods=['GET'])
def searchauthor(author):
    body = {
        "query": {
            "multi_match": {
                "query": author,
                "fields": ["author"]
            }
        }
    }

    res = es.search(index="library", body=body)

    return jsonify(res['hits']['hits'])

"""
@app.route('/library/<string:name>', methods=['GET'])
def searchname(name):
    keyword = request.form['keyword']

    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["content", "title"]
            }
        }
    }

    res = es.search(index="books", doc_type="title", body=body)

    return jsonify(res['hits']['hits'])
"""

app.run(host="0.0.0.0", port=5000, debug=False)
