from flask import Flask
from app.main.routes import main_bp
from app.detection.routes import detection_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Registro de Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(detection_bp)

    return app
