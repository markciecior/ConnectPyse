from ..cw_controller import CWController
# Class for /project/projects
from . import project


class ProjectsAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'project'
        self.module = 'projects'
        self._class = project.Project
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_projects(self):
        return super()._get()

    def create_project(self, a_project):
        return super()._create(a_project)

    def get_projects_count(self):
        return super()._get_count()

    def get_project_by_id(self, project_id):
        return super()._get_by_id(project_id)

    def delete_project_by_id(self, project_id):
        super()._delete_by_id(project_id)

    def replace_project(self, project_id):
        pass

    def update_project(self, project_id, key, value):
        return super()._update(project_id, key, value)

    def update_project_multiple_keys(self, project_id, changes_dict):
        return super()._update_multiple_keys(project_id, changes_dict)

    def merge_project(self, a_project, target_project_id):
        # return super()._merge(a_project, target_project_id)
        pass
