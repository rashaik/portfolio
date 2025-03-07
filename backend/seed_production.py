from app import create_app, db
from app.models.models import Project, Skill, User
from datetime import datetime

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Clear existing data
        Project.query.delete()
        Skill.query.delete()
        
        # Seed Projects
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

        # Add projects
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)

        # Seed Skills
        skills = [
            # Frontend Skills
            {'name': 'React', 'category': 'Frontend', 'proficiency': 90},
            {'name': 'Vue.js', 'category': 'Frontend', 'proficiency': 85},
            {'name': 'HTML5/CSS3', 'category': 'Frontend', 'proficiency': 95},
            {'name': 'JavaScript', 'category': 'Frontend', 'proficiency': 90},
            
            # Backend Skills
            {'name': 'Python', 'category': 'Backend', 'proficiency': 95},
            {'name': 'Flask', 'category': 'Backend', 'proficiency': 90},
            {'name': 'PostgreSQL', 'category': 'Backend', 'proficiency': 85},
            {'name': 'RESTful APIs', 'category': 'Backend', 'proficiency': 90},
            
            # DevOps Skills
            {'name': 'Git', 'category': 'DevOps', 'proficiency': 85},
            {'name': 'Docker', 'category': 'DevOps', 'proficiency': 80},
            {'name': 'CI/CD', 'category': 'DevOps', 'proficiency': 75},
            {'name': 'AWS', 'category': 'DevOps', 'proficiency': 70}
        ]

        # Add skills
        for skill_data in skills:
            skill = Skill(**skill_data)
            db.session.add(skill)

        try:
            db.session.commit()
            print("✅ Database seeded successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding database: {str(e)}")
            raise

if __name__ == '__main__':
    seed_database()
