from flask import Flask
from app.utils.config import Config
from flask_cors import CORS

# Globally accessible libraries
config = Config()

def create_app():
    """
    Create App Factory

    1. Create Flask
    2. Add CORS
    3. Setup Config
    4. Init Database
    5. Register APIs

    :return: app
    """
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(config)

    app.url_map.strict_slashes = False

    return app



