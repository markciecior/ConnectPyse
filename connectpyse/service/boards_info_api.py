from ..cw_controller import CWController
# Class for /service/info/boards
from . import board_info


class BoardsInfoAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'service'
        self.module = 'info/boards'
        self._class = board_info.BoardInfo
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_boards_info(self):
        return super()._get()

    def get_boards_info_count(self):
        return super()._get_count()

    def get_board_info_by_id(self, entry_id):
        return super()._get_by_id(entry_id)
