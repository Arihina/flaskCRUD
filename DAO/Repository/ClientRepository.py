from werkzeug.sansio.multipart import Data

from App import db


class ClientRepository:
    def get(self, id):
        pass

    def create(self, new_data):
        data = new_data
        db.session.add(*data)
        db.session.commit()

    def update(self, id, data):
        pass

    def delete(self, id):
        pass
