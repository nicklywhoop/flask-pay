from . import ApiRessource

class RateHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}