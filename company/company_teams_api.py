from ..cw_controller import CWController
# Class for /company/companies/{id}/teams
from connectpyse.company import company_team


class CompanyTeamsAPI(CWController):
    def __init__(self, company_id, **kwargs):
        self.module_url = 'company'
        self.module = 'companies/{}/teams'.format(company_id)
        self._class = company_team.CompanyTeam
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_company_teams(self):
        return super()._get()

    def create_company_team(self, a_company_team):
        return super()._create(a_company_team)

    def get_company_teams_count(self):
        return super()._get_count()

    def get_company_team_by_id(self, company_team_id):
        return super()._get_by_id(company_team_id)

    def delete_company_team_by_id(self, company_team_id):
        super()._delete_by_id(company_team_id)

    def replace_company_team(self, company_team_id):
        pass

    def update_company_team(self, company_id, key, value):
        return super()._update(company_id, key, value)

    def update_company_team_multiple_keys(self, company_id, changes_dict):
        return super()._update_multiple_keys(company_id, changes_dict)

    def merge_company_team(self, a_company_team, target_company_team_id):
        # return super()._merge(a_company_team, target_company_team_id)
        pass

