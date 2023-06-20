Seems like the data model is not properly validated or the OpenAPI specificiation is not up to date. There are several endpoints and fields that are not matching the OpenAPI specification.

1) Fields that can contain null values but are not specified as nullable:

AccessRights:

 - accessTimeStart
 - accessTimeEnd
 - pauseTimeStart
 - pauseTimeEnd
 - maxCacheDate
 - data

Subscriptions:

 - startDate
 - endDate
 - cancellationDate
 - firstBookingDate
 - lastBookingDate
 - nextBookingDate

Customers
 - birthday

OfferBase
 - fixedStartDate


2) Different JSON schema:

Refunds:

    - missing reason field that is specified as required in the specification

3) Fields that are defined as ENUM with fixed values but the API returns different values:

Empty strings:
  - precursorReason
  - precursorReasonDetail
  - successorReason
  - successorReasonDetail
  - salutation
  - pdfTemplateUsage

Additional new values:
  - successorReason 
  - precursorReason
