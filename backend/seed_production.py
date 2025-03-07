from app import create_app, db
from app.models.models import Project, Skill, User
from datetime import datetime
from sqlalchemy import text

def seed_database():
    print("Starting database seeding process...")
    app = create_app()
    
    with app.app_context():
        try:
            print("Creating portfolio schema...")
            db.session.execute(text('CREATE SCHEMA IF NOT EXISTS portfolio'))
            db.session.commit()
            print("Schema created successfully!")

            print("Creating all tables...")
            db.create_all()
            print("Tables created successfully!")
            
            print("Clearing existing data...")
            Project.query.delete()
            Skill.query.delete()
            db.session.commit()
            print("Existing data cleared!")
            
            # Seed Projects
            print("Seeding projects...")
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
            db.session.commit()
            print("Projects added successfully!")

            # Seed Skills
            print("Seeding skills...")
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
            db.session.commit()
            print("Skills added successfully!")

            print("✅ Database seeding completed successfully!")
            
            # Verify the data
            print("\nVerifying seeded data:")
            project_count = Project.query.count()
            skill_count = Skill.query.count()
            print(f"Projects in database: {project_count}")
            print(f"Skills in database: {skill_count}")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error during database seeding: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            raise

if __name__ == '__main__':
    seed_database()
