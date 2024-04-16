from flask import jsonify, request

from configApp import app, db
from models.Client import Client


@app.route('/v1/client', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    dto_clients = list(map(lambda obj: obj.to_json(), clients))

    return jsonify({"clients": dto_clients})


@app.route('/v1/client', methods=['POST'])
def registration_client():
    name = request.json.get("name")
    email = request.json.get("email")
    phone = request.json.get("phone")

    if not name or not email or not phone:
        return (
            jsonify({"Error": "one of the required fields is missing"}),
            400
        )

    client = Client(name=name, email=email, phone=phone)
    try:
        db.session.add(client)
        db.session.commit()
    except Exception as ex:
        return (
            jsonify({"Error": str(ex)}),
            400
        )

    return (
        jsonify({"Message": "registration complete successful"}),
        201
    )


@app.route('/v1/client/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def processing_client(id):
    client = Client.query.get(id)

    if not client:
        return (
            jsonify({"Error": "client not found"}),
            404
        )

    if request.method == 'GET':
        return jsonify({"client": client.to_json()})

    if request.method == 'DELETE':
        db.session.delete(client)
        db.session.commit()

        return (
            jsonify({"Message": "delete complete successful"}),
            404
        )

    if request.method == 'PATCH':
        data = request.json
        client.name = data.get("name", client.name)
        client.email = data.get("email", client.email)
        client.name = data.get("phone", client.phone)
        db.session.commit()

        return jsonify({"Message": "update complete successful"})


if __name__ == "__main__":
    app.run(debug=True)
