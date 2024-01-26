from ..cw_controller import CWController
# Class for /sales/opportunities
from . import opportunity_forecast


class OpportunityForecastAPI(CWController):
    def __init__(self, parent, **kwargs):
        self.module_url = 'sales'
        self.module = 'opportunities/{}/forecast'.format(parent)
        self._class = opportunity_forecast.OpportunityForecast
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_opportunity_forecasts(self):
        return super()._get()

    def create_opportunity_forecast(self, a_opportunity_forecast):
        return super()._create(a_opportunity_forecast)

    def get_opportunity_forecasts_count(self):
        return super()._get_count()

    def get_opportunity_forecast_by_id(self, opportunity_forecast_id):
        return super()._get_by_id(opportunity_forecast_id)

    def delete_opportunity_forecast_by_id(self, opportunity_forecast_id):
        super()._delete_by_id(opportunity_forecast_id)

    def replace_opportunity_forecast(self, opportunity_forecast_id):
        return super()._replace(opportunity_forecast_id)

    def update_opportunity_forecast(self, opportunity_forecast_id, key, value):
        return super()._update(opportunity_forecast_id, key, value)

    def update_opportunity_forecast_multiple_keys(self, opportunity_forecast_id, changes_dict):
        return super()._update_multiple_keys(opportunity_forecast_id, changes_dict)