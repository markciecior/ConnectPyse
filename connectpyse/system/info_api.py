from ..cw_controller import CWController
# Class for /system/info
from connectpyse.system import info

class InfoAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'system'
        self.module = 'info'
        self._class = info.Info
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_info(self):
        return super()._get()