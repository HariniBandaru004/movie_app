import logging
logging.basicConfig(filename='/home/harinibandaru/Desktop/error_logs.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

from elasticsearch import Elasticsearch, helpers
from flask import Flask, request, jsonify
import json

header = {'Content-type': "application/json"}
es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})


@app.errorhandler(405)
def invalid_syntax(e):
    return "This is post method"


@app.route("/insert_all", methods=["POST"])
def create_idx_insert_documents():
    try:
        payload = json.loads(request.data.decode('utf-8'))
        path = payload.get("file_path")
        input_file= open(path, 'r')
        movies_file = json.load(input_file)
        data = movies_file.get('movies', {})
        response = helpers.bulk(es, data, index="movie")
        if response:
            return "Documents inserted successfully"
        else:
            return "Failed to insert documents"
    except Exception as e:
        logger.error(e)
        return "Error! Files cannot be uploaded"


@app.route("/insert", methods=["POST"])
def insert_document():
    try:
        document = request.data
        response = es.index(index="movie", body=document)
        if response:
            return response.get("result", {})
        else:
            return "Failed to fetch response"
    except Exception as e:
        logger.error(e)
        return "Error! Document cannot be inserted"


@app.route("/search_all", methods=["GET"])
def search_index():
    try:
        query = {
            "query": {
                "match_all": {}
            }
        }
        result = es.search(index="movie", doc_type="_doc", body=query, headers=header)
        if result:
            return result
        else:
            return "Can't Fetch any documents"
    except Exception as e:
        logger.error(e)
        return "Error in searching documents"


@app.route("/movie_search/<movie_name>", methods=["GET"])
def movie_search(movie_name):
    try:
        query = {
            "query": {
                "match_phrase": {
                    "title": movie_name
                }
            }
        }
        result = es.search(index="movie", body=query, headers=header)
        if result:
            response = {}
            result_response = result.get("hits", {}).get("hits", [])
            extracted_list = result_response[0]
            response["title"] = extracted_list.get("_source",{}).get("title")
            response["plot"] = extracted_list.get("_source",{}).get("plot")
            return response
        else:
            return "Movie Name Not Found"
    except Exception as e:
        logger.error(e)
        return "Error in searching movie name"


@app.route("/director_search/<director_name>", methods=["GET"])
def director_search(director_name):
    try:
        query = {
            "query": {
                "match_phrase": {
                    "director": director_name
                }
            }
        }
        result = es.search(index="movie", body=query, headers=header)
        if result:
            response = {}
            result_response = result.get("hits",{}).get("hits",[])
            extracted_list = result_response[0]
            response["title"] = extracted_list.get("_source",{}).get("title")
            response["year"] = extracted_list.get("_source",{}).get("year")
            response["plot"] = extracted_list.get("_source",{}).get("plot")
            return response
        else:
            return "Director Name Not Found"
    except Exception as e:
        logger.error(e)
        return "Error in searching director name"


@app.route("/delete_doc/<i>", methods=["GET"])
def delete_id(i):
    try:
        result = es.delete_by_query(index="movie", doc_type='_doc', body={"query": {"match": {"id": i}}})
        response = result.get("deleted")
        if response == 0:
            return "Document Not Found"
        else:
            return "Document Deleted Successfully"
    except Exception as e:
        logger.error(e)
        return "Delete Failed"


@app.route("/stats", methods=["GET"])
def get_stats():
    try:
        query = {
            "size": 0,
            "aggs": {
                "Group1": {
                    "cardinality": {
                        "field": "actors.keyword"
                    }
                },
                "Group2": {
                    "cardinality": {
                        "field": "genres.keyword"
                    }
                },
                "Group3": {
                    "cardinality": {
                        "field": "director.keyword"
                    }
                }
            }
        }

        result = es.search(index="movie", body=query, headers=header)
        if result:
            response = {"actors": result.get("aggregations",{}).get("Group1",{}).get("value"),
                        "genres": result.get("aggregations",{}).get("Group2",{}).get("value"),
                        "directors": result.get("aggregations",{}).get("Group3",{}).get("value")}
            return response
        else:
            return "Failed to get stats"
    except Exception as e:
        logger.error(e)
        return "Error in getting stats"

@app.route("/actor_search/<actor_name>", methods=["GET"])
def actor_search(actor_name):
     try:
        query = {
            "query": {
                "match_phrase": {
                    "actors": actor_name
                }
            }
        }
        result = es.search(index="movie", body=query, headers=header)
        if result:
            extracted_list = result.get("hits",{}).get("hits",[])
            response = {}
            j = 1
            for doc in extracted_list:
                result_response = {"title": doc.get("_source", {}).get("title"),
                                   "plot": doc.get("_source", {}).get("plot"),
                                   "actors": doc.get("_source", {}).get("actors")}
                response[j] = result_response
                j += 1
            return response
        else:
            return "Failed to search actor"
     except Exception as e:
        logger.error(e)
        return "Error in searching actor"

@app.route("/", methods=["GET"])
def home():
    return "Hello"


if __name__ == "__main__":
    app.run(port='5005', debug=True)

