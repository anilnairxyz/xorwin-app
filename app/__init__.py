from flask import Flask
from config import Config

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

from app import routes
