from flask import Flask, Blueprint, jsonify, request,render_template



context_blueprint = Blueprint('context', __name__, url_prefix='/context')

@context_blueprint.route('/', methods=["GET"])
def home_page():
    if request.method == 'GET':
        # return jsonify({"message": "Home Page"}), 200
        return render_template('context/index.html')
        # return render_template('index.html')
    
    
@context_blueprint.route('/about', methods=["GET"])
def about_section():
    if request.method == 'GET':
        return jsonify({"message": "About section"}), 200

