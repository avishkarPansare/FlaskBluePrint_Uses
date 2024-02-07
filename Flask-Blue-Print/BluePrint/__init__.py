from flask import Flask

def init_app():
    app = Flask(__name__)

    with app.app_context():
            
        from .Context import context_blueprint
        from .Home import home_blueprint

        app.register_blueprint(home_blueprint)
        
        app.register_blueprint(context_blueprint)

        return app