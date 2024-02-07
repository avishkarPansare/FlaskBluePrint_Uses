
from flask_cors import CORS
from Context.view import context_blueprint
from Home.view import home_blueprint
from flask import Flask

app = Flask(__name__)


CORS(app)
app.register_blueprint(context_blueprint)
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5005)