from . import ApiRessource

class PayoutHandler(ApiRessource):
    def get(self, payout_id=None):

        return {'hello': 'world'}