from . import ApiRessource

class SubscriptionHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}