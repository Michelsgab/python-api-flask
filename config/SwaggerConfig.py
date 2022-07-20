import os
from server.appserver import server
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = server.app


SWAGGER_URL = '/swagger'
API_URL = '/config/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/config/swagger.yml')
def send_static():
    return send_from_directory(f'{os.getcwd()}/config', 'swagger.yml')
