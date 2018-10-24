from . import ApiRessource

class ClientHandler(ApiRessource):
    def get(self, key_id=None):

        return {'hello': 'world'}