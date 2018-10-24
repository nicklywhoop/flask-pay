from . import ApiRessource

class PayoutHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}