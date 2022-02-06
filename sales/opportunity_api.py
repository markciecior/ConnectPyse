from ..cw_controller import CWController
# Class for /sales/opportunity
from . import opportunity


class OpportunityAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'sales'
        self.module = 'opportunities'
        self._class = opportunity.Opportunity
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_opportunities(self):
        return super()._get()

    def create_opportunity(self, a_type):
        return super()._create(a_type)

    def get_opportunities_count(self):
        return super()._get_count()

    def get_opportunity_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_opportunity_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_opportunity(self, type_id):
        pass

    def update_opportunity(self, type_id, key, value):
        return super()._update(type_id, key, value)

    def update_opportunity_multiple_keys(self, type_id, changes_dict):
        return super()._update_multiple_keys(type_id, changes_dict)

    def merge_opportunity(self, a_type, target_type_id):
        # return super()._merge(a_type, target_type_id)
        pass
