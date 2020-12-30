from ..cw_model import CWModel


class OpportunityForecast(CWModel):

    def __init__(self, json_dict=None):
        self.id = None # (Integer)
        self.forecastItems = None  # ([ForecastItem])
        self.productRevenue = None  # (ProductRevenueReference)
        self.serviceRevenue = None  # (ServiceRevenueReference)
        self.agreementRevenue = None  # (AgreementRevenueReference)
        self.timeRevenue = None  # (TimeRevenueReference)
        self.expenseRevenue = None  # (ExpenseRevenueReference)
        self.forecastRevenueTotals = None  # (ForecastRevenueReference)
        self.inclusiveRevenueTotals = None  # (InclusiveRevenueReference)
        self.recurringTotal = None  # (Number)
        self.wonRevenue = None  # (WonRevenueReference)
        self.lostRevenue = None  # (LostRevenueReference)
        self.openRevenue = None  # (OpenRevenueReference)
        self.otherRevenue1 = None  # (Other1RevenueReference)
        self.otherRevenue2 = None  # (Other2RevenueReference)
        self.salesTaxRevenue = None  # (Number)
        self.forecastTotalWithTaxes = None  # (Number)
        self.expectedProbability = None  # (Number)
        self.taxCode = None  # (TaxCodeReference)
        self.billingTerms = None  # (BillingTermsReference)
        self.currency = None  # (CurrencyRefernce)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
