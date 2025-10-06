from ..cw_model import CWModel


class DocumentDownload(CWModel):

    def __init__(self, json_dict=None):
        self.bytes = None  # (BytesIO)

        # initialize object with bytes
        super().__init__(json_dict)
