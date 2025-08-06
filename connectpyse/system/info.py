from ..cw_model import CWModel


class Info(CWModel):

    def __init__(self, json_dict=None):
        self.cloudRegion = None # (String)
        self.isCloud = None  # (Boolean)
        self.licenseBits = None # (list(dict))
        self.maxWorkFlowRecordsAllowed = None # Int
        self.serverTimeZone = None  # (String)
        self.version = None  # (String)
        


        # initialize object with json dict
        super().__init__(json_dict)
