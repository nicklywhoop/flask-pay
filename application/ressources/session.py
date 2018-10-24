from . import ApiRessource

class SessionHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}