from flask import Blueprint, jsonify, request
from app.models.models import Skill
from app import db

bp = Blueprint('skills', __name__, url_prefix='/api/skills')

@bp.route('/', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'category': s.category,
        'proficiency': s.proficiency
    } for s in skills])

@bp.route('/', methods=['POST'])
def create_skill():
    data = request.get_json()
    skill = Skill(
        name=data['name'],
        category=data['category'],
        proficiency=data.get('proficiency', 0)
    )
    db.session.add(skill)
    db.session.commit()
    return jsonify({'message': 'Skill created successfully'}), 201
