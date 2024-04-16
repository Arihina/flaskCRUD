from Dao.Repository.ClientRepository import ClientRepository


class ClientService:
    repository = ClientRepository()

    def get(self, id):
        pass

    def create(self, data):
        correct_data = [data.id, data.name, data.email, data.phone]
        self.repository.create(correct_data)

    def update(self, id, data):
        pass

    def delete(self, id):
        pass
