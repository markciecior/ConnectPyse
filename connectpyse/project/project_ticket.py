from ..cw_model import CWModel


class ProjectTicket(CWModel):
    
    def __init__(self, json_dict=None):
        
        # Core fields
        self.id = None  # (int)
        self.summary = None  # (String) Max length: 100, required
        self.isIssueFlag = None  # (boolean)
        
        # Reference objects
        self.board = None  # (BoardReference)
        self.status = None  # (ServiceStatusReference)
        self.workRole = None  # (WorkRoleReference)
        self.workType = None  # (WorkTypeReference)
        self.project = None  # (ProjectReference)
        self.phase = None  # (ProjectPhaseReference) required
        
        # WBS and Location
        self.wbsCode = None  # (String) Max length: 50
        self.company = None  # (CompanyReference)
        self.site = None  # (SiteReference)
        self.siteName = None  # (String) Max length: 156
        
        # Address fields
        self.addressLine1 = None  # (String) Max length: 50
        self.addressLine2 = None  # (String) Max length: 50
        self.city = None  # (String) Max length: 50
        self.stateIdentifier = None  # (String) Max length: 50
        self.zip = None  # (String) Max length: 12
        self.country = None  # (CountryReference)
        
        # Contact information
        self.contact = None  # (ContactReference)
        self.contactName = None  # (String) Max length: 62
        self.contactPhoneNumber = None  # (String) Max length: 20
        self.contactPhoneExtension = None  # (String) Max length: 15
        self.contactEmailAddress = None  # (String) Max length: 250
        
        # Service classification
        self.type = None  # (ServiceTypeReference)
        self.subType = None  # (ServiceSubTypeReference)
        self.item = None  # (ServiceItemReference)
        
        # Assignment and priority
        self.owner = None  # (MemberReference)
        self.priority = None  # (PriorityReference)
        self.serviceLocation = None  # (ServiceLocationReference)
        self.source = None  # (ServiceSourceReference)
        
        # Dates and hours
        self.requiredDate = None  # (String) ISO 8601 datetime
        self.budgetHours = None  # (double)
        
        # Related records
        self.opportunity = None  # (OpportunityReference)
        self.agreement = None  # (AgreementReference)
        self.agreementType = None  # (String)
        
        # Knowledge base
        self.knowledgeBaseCategoryId = None  # (int)
        self.knowledgeBaseSubCategoryId = None  # (int)
        self.knowledgeBaseLinkId = None  # (int)
        self.knowledgeBaseLinkType = None  # (String) Enum: ["ServiceFaq", "ServiceTicket", "ServiceBoard", "Article", "Unknown", "SalesFaq"]
        
        # Portal and notification flags
        self.allowAllClientsPortalView = None  # (boolean)
        self.customerUpdatedFlag = None  # (boolean)
        self.automaticEmailContactFlag = None  # (boolean)
        self.automaticEmailResourceFlag = None  # (boolean)
        self.automaticEmailCcFlag = None  # (boolean)
        self.automaticEmailCc = None  # (String) Max length: 1000
        
        # Closure information
        self.closedDate = None  # (String)
        self.closedBy = None  # (String)
        self.closedFlag = None  # (boolean)
        
        # Time tracking
        self.actualHours = None  # (double)
        self.approved = None  # (boolean)
        
        # Billing
        self.subBillingMethod = None  # (String) Enum: ["ActualRates", "FixedFee", "NotToExceed", "OverrideRate"]
        self.subBillingAmount = None  # (double)
        self.subDateAccepted = None  # (String)
        self.resources = None  # (String)
        
        # Billing flags
        self.billTime = None  # (String) Enum: ["Billable", "DoNotBill", "NoCharge", "NoDefault"]
        self.billExpenses = None  # (String) Enum: ["Billable", "DoNotBill", "NoCharge", "NoDefault"]
        self.billProducts = None  # (String) Enum: ["Billable", "DoNotBill", "NoCharge", "NoDefault"]
        
        # Predecessor/dependency information
        self.predecessorType = None  # (String) Enum: ["Ticket", "Phase"]
        self.predecessorId = None  # (int)
        self.predecessorClosedFlag = None  # (boolean)
        self.lagDays = None  # (int)
        self.lagNonworkingDaysFlag = None  # (boolean)
        
        # Scheduling
        self.estimatedStartDate = None  # (String) ISO 8601 datetime
        self.location = None  # (SystemLocationReference)
        self.department = None  # (SystemDepartmentReference)
        self.duration = None  # (int)
        self.scheduleStartDate = None  # (String) ISO 8601 datetime
        self.scheduleEndDate = None  # (String) ISO 8601 datetime
        
        # Additional fields
        self.mobileGuid = None  # (String) UUID format
        self.currency = None  # (CurrencyReference)
        self._info = None  # (dict)
        
        # Related objects
        self.tasks = None  # (List) List of TicketTask
        
        # POST-only fields (not returned in response)
        self.initialDescription = None  # (String)
        self.initialInternalAnalysis = None  # (String)
        self.initialResolution = None  # (String)
        
        # Processing flags
        self.contactEmailLookup = None  # (String)
        self.processNotifications = None  # (boolean) Can be set to false to skip notification processing (defaults to True)
        self.skipCallback = None  # (boolean)
        
        # Custom fields
        self.customFields = None  # (List) List of CustomFieldValue

        # initialize object with json dict
        super().__init__(json_dict)
