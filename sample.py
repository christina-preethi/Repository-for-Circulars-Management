from elasticsearch import Elasticsearch

es = Elasticsearch(['https://search-repository-u77zd33iw7o5rozrc6j3q5r2my.us-east-1.es.amazonaws.com'])

def insert_into(key, to, from_whom, title, body):
    doc = {
        "key": key,
        "to": to,
        "from": from_whom,
        "title": title,
        "body": body
    }

    res = es.index(index="circulars", doc_type='_doc', body=doc)
    return res['result']

def show_result(search_for):
    res = es.search(index="circulars", body={"query": {"match": {"body": search_for}}})
    for hit in res['hits']['hits']:
        print(hit["_source"])

if __name__ == "__main__":
    print("1. Insert")
    print("0. Search")
    operation = int(input())
    if(operation):
        key = input("key: ")
        to = input("to: ")
        from_whom = input("from: ")
        title = input("title: ")
        body = input("body: ")

        result = insert_into(key, to, from_whom, title, body)
        print(result)
    else:
        search_for = input("Enter search word: ")
        show_result(search_for)

