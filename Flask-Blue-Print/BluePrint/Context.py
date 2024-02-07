from flask import Flask, Blueprint, jsonify, request


context_blueprint = Blueprint('context', __name__, url_prefix='/context')

@context_blueprint.route('/', methods=["GET"])
def home_page():
    if request.method == 'GET':
        return jsonify({"message": "Home Page"}), 200
    
    
@context_blueprint.route('/about', methods=["GET"])
def about_section():
    if request.method == 'GET':
        return jsonify({"message": "About section"}), 200

