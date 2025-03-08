from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from decouple import config
from sqlalchemy import text
import re

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure CORS to allow requests from frontend
    CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",
            "https://portfolio-frontend-pbq2.onrender.com"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True
    }
})
    
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
        try:
            # Create schema if it doesn't exist
            db.session.execute(text('CREATE SCHEMA IF NOT EXISTS portfolio'))
            db.session.commit()
            
            # Import models and create tables
            from app.models.models import Project, Message, Skill, User
            db.create_all()
            db.session.commit()
        except Exception as e:
            print(f"Database initialization error: {str(e)}")
            db.session.rollback()
            raise
    
    # Register blueprints
    from app.routes.projects import bp as projects_bp
    app.register_blueprint(projects_bp)

    from app.routes.skills import bp as skills_bp
    app.register_blueprint(skills_bp)
 
    # Add a test route to verify API is working
    @app.route('/api/test', methods=['GET'])
    def test_api():
        return {'message': 'API is working!'}, 200
    
    return app
