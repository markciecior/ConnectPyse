from ..cw_controller import CWController
# Class for /procurement/products
from . import product_item


class ProductItemAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'procurement'
        self.module = 'products'
        self._class = product_item.ProductItem
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_product_items(self):
        return super()._get()

    def create_product_item(self, a_productitem):
        return super()._create(a_productitem)

    def get_product_items_count(self):
        return super()._get_count()

    def get_product_item_by_id(self, product_item_id):
        return super()._get_by_id(product_item_id)

    def delete_product_item_by_id(self, product_item_id):
        super()._delete_by_id(product_item_id)

    def replace_product_item(self, product_item_id):
        pass

    def update_product_item(self, product_item_id, key, value):
        return super()._update(product_item_id, key, value)

    def update_product_item_multiple_keys(self, product_item_id, changes_dict):
        return super()._update_multiple_keys(product_item_id, changes_dict)