from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

import config
from Service.ClientService import ClientService

app = Flask(__name__)
app.secret_key = config.key
app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_data
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/v1/client', methods=['POST', 'GET'])
def save_get(client_id):
    service = ClientService()

    if request.method == "POST":
        content = request.json
        service.create(content)

    if request.method == "GET":
        info = service.get(client_id)
        return Response(info)

    return Response('OK')


if __name__ == "__main__":
    app.run(debug=True)
