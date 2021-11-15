"""
    This api is for LISTOUT app
    Python : 3.6.5
    MySQL : 5.7
"""
__author__ = "Sairaj Bhise"
__date__ = "14-11-2021"

from flask import Flask
from constants.names import FLASK_APP_NAME

app = Flask(FLASK_APP_NAME)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5015, debug=True)



