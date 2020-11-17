from ..cw_controller import CWController
# Class for /finance/agreementadditions
from . import agreement_addition


class AgreementAdditionsAPI(CWController):

    def __init__(self, parent, **kwargs):
        self.module_url = 'finance'
        self.module = 'agreements/{}/additions'.format(parent)
        self._class = agreement_addition.AgreementAddition
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_agreement_additions(self):
        return super()._get()

    def create_agreement_addition(self, a_agreement_addition):
        return super()._create(a_agreement_addition)

    def get_agreement_additions_count(self):
        return super()._get_count()

    def get_agreement_addition_by_id(self, agreement_addition_id):
        return super()._get_by_id(agreement_addition_id)

    def delete_agreement_addition_by_id(self, agreement_addition_id):
        super()._delete_by_id(agreement_addition_id)

    def replace_agreement_addition(self, agreement_addition_id):
        pass

    def update_agreement_addition(self, agreement_addition_id, key, value):
        return super()._update(agreement_addition_id, key, value)
