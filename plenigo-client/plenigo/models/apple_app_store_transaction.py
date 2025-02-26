from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppleAppStoreTransaction")


@_attrs_define
class AppleAppStoreTransaction:
    """
    Attributes:
        transaction_id (Union[Unset, str]):
        original_transaction_id (Union[Unset, str]):
        web_order_line_item_id (Union[Unset, str]):
        bundle_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        subscription_group_identifier (Union[Unset, str]):
        purchase_date (Union[Unset, int]):
        original_purchase_date (Union[Unset, int]):
        expires_date (Union[Unset, int]):
        quantity (Union[Unset, int]):
        type_ (Union[Unset, str]):
        app_account_token (Union[Unset, str]):
        in_app_ownership_type (Union[Unset, str]):
        signed_date (Union[Unset, int]):
        offer_type (Union[Unset, int]):
        offer_identifier (Union[Unset, str]):
        revocation_date (Union[Unset, int]):
        revocation_reason (Union[Unset, int]):
        is_upgraded (Union[Unset, bool]):
        storefront (Union[Unset, str]):
        storefront_id (Union[Unset, str]):
        transaction_reason (Union[Unset, str]):
        environment (Union[Unset, str]):
        price (Union[Unset, int]):
        currency (Union[Unset, str]):
        offer_discount_type (Union[Unset, str]):
    """

    transaction_id: Union[Unset, str] = UNSET
    original_transaction_id: Union[Unset, str] = UNSET
    web_order_line_item_id: Union[Unset, str] = UNSET
    bundle_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    subscription_group_identifier: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, int] = UNSET
    original_purchase_date: Union[Unset, int] = UNSET
    expires_date: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    app_account_token: Union[Unset, str] = UNSET
    in_app_ownership_type: Union[Unset, str] = UNSET
    signed_date: Union[Unset, int] = UNSET
    offer_type: Union[Unset, int] = UNSET
    offer_identifier: Union[Unset, str] = UNSET
    revocation_date: Union[Unset, int] = UNSET
    revocation_reason: Union[Unset, int] = UNSET
    is_upgraded: Union[Unset, bool] = UNSET
    storefront: Union[Unset, str] = UNSET
    storefront_id: Union[Unset, str] = UNSET
    transaction_reason: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    price: Union[Unset, int] = UNSET
    currency: Union[Unset, str] = UNSET
    offer_discount_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id

        original_transaction_id = self.original_transaction_id

        web_order_line_item_id = self.web_order_line_item_id

        bundle_id = self.bundle_id

        product_id = self.product_id

        subscription_group_identifier = self.subscription_group_identifier

        purchase_date = self.purchase_date

        original_purchase_date = self.original_purchase_date

        expires_date = self.expires_date

        quantity = self.quantity

        type_ = self.type_

        app_account_token = self.app_account_token

        in_app_ownership_type = self.in_app_ownership_type

        signed_date = self.signed_date

        offer_type = self.offer_type

        offer_identifier = self.offer_identifier

        revocation_date = self.revocation_date

        revocation_reason = self.revocation_reason

        is_upgraded = self.is_upgraded

        storefront = self.storefront

        storefront_id = self.storefront_id

        transaction_reason = self.transaction_reason

        environment = self.environment

        price = self.price

        currency = self.currency

        offer_discount_type = self.offer_discount_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionID"] = transaction_id
        if original_transaction_id is not UNSET:
            field_dict["originalTransactionId"] = original_transaction_id
        if web_order_line_item_id is not UNSET:
            field_dict["webOrderLineItemId"] = web_order_line_item_id
        if bundle_id is not UNSET:
            field_dict["bundleID"] = bundle_id
        if product_id is not UNSET:
            field_dict["productID"] = product_id
        if subscription_group_identifier is not UNSET:
            field_dict["subscriptionGroupIdentifier"] = subscription_group_identifier
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if original_purchase_date is not UNSET:
            field_dict["originalPurchaseDate"] = original_purchase_date
        if expires_date is not UNSET:
            field_dict["expiresDate"] = expires_date
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if type_ is not UNSET:
            field_dict["type"] = type_
        if app_account_token is not UNSET:
            field_dict["appAccountToken"] = app_account_token
        if in_app_ownership_type is not UNSET:
            field_dict["inAppOwnershipType"] = in_app_ownership_type
        if signed_date is not UNSET:
            field_dict["signedDate"] = signed_date
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if offer_identifier is not UNSET:
            field_dict["offerIdentifier"] = offer_identifier
        if revocation_date is not UNSET:
            field_dict["revocationDate"] = revocation_date
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason
        if is_upgraded is not UNSET:
            field_dict["isUpgraded"] = is_upgraded
        if storefront is not UNSET:
            field_dict["storefront"] = storefront
        if storefront_id is not UNSET:
            field_dict["storefrontId"] = storefront_id
        if transaction_reason is not UNSET:
            field_dict["transactionReason"] = transaction_reason
        if environment is not UNSET:
            field_dict["environment"] = environment
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if offer_discount_type is not UNSET:
            field_dict["offerDiscountType"] = offer_discount_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transactionID", UNSET)

        original_transaction_id = d.pop("originalTransactionId", UNSET)

        web_order_line_item_id = d.pop("webOrderLineItemId", UNSET)

        bundle_id = d.pop("bundleID", UNSET)

        product_id = d.pop("productID", UNSET)

        subscription_group_identifier = d.pop("subscriptionGroupIdentifier", UNSET)

        purchase_date = d.pop("purchaseDate", UNSET)

        original_purchase_date = d.pop("originalPurchaseDate", UNSET)

        expires_date = d.pop("expiresDate", UNSET)

        quantity = d.pop("quantity", UNSET)

        type_ = d.pop("type", UNSET)

        app_account_token = d.pop("appAccountToken", UNSET)

        in_app_ownership_type = d.pop("inAppOwnershipType", UNSET)

        signed_date = d.pop("signedDate", UNSET)

        offer_type = d.pop("offerType", UNSET)

        offer_identifier = d.pop("offerIdentifier", UNSET)

        revocation_date = d.pop("revocationDate", UNSET)

        revocation_reason = d.pop("revocationReason", UNSET)

        is_upgraded = d.pop("isUpgraded", UNSET)

        storefront = d.pop("storefront", UNSET)

        storefront_id = d.pop("storefrontId", UNSET)

        transaction_reason = d.pop("transactionReason", UNSET)

        environment = d.pop("environment", UNSET)

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        offer_discount_type = d.pop("offerDiscountType", UNSET)

        apple_app_store_transaction = cls(
            transaction_id=transaction_id,
            original_transaction_id=original_transaction_id,
            web_order_line_item_id=web_order_line_item_id,
            bundle_id=bundle_id,
            product_id=product_id,
            subscription_group_identifier=subscription_group_identifier,
            purchase_date=purchase_date,
            original_purchase_date=original_purchase_date,
            expires_date=expires_date,
            quantity=quantity,
            type_=type_,
            app_account_token=app_account_token,
            in_app_ownership_type=in_app_ownership_type,
            signed_date=signed_date,
            offer_type=offer_type,
            offer_identifier=offer_identifier,
            revocation_date=revocation_date,
            revocation_reason=revocation_reason,
            is_upgraded=is_upgraded,
            storefront=storefront,
            storefront_id=storefront_id,
            transaction_reason=transaction_reason,
            environment=environment,
            price=price,
            currency=currency,
            offer_discount_type=offer_discount_type,
        )

        apple_app_store_transaction.additional_properties = d
        return apple_app_store_transaction

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
