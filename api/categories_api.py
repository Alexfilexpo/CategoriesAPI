import json
from flask import Flask, request, Response

api = Flask(__name__)

@api.route('/categories', methods=['PUT', ])
def categories():
    if not request.is_json:
        return 'Request body is not a JSON'
    return Response(json.dumps([]), mimetype='application/json', status=201)


@api.route('/categories/<id>', methods=['GET', ])
def category_by_id(id):
    return Response(json.dumps([]), mimetype='application/json')


if __name__ == "__main__":
    api.run()