from . import ApiRessource

class SubscriptionHandler(ApiRessource):
    def get(self, subscription_id=None):

        return {'hello': 'world'}