from . import ApiRessource

class BillHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}