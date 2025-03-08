from flask import Blueprint, jsonify, request, current_app
from app.models.models import Skill
from app import db
from datetime import datetime

# Change the URL prefix to match the frontend expectation
bp = Blueprint('skills', __name__)

@bp.route('/api/skills', methods=['GET'])
def get_skills():
    try:
        skills = Skill.query.all()
        print(f"Found {len(skills)} skills")
        skills_list = [{
            'id': s.id,
            'name': s.name,
            'category': s.category,
            'proficiency': s.proficiency
        } for s in skills]
        print("Skills list:", skills_list)  # Debug print
        return jsonify(skills_list)
    except Exception as e:
        print(f"Error in get_skills: {str(e)}")  # Debug print
        return jsonify({'error': str(e)}), 500

@bp.route('/api/skills/<int:id>', methods=['GET'])
def get_project(id):
    skill = Skill.query.get_or_404(id)
    return jsonify({
        'id': skill.id,
        'name': skill.name,
        'category': skill.category,
        'proficiency': skill.proficiency
    })

@bp.route('/api/skills', methods=['POST'])
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
