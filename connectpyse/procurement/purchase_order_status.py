from ..cw_model import CWModel


class PurchaseOrderStatus(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self._info = None  # (Metadata)
        self.defaultFlag = None  # (Boolean)
        self.closedFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self.defaultClosedFlag = None  # (Boolean)
        self.sortOrder = None  # (Integer)
        self.emailTemplate = None  # (PurchaseOrderStatusEmailTemplateReference)

        # initialize object with json dict
        super().__init__(json_dict)
