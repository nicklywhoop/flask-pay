from . import ApiRessource

class Bill(ApiRessource):
    def get(self):
        return {'hello': 'world'}