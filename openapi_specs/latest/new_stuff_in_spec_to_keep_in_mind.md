1. The AppleAppStorePurchaseAddition has a new field called transactionIds.
2. AppStoreAcessRight -> additionalData changed from a {key: "...", value: "..."} to {foo: "...", bar: "..."} so this might be a breaking change?
3. We have a new TaxType type, which is returned by OrderItem -> taxType and also SubscriptionItem and also OfferProductBase
4. Customer -> acceptedTerms changed similar to the change I mentioned in the 2.
5. AdditionalCustomerData was renamed to CustomerData, and also got a similar change I mentioned in the 2. -> BREAKING CHANGE?
6. Transaction -> TransactionId changed from int to string BREAKING CHANGE?
7. Transaction got a new field called sortKey
8. ProductTagCreation -> category got new enum variants.
9. ProductTagCreation required fields changed removing title and introducing name
10. OfferTranslationImage -> image new field
11. OfferTranslationImage changed the required fields
12. OfferProductBase -> additionalData got apparently fixed similar to what was mentioned in the 2.
13. Offers got a lot of fields referencing ApiSearchResultBase
14. AdditionalChainData -> data got fixed similar to what was mentioned in the 2.
15. ApiVoucher got new fields referencing VoucherUsageData
16. ApiVoucherPage got new fields referencing ApiSearchResultBase
17. 2 new types: ApiMultiVoucher and ApiChannel
18. ApiCampaginView got renamed to ApiCampaign BREAKING CHANGE?
19. ApiCampaignPage got fixed
--250313--
20. ApiVoucherPage got fixed
21. CreditUploadItemType patched by adding a new variant


