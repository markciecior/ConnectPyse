from ..cw_controller import CWController
# Class for /procurement/purchaseorders
from . import purchase_order


class PurchaseOrderAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'procurement'
        self.module = 'purchaseorders'
        self._class = purchase_order.PurchaseOrder
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_purchase_orders(self):
        return super()._get()

    def create_purchase_order(self, a_purchase_order):
        return super()._create(a_purchase_order)

    def get_purchase_orders_count(self):
        return super()._get_count()

    def get_purchase_order_by_id(self, purchase_order_id):
        return super()._get_by_id(purchase_order_id)

    def delete_purchase_order_by_id(self, purchase_order_id):
        super()._delete_by_id(purchase_order_id)

    def replace_purchase_order(self, purchase_order_id):
        pass

    def update_purchase_order(self, purchase_order_id, key, value):
        return super()._update(purchase_order_id, key, value)

    def update_purchase_order_multiple_keys(self, purchase_order_id, changes_dict):
        return super()._update_multiple_keys(purchase_order_id, changes_dict)