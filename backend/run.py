from app import create_app, db

app = create_app()

# Initialize the database
with app.app_context():
    db.create_all()

# Only run the development server when this file is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
