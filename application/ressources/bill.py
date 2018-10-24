from . import ApiRessource

class BillHandler(ApiRessource):
    def get(self, bill_id=None):

        return {'hello': 'world'}

class BillDeliveryHandler(ApiRessource):
    def get(self, bill_id=None):

        return {'hello': 'world'}