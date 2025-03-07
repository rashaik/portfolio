from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from decouple import config
import re

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app)
    
    # Database configuration
    database_url = config('DATABASE_URL', default='postgresql:///portfolio')
    
    # Fix Render Postgres URL format if needed
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config('SECRET_KEY', default='your-secret-key')
    
    # Initialize extensions
    db.init_app(app)
    
    # Create schema if it doesn't exist
    with app.app_context():
        # Create schema if it doesn't exist
        db.session.execute('CREATE SCHEMA IF NOT EXISTS portfolio')
        db.session.commit()
        
        # Import models and create tables
        from app.models.models import Project, Message, Skill, User
        db.create_all()
        db.session.commit()
    
    # Register blueprints
    from app.routes.projects import bp as projects_bp
    from app.routes.skills import bp as skills_bp
    from app.routes.auth import bp as auth_bp
    
    app.register_blueprint(projects_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(auth_bp)
    
    return app
