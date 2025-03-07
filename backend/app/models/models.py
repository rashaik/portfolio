from app import db
from datetime import datetime
import bcrypt

class User(db.Model):
    __table_args__ = {'schema': 'portfolio'}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

class Project(db.Model):
    __table_args__ = {'schema': 'portfolio'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
    technologies = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Skill(db.Model):
    __table_args__ = {'schema': 'portfolio'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "Frontend", "Backend", "DevOps"
    proficiency = db.Column(db.Integer)  # 1-100 scale

class Message(db.Model):
    __table_args__ = {'schema': 'portfolio'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
