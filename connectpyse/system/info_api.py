from ..cw_controller import CWController
# Class for /system/info
from connectpyse.system import info

class InfoAPI(CWController):
    def __init__(self, **kwargs):
        """
            *Fields attribute is not supported*
        """
        self.module_url = 'system'
        self.module = 'info'
        self._class = info.Info
        super().__init__(**kwargs)  # instance gets passed to parent object
        

    def get_info(self):
        an_instance = self._class(getattr(self, self.module).get(user_headers=self.basic_auth, 
                                                                 user_params=self._format_user_params()))
        return an_instance
        