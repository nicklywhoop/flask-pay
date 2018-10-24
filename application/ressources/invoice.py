from . import ApiRessource

class InvoiceHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}