from . import ApiRessource

class TokenHandler(ApiRessource):
    def get(self):

        return {'hello': 'world'}