import flask
from flask_cors import CORS, cross_origin
from flask import make_response, jsonify
from json import *
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth



es = Elasticsearch(
    hosts = [{'host': 'search-repository-u77zd33iw7o5rozrc6j3q5r2my.us-east-1.es.amazonaws.com', 'port': 443}],
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

app = flask.Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'




@app.route('/api/auth/', methods=["POST"])
def auth():
    query_body = flask.request.get_json()
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                        "user_id": query_body['user_id']
                        }
                    },
                    {
                        "match": {
                        "password": query_body['password']
                        }
                    }
                ]
            }
        }   
    }

    res = es.search(index="auth", body=body)
    if res['hits']['total']['value'] == 1:
        return {
            "status_code": 200,
            "content": True
        }
    return {
        "status_code": 500,
        "content": False
    }

@app.route('/api/insert/', methods=["PUT"])
def insert():
    # print("JSON BODY", flask.request.json)
    
    res = es.index(index="circulars", doc_type='_doc', body=flask.request.json)
    return {
        "status_code": 200,
        "content": res['_id']
    }

@app.route('/api/view/<id>', methods=["GET"])
def view(id):
    res = es.get(index="circulars", id=id)
    print(res)

    return {
        "status_code": 200,
        "content": res
    }

@app.route('/api/search/', methods=["POST"])
def search():
    print('DATA', flask.request.json)
    json = flask.request.get_json()
    field = json['field']
    value = json['value']
    body = {
        "sort": [
            {
                "time": {"order": "desc"}
            }
        ], 
        "query": {
            "match": {
                field: value
            }
        }
    }
    res = es.search(index="circulars", body=body)
    print("res=", res)

    return {
        "status_code": 200,
        "content": res['hits']['hits']
    }

@app.route('/api/delete/', methods=["DELETE"])
def delete():
    query_body = flask.request.get_json()
    # temp = body['key']
    print('KEY', query_body)
    # print(type(query_body))
    body = {
        "query": {
            "match_phrase": {
                "key": query_body
            }
        }
    }
    delete_data = es.delete_by_query(index='circulars', body=body)
    return {
        "status_code": 200,
        "content": "deleted "
    }

@app.route('/api/fetch/', methods=["GET"])
def fetch():
    # query_body = flask.request.get_json()
    # print(query_body)
    body = {
        "sort": [
            {
                "time": {
                    "order": "desc"
                }
            }
        ], 
        "size": 9, 
        "query": {
            "match_all": {}
        }
    }
    res = es.search(index="circulars", body= body)

    return {
        "status_code": 200,
        "content": res['hits']['hits']
    }


if __name__ == "__main__":
    app.run()