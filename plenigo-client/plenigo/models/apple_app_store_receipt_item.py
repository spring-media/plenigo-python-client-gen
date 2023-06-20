import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppleAppStoreReceiptItem")


@attr.s(auto_attribs=True)
class AppleAppStoreReceiptItem:
    """
    Attributes:
        quantity (Union[Unset, str]): number of items purchased
        product_id (Union[Unset, str]): product identifier of the item that was purchased
        transaction_id (Union[Unset, str]): transaction identifier of the item that was purchased
        original_transaction_id (Union[Unset, str]): for a transaction that restores a previous transaction, the
            transaction identifier of the original transaction - otherwise, identical to the transaction identifier
        web_order_line_item_id (Union[Unset, str]): primary key for identifying subscription purchases
        promotional_offer_id (Union[Unset, str]): id of the promotional offer
        subscription_group_identifier (Union[Unset, str]): identifier for the subscription group
        is_trial_period (Union[Unset, str]): value for this key is "true" if the customer’s subscription is currently in
            the free trial period, or "false" if not
        is_in_intro_offer_period (Union[Unset, str]): value for this key is "true" if the customer’s subscription is
            currently in an introductory price period, or "false" if not.
        is_upgraded (Union[Unset, str]): flag indicating if item is an upgrade of another item
        expires_date (Union[Unset, datetime.datetime]): expiration date for the subscription with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        purchase_date (Union[Unset, datetime.datetime]): date and time that the item was purchased with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        original_purchase_date (Union[Unset, datetime.datetime]): for a transaction that restores a previous
            transaction, the date of the original transaction with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        cancellation_date (Union[Unset, datetime.datetime]): for a transaction that was canceled by Apple customer
            support, the time and date of the cancellation - for an auto-renewable subscription plan that was upgraded, the
            time and date of the upgrade transaction with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        cancellation_reason (Union[Unset, str]): for a transaction that was canceled, the reason for cancellation
    """

    quantity: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    original_transaction_id: Union[Unset, str] = UNSET
    web_order_line_item_id: Union[Unset, str] = UNSET
    promotional_offer_id: Union[Unset, str] = UNSET
    subscription_group_identifier: Union[Unset, str] = UNSET
    is_trial_period: Union[Unset, str] = UNSET
    is_in_intro_offer_period: Union[Unset, str] = UNSET
    is_upgraded: Union[Unset, str] = UNSET
    expires_date: Union[Unset, datetime.datetime] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    original_purchase_date: Union[Unset, datetime.datetime] = UNSET
    cancellation_date: Union[Unset, datetime.datetime] = UNSET
    cancellation_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        product_id = self.product_id
        transaction_id = self.transaction_id
        original_transaction_id = self.original_transaction_id
        web_order_line_item_id = self.web_order_line_item_id
        promotional_offer_id = self.promotional_offer_id
        subscription_group_identifier = self.subscription_group_identifier
        is_trial_period = self.is_trial_period
        is_in_intro_offer_period = self.is_in_intro_offer_period
        is_upgraded = self.is_upgraded
        expires_date: Union[Unset, str] = UNSET
        if not isinstance(self.expires_date, Unset):
            expires_date = self.expires_date.isoformat()

        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        original_purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.original_purchase_date, Unset):
            original_purchase_date = self.original_purchase_date.isoformat()

        cancellation_date: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_date, Unset):
            cancellation_date = self.cancellation_date.isoformat()

        cancellation_reason = self.cancellation_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if original_transaction_id is not UNSET:
            field_dict["originalTransactionId"] = original_transaction_id
        if web_order_line_item_id is not UNSET:
            field_dict["webOrderLineItemId"] = web_order_line_item_id
        if promotional_offer_id is not UNSET:
            field_dict["promotionalOfferId"] = promotional_offer_id
        if subscription_group_identifier is not UNSET:
            field_dict["subscriptionGroupIdentifier"] = subscription_group_identifier
        if is_trial_period is not UNSET:
            field_dict["isTrialPeriod"] = is_trial_period
        if is_in_intro_offer_period is not UNSET:
            field_dict["isInIntroOfferPeriod"] = is_in_intro_offer_period
        if is_upgraded is not UNSET:
            field_dict["isUpgraded"] = is_upgraded
        if expires_date is not UNSET:
            field_dict["expiresDate"] = expires_date
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if original_purchase_date is not UNSET:
            field_dict["originalPurchaseDate"] = original_purchase_date
        if cancellation_date is not UNSET:
            field_dict["cancellationDate"] = cancellation_date
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        product_id = d.pop("productId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        original_transaction_id = d.pop("originalTransactionId", UNSET)

        web_order_line_item_id = d.pop("webOrderLineItemId", UNSET)

        promotional_offer_id = d.pop("promotionalOfferId", UNSET)

        subscription_group_identifier = d.pop("subscriptionGroupIdentifier", UNSET)

        is_trial_period = d.pop("isTrialPeriod", UNSET)

        is_in_intro_offer_period = d.pop("isInIntroOfferPeriod", UNSET)

        is_upgraded = d.pop("isUpgraded", UNSET)

        _expires_date = d.pop("expiresDate", UNSET)
        expires_date: Union[Unset, datetime.datetime]
        if isinstance(_expires_date, Unset):
            expires_date = UNSET
        else:
            expires_date = isoparse(_expires_date)

        _purchase_date = d.pop("purchaseDate", UNSET)
        purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        _original_purchase_date = d.pop("originalPurchaseDate", UNSET)
        original_purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_original_purchase_date, Unset):
            original_purchase_date = UNSET
        else:
            original_purchase_date = isoparse(_original_purchase_date)

        _cancellation_date = d.pop("cancellationDate", UNSET)
        cancellation_date: Union[Unset, datetime.datetime]
        if isinstance(_cancellation_date, Unset):
            cancellation_date = UNSET
        else:
            cancellation_date = isoparse(_cancellation_date)

        cancellation_reason = d.pop("cancellationReason", UNSET)

        apple_app_store_receipt_item = cls(
            quantity=quantity,
            product_id=product_id,
            transaction_id=transaction_id,
            original_transaction_id=original_transaction_id,
            web_order_line_item_id=web_order_line_item_id,
            promotional_offer_id=promotional_offer_id,
            subscription_group_identifier=subscription_group_identifier,
            is_trial_period=is_trial_period,
            is_in_intro_offer_period=is_in_intro_offer_period,
            is_upgraded=is_upgraded,
            expires_date=expires_date,
            purchase_date=purchase_date,
            original_purchase_date=original_purchase_date,
            cancellation_date=cancellation_date,
            cancellation_reason=cancellation_reason,
        )

        apple_app_store_receipt_item.additional_properties = d
        return apple_app_store_receipt_item

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
