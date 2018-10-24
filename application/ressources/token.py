from . import ApiRessource

class TokenHandler(ApiRessource):
    def get(self, invoice_id=None):

        return {'hello': 'world'}