from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from decouple import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app)
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL', 
        default='postgresql:///portfolio')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config('SECRET_KEY', default='your-secret-key')
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes.projects import bp as projects_bp
    from app.routes.skills import bp as skills_bp
    from app.routes.auth import bp as auth_bp
    
    app.register_blueprint(projects_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(auth_bp)
    
    return app
