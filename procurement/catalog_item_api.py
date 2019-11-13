from ..cw_controller import CWController
# Class for /procurement/catalog
from . import catalog_item


class CatalogItemAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'procurement'
        self.module = 'catalog'
        self._class = catalog_item.CatalogItem
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_catalog_items(self):
        return super()._get()

    def create_catalog_item(self, a_catalog_item):
        return super()._create(a_catalog_item)

    def get_catalog_items_count(self):
        return super()._get_count()

    def get_catalog_item_by_id(self, catalog_item_id):
        return super()._get_by_id(catalog_item_id)

    def delete_catalog_item_by_id(self, catalog_item_id):
        super()._delete_by_id(catalog_item_id)

    def replace_catalog_item(self, catalog_item_id):
        pass

    def update_catalog_item(self, catalog_item_id, key, value):
        return super()._update(catalog_item_id, key, value)