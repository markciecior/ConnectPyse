from ..cw_controller import CWController
# Class for /company/companies/types
from connectpyse.company import configuration_type


class ConfigurationTypeAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'company'
        self.module = 'configurations/types'
        self._class = configuration_type.ConfigurationType
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_configuration_types(self):
        return super()._get()

    def create_configuration_type(self, a_configuration_type):
        return super()._create(a_configuration_type)

    def get_configuration_types_count(self):
        return super()._get_count()

    def get_configuration_type_by_id(self, configuration_type_id):
        return super()._get_by_id(configuration_type_id)

    def delete_configuration_type_by_id(self, configuration_type_id):
        super()._delete_by_id(configuration_type_id)

    def replace_configuration_type(self, configuration_type_id):
        pass

    def update_configuration_type(self, configuration_type_id, key, value):
        return super()._update(configuration_type_id, key, value)

    def update_configuration_type_multiple_keys(self, configuration_type_id, changes_dict):
        return super()._update_multiple_keys(configuration_type_id, changes_dict)

    def merge_configuration_type(self, a_configuration_type, target_configuration_type_id):
        # return super()._merge(a_configuration_type, target_configuration_type_id)
        pass
