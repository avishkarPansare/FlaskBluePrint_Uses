from flask import Flask, Blueprint, jsonify, request


home_blueprint = Blueprint('home', __name__, url_prefix='/home')

@home_blueprint.route('/', methods=["GET"])
def home_page():
    if request.method == 'GET':
        return jsonify({"message": "Home Page"}), 200
    
    
@home_blueprint.route('/about', methods=["GET"])
def about_section():
    if request.method == 'GET':
        return jsonify({"message": "About section"}), 200

