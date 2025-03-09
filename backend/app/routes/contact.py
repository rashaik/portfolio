from flask import Blueprint, request, jsonify
from app.models.models import Message, db

bp = Blueprint('contact', __name__, url_prefix='/api')

@bp.route('/contact', methods=['POST'])
def send_message():
    data = request.json
    message = Message(
        name=data['name'],
        email=data['email'],
        subject=data['subject'],
        message=data['message']
    )
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201