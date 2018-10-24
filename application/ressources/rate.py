from . import ApiRessource

class RateHandler(ApiRessource):
    def get(self, base_currency=None, currency=None):

        return {'hello': 'world'}