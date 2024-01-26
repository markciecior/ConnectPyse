from ..cw_model import CWModel


class Company(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.identifier = None  # *(String(25))
        self.name = None  # *(String(50))
        self.status = None  # *(CompanyStatusReference)
        self.type = None  # *(CompanyTypeReference)
        self.addressLine1 = None  # *(String(50))
        self.addressLine2 = None  # *(String(50))
        self.city = None  # *(String(50))
        self.state = None  # *(String(50))
        self.zip = None  # *(String(12))
        self.country = None  # (CountryReference)
        self.phoneNumber = None  # (String(30))
        self.faxNumber = None  # (String(30))
        self.website = None  # (String(255))
        self.territoryId = None  # (Integer)
        self.marketId = None  # (Integer)
        self.accountNumber = None  # (String(100))
        self.defaultContact = None  # (ContactReference)
        self.dateAcquired = None  # (String)
        self.sicCode = None  # (SicCodeReference)
        self.parentCompany = None  # (CompanyReference)
        self.annualRevenue = None  # (Number)
        self.numberOfEmployees = None  # (Integer)
        self.ownershipType = None  # (OwnershipTypeReference)
        self.timeZone = None  # (TimeZoneReference)
        self.leadSource = None  # (String(50))
        self.leadFlag = None  # (Boolean)
        self.unsubscribeFlag = None  # (Boolean)
        self.calendarId = None  # (Integer)
        self.userDefinedField1 = None  # (String(50))
        self.userDefinedField2 = None  # (String(50))
        self.userDefinedField3 = None  # (String(50))
        self.userDefinedField4 = None  # (String(50))
        self.userDefinedField5 = None  # (String(50))
        self.userDefinedField6 = None  # (String(50))
        self.userDefinedField7 = None  # (String(50))
        self.userDefinedField8 = None  # (String(50))
        self.userDefinedField9 = None  # (String(50))
        self.userDefinedField10 = None  # (String(50))
        self.vendorIdentifier = None  # (String(100))
        self.taxIdentifier = None  # (String)
        self.taxCode = None  # (TaxCodeReference)
        self.billingTerms = None  # (BillingTermsReference)
        self.invoiceTemplate = None  # (InvoiceTemplateReference)
        self.pricingSchedule = None  # (PricingScheduleReference)
        self.companyEntityType = None  # (EntityTypeReference)
        self.billToCompany = None  # (CompanyReference)
        self.billingSite = None  # (SiteReference)
        self.billingContact = None  # (ContactReference)
        self.invoiceDeliveryMethod = None  # (BillingDeliveryReference)
        self.invoiceToEmailAddress = None  # (String)
        self.invoiceCCEmailAddress = None  # (String)
        self.deletedFlag = None  # (Boolean)
        self.dateDeleted = None  # (String)
        self.deletedBy = None  # (String)
        self.mobileGuid = None  # (Guid)
        self.currency = None  # (CurrencyReference)
        self.territoryManager = None  # (MemberReference)
        self._info = None  # (Metadata)
        self.customFields = None  # (Array)

        # initialize object with json dict
        super().__init__(json_dict)

