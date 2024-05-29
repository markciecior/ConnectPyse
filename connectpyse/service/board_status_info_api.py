from ..cw_controller import CWController
# Class for /service/boards{}/statuses/info
from . import board_status_info


class BoardsStatusInfoAPI(CWController):
    def __init__(self, board_id, **kwargs):
        self.module_url = 'service'
        self.module = 'boards/{}/statuses/info'.format(board_id)
        self._class = board_status_info.BoardStatusInfo
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_board_statuses(self):
        return super()._get()

    def get_count_board_statuses(self):
        return super()._get_count()
