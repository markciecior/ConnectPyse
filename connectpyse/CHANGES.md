0.0
---
-  Initial version

0.1
---
-  Hard labor. Mostly up and working with several modules completed.

0.2
---
- Pickup it up again after several months
- Brought the RestAPI library internal as it's a dead project on GitHub now and I've had to make several patches.

0.3
---
- Several updates and additional API modules by Mark

0.4
---
- Fixed lots of imports
- Uploaded to PyPI

0.5.0.2
---
- Updated Agreements API to use CWController class

0.5.0.5
---
- Added Documents API to upload documents to Tickets, Opportunities, and Companies.

0.5.0.6
---
- Modified Documents API to retrieve documents from Tickets, Opportunities, and Companies.

0.5.0.7
---
- Modified the OpportunityForecast API to correct the fields.
- NOTE: The GET /sales/opportunities/{}/forecast endpoint doesn't return a list, it returns a dict.  The RestApi.get() method doesn't deal with this properly.  ConnectWise needs to fix their endpoint.

0.5.0.8
---
- Added projects_api.py 

0.5.0.9
---
- Added support for Time Sheets (from @wesgann)

0.6.0.2
---
- Added fix for deleting objects (from @billyzoelers)

0.6.0.3
---
- Added support for Company Teams

0.6.0.4
---
- Added support for Configuration Types

0.7
---
- [0xliam](https://github.com/0xliam) added an optional ```ensure_ascii``` keyword argument