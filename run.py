"""
This module runs the Flask application.
"""
from app import app  # Import the 'app' variable from the app module

if __name__ == '__main__':
    # Run the Flask application in debug mode and make it accessible externally
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
