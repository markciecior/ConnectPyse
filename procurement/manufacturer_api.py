from ..cw_controller import CWController
# Class for /procurement/manufacturers
from . import manufacturer


class ManufacturerAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'procurement'
        self.module = 'manufacturers'
        self._class = manufacturer.Manufacturer
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_manufacturers(self):
        return super()._get()

    def create_manufacturer(self, a_manufacturer):
        return super()._create(a_manufacturer)

    def get_manufacturers_count(self):
        return super()._get_count()

    def get_manufacturer_by_id(self, manufacturer_id):
        return super()._get_by_id(manufacturer_id)

    def delete_manufacturer_by_id(self, manufacturer_id):
        super()._delete_by_id(manufacturer_id)

    def replace_manufacturer(self, manufacturer_id):
        pass

    def update_manufacturer(self, manufacturer_id, key, value):
        return super()._update(manufacturer_id, key, value)