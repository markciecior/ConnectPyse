from ..cw_controller import CWController
# Class for /procurement/purchaseorderstatuses
from . import purchase_order_status


class PurchaseOrderStatusAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'procurement'
        self.module = 'purchaseorderstatuses'
        self._class = purchase_order_status.PurchaseOrderStatus
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_purchase_order_statuses(self):
        return super()._get()

    def create_purchase_order_status(self, a_purchase_order_status):
        return super()._create(a_purchase_order_status)

    def get_purchase_order_statuses_count(self):
        return super()._get_count()

    def get_purchase_order_status_by_id(self, purchase_order_status_id):
        return super()._get_by_id(purchase_order_status_id)

    def delete_purchase_order_status_by_id(self, purchase_order_status_id):
        super()._delete_by_id(purchase_order_status_id)

    def replace_purchase_order_status(self, purchase_order_status_id):
        pass

    def update_purchase_order_status(self, purchase_order_status_id, key, value):
        return super()._update(purchase_order_status_id, key, value)

    def update_purchase_order_multiple_keys(self, purchase_order_status_id, changes_dict):
        return super()._update_multiple_keys(purchase_order_status_id, changes_dict)