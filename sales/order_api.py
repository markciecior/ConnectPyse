from ..cw_controller import CWController
# Class for /sales/orders
from . import order


class OrderAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'sales'
        self.module = 'orders'
        self._class = order.Order
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_orders(self):
        return super()._get()

    def create_order(self, a_order):
        return super()._create(a_order)

    def get_orders_count(self):
        return super()._get_count()

    def get_order_by_id(self, order_id):
        return super()._get_by_id(order_id)

    def delete_order_by_id(self, order_id):
        super()._delete_by_id(order_id)

    def replace_order(self, order_id):
        pass

    def update_order(self, order_id, key, value):
        return super()._update(order_id, key, value)