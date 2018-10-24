from . import ApiRessource

class SettlementHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}