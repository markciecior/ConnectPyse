from ..cw_controller import CWController
# Class for /sales/opportunities
from . import opportunity_team


class OpportunityTeamAPI(CWController):
    def __init__(self, parent, **kwargs):
        self.module_url = 'sales'
        self.module = 'opportunities/{}/team'.format(parent)
        self._class = opportunity_team.OpportunityTeam
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_opportunity_team(self):
        return super()._get()

    def create_opportunity_team(self, a_opportunity_team):
        return super()._create(a_opportunity_team)

    def get_opportunity_team_count(self):
        return super()._get_count()

    def get_opportunity_team_by_id(self, opportunity_team_id):
        return super()._get_by_id(opportunity_team_id)

    def delete_opportunity_team_by_id(self, opportunity_team_id):
        super()._delete_by_id(opportunity_team_id)

    def replace_opportunity_team(self, opportunity_team_id):
        return super()._replace(opportunity_team_id)

    def update_opportunity_team(self, opportunity_team_id, key, value):
        return super()._update(opportunity_team_id, key, value)

    def update_opportunity_team_multiple_keys(self, opportunity_team_id, changes_dict):
        return super()._update_multiple_keys(opportunity_team_id, changes_dict)