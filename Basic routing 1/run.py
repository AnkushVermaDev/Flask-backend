# Import the Flask class from the flask package.
from flask import Flask

# Import the blueprint 'main' defined in the main.py file.
# A blueprint helps organize a group of related routes and functions.
from mainpage import main
from authpage import auth


def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask app, registers the blueprint,
    and returns the configured app instance.

    Returns:
        Flask: A configured Flask application instance.
    """
    # Create an instance of the Flask application.
    # The __name__ variable helps Flask determine the root path of the application.
    app = Flask(__name__)
    
    # Register the blueprint with the Flask application.
    # The blueprint 'main' contains routes defined in main.py.
    # Registering it here makes those routes available to the application.
    app.register_blueprint(main)
    app.register_blueprint(auth)

    
    # Return the configured Flask application instance.
    return app

# Create the Flask application by calling the create_app() function.
app = create_app()

# This block checks if the script is being run directly (not imported as a module).
if __name__ == '__main__':
    # Run the Flask development server with debugging enabled.
    # Debug mode provides detailed error messages and auto-reloads the server
    # when code changes are detected.
    app.run(debug=True)
