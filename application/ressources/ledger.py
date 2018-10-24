from . import ApiRessource

class LedgerHandler(ApiRessource):
    def get(self, currency=None):

        return {'hello': 'world'}