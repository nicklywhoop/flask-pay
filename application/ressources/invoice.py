from . import ApiRessource

class InvoiceHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}

class InvoiceEventHandler(ApiRessource):
    def get(self, invoice_id):

        return {'hello': 'world'}

class InvoiceRefundHandler(ApiRessource):
    def get(self, invoice_id, request_id=None):

        return {'hello': 'world'}

class InvoiceNotificationHandler(ApiRessource):
    def get(self, invoice_id):

        return {'hello': 'world'}