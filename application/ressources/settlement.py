from . import ApiRessource

class SettlementHandler(ApiRessource):
    def get(self, settlement_id=None):

        return {'hello': 'world'}

class SettlementReconciliationHandler(ApiRessource):
    def get(self, settlement_id):

        return {'hello': 'world'}