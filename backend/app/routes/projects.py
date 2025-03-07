from flask import Blueprint, jsonify, request, current_app
from app.models.models import Project
from app import db

bp = Blueprint('projects', __name__, url_prefix='/api/projects')

@bp.route('/', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        print(f"Found {len(projects)} projects")  # Debug print
        project_list = [{
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'image_url': p.image_url,
            'github_url': p.github_url,
            'live_url': p.live_url,
            'technologies': p.technologies,
            'created_at': p.created_at.isoformat()
        } for p in projects]
        print("Project list:", project_list)  # Debug print
        return jsonify(project_list)
    except Exception as e:
        print(f"Error in get_projects: {str(e)}")  # Debug print
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get_or_404(id)
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'image_url': project.image_url,
        'github_url': project.github_url,
        'live_url': project.live_url,
        'technologies': project.technologies,
        'created_at': project.created_at.isoformat()
    })

@bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(
        title=data['title'],
        description=data['description'],
        image_url=data.get('image_url'),
        github_url=data.get('github_url'),
        live_url=data.get('live_url'),
        technologies=data.get('technologies')
    )
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully'}), 201
