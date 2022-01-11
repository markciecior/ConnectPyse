# ConnectPyse
ConnectWise (Manage) REST API client written in Python 3.x
The original project was created by Joshua M. Smith.  This forked version was started by Mark Ciecior.

ConnectWise RESTful API Client
--------------------------------

Following the layout style of the official SDKs from CW team. Classes and their API counter part classes are under
their appropriate sections. Import the API class(es) you want to leverage and the model classes are imported with them.

## Setup (old way)
1. Copy your_api.json to new my_api.json file and update with your API key and clientId details

## Setup (new way)
1. Create two variables which are passed to the constructor of the API classes.
2. URL = 'https://connectwise.mycompany.com/v4_6_release/apis/3.0'
3. AUTH = {'Authorization': 'Basic Wmdlasdkjfeklamwekf=', 'clientId': 'myClientIdKey'}

## Usage
1. Import the sections you'll be using
2. Create an object from API Class
3. Leverage member methods to access features

### Paging

    >>> from connectpyse.sales import opportunity_api
    >>> o = opportunity_api.OpportunityAPI(url=URL, auth=AUTH)
    >>> o.pageSize = 27
    >>> o.get_opportunities()

### Filtering

    >>> from connectpyse.sales import opportunity_api
    >>> o = opportunity_api.OpportunityAPI(url=URL, auth=AUTH)
    >>> o.conditions = 'name="My Opportunity"'
    >>> o.get_opportunities()

### Filtering on sub-attributes (use '/')

    >>> from connectpyse.sales import opportunity_api
    >>> o = opportunity_api.OpportunityAPI(url=URL, auth=AUTH)
    >>> o.conditions = 'company/id=19297'
    >>> result = o.get_opportunities()
    >>> for i in result:
    >>>   print(i.company['id'])

### To upload a document to an opportunity:

    >>> from connectpyse.system import document_api
    >>> from connectpyse.sales import opportunity_api
    >>> o = opportunity_api.OpportunityAPI(url=URL, auth=AUTH)
    >>> d = document_api.DocumentAPI(url=URL, auth=AUTH)

    >>> a_opp = o.get_opportunity_by_id(1234)
    >>> f = os.path.join(os.path.curdir, 'local_info.txt')
    >>> a_document = d.create_document(o, 'Newly Uploaded Document', 'server_info.txt', open(f, 'rb'))
    >>> print(a_document.title)

### To retrieve the documents attached to an opportunity:

    >>> from connectpyse.system import document_api
    >>> from connectpyse.sales import opportunity_api
    >>> o = opportunity_api.OpportunityAPI(url=URL, auth=AUTH)
    >>> d = document_api.DocumentAPI(url=URL, auth=AUTH)

    >>> a_opp = o.get_opportunity_by_id(1234)
    >>> myDocs = d.get_documents(a_pp)
    >>> for doc in myDocs:
    >>>   print(doc.title)
    >>> 

### For example to get a Member's office phone number you would:

    >>> from connectpyse.system import members_api
    >>> m = members_api.MembersAPI() #Assuming the my_api.json file has been updated
    -or-
    >>> from connectpyse.system import members_api
    >>> m = members_api.MembersAPI(url=URL, auth=AUTH) #No my_api.json file necessary

    >>> a_member = m.get_member_by_id(123)
    >>> print(a_member.officePhone)
    
### For example to find the name of all activities related to a particular opportunity you would:

    >>> from connectpyse.sales import activity_api
    >>> myAct = activity_api.ActivityAPI() #Assuming the my_api.json file has been updated
    -or-
    >>> from connectpyse.sales import activity_api
    >>> myAct = activity_api.ActivityAPI(url=URL, auth=AUTH) #No my_api.json file necessary

    >>> myAct.conditions = 'opportunity/id=1250'
    >>> allActivities = myAct.get_activities()
    >>> for oneAct in allActivities:
    >>>   print(oneAct.name)

### For example to find all line items of a parent purchase order:

    >>> from connectpyse.procurement import purchase_order_line_item_api
    >>> lineItems = purchase_order_line_item_api.PurchaseOrderLineItemAPI(url=URL,auth=AUTH,parent=1919)
    >>> myItems = lineItems.get_purchase_order_line_items()
    
### For example to update a ticket note:

    >>> from connectpyse.service import ticket_notes_api, ticket_note 
    >>> ticket_notes = ticket_notes_api.TicketNotesAPI(url=URL, auth=AUTH, ticket_id=TICKET_ID)
    >>> note = ticket_note.TicketNote({"text":"testing ticket note update.. ", "detailDescriptionFlag": True})
    >>> ticket_notes.create_ticket_note(note)

### For example to update multiple fields on a ticket:

    >>> from connectpyse.service import tickets_api 
    >>> api = tickets_api.TicketsAPI(url=URL, auth=AUTH)
    >>> mychanges = {"summary": "update multiple keys", "budgetHours": .50}
    >>> ticket = api.update_ticket_multiple_keys(ticketId, mychanges)