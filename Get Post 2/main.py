from flask import Flask
from authReq import auth as auth_blueprint

def create_app():
    app = Flask(__name__)

    # Register the authentication blueprint
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Corrected syntax error
