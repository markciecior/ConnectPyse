from ..cw_controller import CWController
# Class for /procurement/purchaseorders
from . import purchase_order_line_item


class PurchaseOrderLineItemAPI(CWController):
    def __init__(self, parent, **kwargs):
        self.module_url = 'procurement'
        self.module = 'purchaseorders/{}/lineitems'.format(parent)
        self._class = purchase_order_line_item.PurchaseOrderLineItem
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_purchase_order_line_items(self):
        return super()._get()

    def create_purchase_order_line_item(self, a_purchase_order_line_item):
        return super()._create(a_purchase_order_line_item)

    def get_purchase_order_line_items_count(self):
        return super()._get_count()

    def get_purchase_order_line_item_by_id(self, purchase_order_line_item_id):
        return super()._get_by_id(purchase_order_line_item_id)

    def delete_purchase_order_line_item_by_id(self, purchase_order_line_item_id):
        super()._delete_by_id(purchase_order_line_item_id)

    def replace_purchase_order_line_item(self, purchase_order_line_item_id):
        return super()._replace(purchase_order_line_item_id)

    def update_purchase_order_line_item(self, purchase_order_line_item_id, key, value):
        return super()._update(purchase_order_line_item_id, key, value)