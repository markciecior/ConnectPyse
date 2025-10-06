from ..cw_model import CWModel


class DocumentDownload(CWModel):

    def __init__(self, bytes=None):
        self.bytes = None  # (BytesIO)

        # initialize object with bytes
        super().__init__(bytes)
