import json
from flask import request, Response
from api import api_app
from api.models import Category

@api_app.route('/categories', methods=['PUT', ])
def categories():
    if not request.is_json:
        return 'Request body is not a JSON'
    return Response(json.dumps([]), mimetype='application/json', status=201)


@api_app.route('/categories/<id>', methods=['GET', ])
def category_by_id(id):
    return Response(json.dumps([]), mimetype='application/json')
