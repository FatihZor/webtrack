from flask import Flask
from flask_restful import Resource, Api

from config import HOST, PORT, DEBUG

from routes import routes_config

app = Flask(__name__)
api = Api(app)

routes_config(api)

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)