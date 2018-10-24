from . import ApiRessource

class LedgerHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}