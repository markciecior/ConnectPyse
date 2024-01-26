from ..cw_controller import CWController
# Class for /company/agreements
from . import agreement


class AgreementsAPI(CWController):

    def __init__(self, **kwargs):
        self.module_url = 'finance'
        self.module = 'agreements'
        self._class = agreement.Agreement
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_agreements(self):
        return super()._get()

    def create_agreement(self, a_agreement):
        return super()._create(a_agreement)

    def get_agreements_count(self):
        return super()._get_count()

    def get_agreement_by_id(self, agreement_id):
        return super()._get_by_id(agreement_id)

    def delete_agreement_by_id(self, agreement_id   ):
        super()._delete_by_id(agreement_id)

    def replace_agreement(self, agreement_id):
        pass

    def update_agreement(self, agreement_id, key, value):
        return super()._update(agreement_id, key, value)

    def update_agreement_multiple_keys(self, agreement_id, changes_dict):
        return super()._update_multiple_keys(agreement_id, changes_dict)

    def merge_agreement(self, agreement_id):
        pass

#    def create_configuration_association(self, user_headers, agreement_id, config_id):
#        # /agreements/{id}/configurations
#         self.root_path = self.root_path + '/agreements/{}'.format(agreement_id)
# 
#         dict_post = {'id': config_id}
#         json_results = self.configurations.post(user_data=dict_post, user_headers=user_headers)
#         #      status_code = json_results.status_code
#         return json_results

    def get_agreement_configurations(self):
        pass
