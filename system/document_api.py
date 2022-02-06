from ..cw_controller import CWController
# Class for /system/documents
from connectpyse.system import document
from connectpyse.service import ticket
from connectpyse.sales import opportunity
from connectpyse.company import company


class DocumentAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'system'
        self.module = 'documents'
        self._class = document.Document
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_documents(self, a_object):
        if isinstance(a_object, ticket.Ticket):
          self.recordType = 'Ticket'
          self.recordId = a_object.id
        elif isinstance(a_object, opportunity.Opportunity):
          self.recordType = 'Opportunity'
          self.recordId = a_object.id
        elif isinstance(a_object, company.Company):
          self.recordType = 'Company'
          self.recordId = a_object.id
        else:
          raise Exception('Document retrieval only supported for Tickets, Opportunities, and Companies')        
        return super()._get()

    def create_document(self, a_object, a_title, a_filename, a_file):
        if isinstance(a_object, ticket.Ticket):
          objectType = 'Ticket'
          objectId = a_object.id
        elif isinstance(a_object, opportunity.Opportunity):
          objectType = 'Opportunity'
          objectId = a_object.id
        elif isinstance(a_object, company.Company):
          objectType = 'Company'
          objectId = a_object.id
        else:
          raise Exception('Document creation only supported for Tickets, Opportunities, and Companies')
        return super()._upload(objectType, objectId, a_title, a_filename, a_file)

    def get_documents_count(self):
        pass

    def get_document_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_document_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_document(self, type_id):
        pass

    def update_document(self, type_id, key, value):
        pass

    def update_document_multiple_keys(self, type_id, changes_dict):
        pass

    def merge_document(self, a_type, target_type_id):
        # return super()._merge(a_type, target_type_id)
        pass
