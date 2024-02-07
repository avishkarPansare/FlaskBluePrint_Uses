from flask import Flask, Blueprint, jsonify, request,render_template


home_blueprint = Blueprint('home', __name__, url_prefix='/home')

@home_blueprint.route('/', methods=["GET"])
def home_page():
    if request.method == 'GET':
        # return jsonify({"message": "Home Page"}), 200
        return render_template('home/index.html',{"message": "Home  section"}) 
    
    
@home_blueprint.route('/about', methods=["GET"])
def about_section():
    if request.method == 'GET':
        return render_template('home/index.html',{"message": "Home About section"})
