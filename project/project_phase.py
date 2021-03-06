from ..cw_model import CWModel


class ProjectPhase(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.projectId = None  # (Integer)
        self.description = None  # *(String(100))
        self.board = None  # (ProjectBoardReference)
        self.status = None  # (PhaseStatusReference)
        self.agreement = None  # (AgreementReference)
        self.opportunity = None  # (OpportunityReference)
        self.parentPhase = None  # (ProjectPhaseReference)
        self.wbsCode = None  # (String(50))
        self.billTime = None  # (Enum)
        self.billExpenses = None  # (Enum)
        self.billProducts = None  # (Enum)
        self.markAsMilestoneFlag = None  # (Boolean)
        self.notes = None  # (String)
        self.deadlineDate = None  # (String)
        self.billSeparatelyFlag = None  # (Boolean)
        self.billingMethod = None  # *(Enum)
        self.scheduledHours = None  # (Number)
        self.scheduledStart = None  # (String)
        self.scheduledEnd = None  # (String)
        self.actualHours = None  # (Number)
        self.actualStart = None  # (String)
        self.actualEnd = None  # (String)
        self.budgetHours = None  # (Number)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.hourlyRate = None  # (Number)
        self.billingStartDate = None  # (String)
        self.billPhaseClosedFlag = None  # (Boolean)
        self.billProjectClosedFlag = None  # (Boolean)
        self.downpayment = None  # (Number)
        self.poNumber = None  # (String(25))
        self.poAmount = None  # (Number)
        self.estimatedTimeCost = None  # (Number)
        self.estimatedExpenseCost = None  # (Number)
        self.estimatedProductCost = None  # (Number)
        self.estimatedTimeRevenue = None  # (Number)
        self.estimatedExpenseRevenue = None  # (Number)
        self.estimatedProductRevenue = None  # (Number)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
