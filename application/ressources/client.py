from . import ApiRessource

class ClientHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}