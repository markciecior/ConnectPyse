from ..cw_model import CWModel


class PurchaseOrder(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self._info = None  # (Metadata)
        self.businessUnitId = None  # (Integer)
        self.cancelReason = None  # (String)
        self.closedFlag = None  # (Boolean)
        self.customerCity = None  # (String)
        self.customerCompany = None  # (CompanyReference)
        self.customerContact = None  # (ContactReference)
        self.customerCountry = None  # (CountryReference)
        self.customerExtension = None  # (String)
        self.customerName = None  # (String)
        self.customerPhone = None  # (String)
        self.customerSite = None  # (SiteReference)
        self.customerSiteName = None  # (String)
        self.customerState = None  # (String)
        self.customerStreetLine1 = None  # (String)
        self.customerStreetLine2 = None  # (String)
        self.customerZip = None  # (String)
        self.dateClosed = None  # (String)
        self.dropShipCustomerFlag = None  # (Boolean)
        self.enteredBy = None  # (String)
        self.freightCost = None  # (Number)
        self.freightPackingSlip = None  # (String)
        self.freightTaxTotal = None  # (Number)
        self.internalNotes = None  # (String)
        self.locationId = None  # *(Integer)
        self.poDate = None  # (String)
        self.poNumber = None  # (String(50))
        self.salesTax = None  # (Number)
        self.shipmentDate = None  # (String)
        self.shipmentMethod = None  # (ShipmentMethodReference)
        self.shippingInstructions = None  # (String)
        self.status = None  # *(PurchaseOrderStatusReference)
        self.subTotal = None  # (Number)
        self.taxCode = None  # (TaxCodeReference)
        self.taxFreightFlag = None  # (Boolean)
        self.taxPoFlag = None  # (Boolean)
        self.terms = None  # *(BillingTermsReference)
        self.total = None  # (Number)
        self.trackingNumber = None  # (String(50))
        self.updateShipmentInfo = None  # (Boolean)
        self.updateVendorOrderNumber = None  # (Boolean)
        self.vendorCompany = None  # *(CompanyReference)
        self.vendorContact = None  # (ContactReference)
        self.vendorInvoiceDate = None  # (String)
        self.vendorInvoiceNumber = None  # (String(50))
        self.vendorOrderNumber = None  # (String(50))
        self.vendorSite = None  # (SiteReference)
        self.warehouse = None  # (WarehouseReference)
        self.currency = None  # (CurrencyReference)

        # initialize object with json dict
        super().__init__(json_dict)
