from app import create_app, db
from app.models.models import Project

def seed_projects():
    projects = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-stack e-commerce platform built with React and Django. Features include user authentication, product catalog, shopping cart, and payment integration.',
            'image_url': 'https://images.unsplash.com/photo-1557821552-17105176677c?w=600&auto=format&q=75',
            'github_url': 'https://github.com/username/ecommerce',
            'live_url': 'https://ecommerce-demo.com',
            'technologies': 'React, Django, PostgreSQL, Redis, AWS'
        },
        {
            'title': 'Task Management App',
            'description': 'A Kanban-style task management application with real-time updates. Users can create boards, add tasks, and collaborate with team members.',
            'image_url': 'https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d?w=600&auto=format&q=75',
            'github_url': 'https://github.com/username/task-manager',
            'live_url': 'https://task-manager-demo.com',
            'technologies': 'Vue.js, Node.js, Express, MongoDB, Socket.io'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A weather dashboard that displays current weather conditions and forecasts for multiple cities. Integrates with OpenWeatherMap API.',
            'image_url': 'https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?w=600&auto=format&q=75',
            'github_url': 'https://github.com/username/weather-dashboard',
            'live_url': 'https://weather-dash-demo.com',
            'technologies': 'HTML5, CSS3, JavaScript, OpenWeatherMap API'
        }
    ]

    # Clear existing projects
    Project.query.delete()
    
    # Add new projects
    for project_data in projects:
        project = Project(**project_data)
        db.session.add(project)
    
    db.session.commit()
    print("Projects have been added to the database!")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_projects()
