from ..cw_controller import CWController
# Class for /system/document/:id/download
from . import document_download


class DocumentDownloadAPI(CWController):
    def __init__(self, parent, **kwargs):
        self.module_url = 'system'
        self.module = 'documents/{}/download'.format(parent)
        self._class = document_download.DocumentDownload
        super().__init__(**kwargs)  # instance gets passed to parent object

    def download_document(self):
        return super()._get_bytes()

    def save_to_file(self, path=""):
        document = self.download_document()
        if path == "":
            raise ValueError("A valid path is required to save the document.")
        with open(path, 'wb') as f:
            f.write(document.bytes.getvalue())
        return True