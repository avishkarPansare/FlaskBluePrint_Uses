from BluePrint import init_app
from flask_cors import CORS
app = init_app()

CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=5005)