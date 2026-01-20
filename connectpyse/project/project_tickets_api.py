from ..cw_controller import CWController
# Class for /project/tickets
from . import project_ticket


class ProjectTicketsAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'project'
        self.module = 'tickets'
        self._class = project_ticket.ProjectTicket
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_tickets(self):
        return super()._get()

    def create_ticket(self, a_ticket):
        return super()._create(a_ticket)

    def get_tickets_count(self):
        return super()._get_count()

    def get_ticket_by_id(self, ticket_id):
        return super()._get_by_id(ticket_id)

    def delete_ticket_by_id(self, ticket_id):
        super()._delete_by_id(ticket_id)

    def replace_ticket(self, ticket_id):
        pass

    def update_ticket(self, ticket_id, key, value):
        return super()._update(ticket_id, key, value)

    def update_ticket_multiple_keys(self, ticket_id, changes_dict):
        return super()._update_multiple_keys(ticket_id, changes_dict)

    def merge_ticket(self, a_ticket, target_ticket_id):
        # return super()._merge(a_ticket, target_ticket_id)
        pass
