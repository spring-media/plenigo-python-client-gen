import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_play_product_purchase import GooglePlayProductPurchase
    from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase


T = TypeVar("T", bound="GooglePlayStorePurchase")


@attr.s(auto_attribs=True)
class GooglePlayStorePurchase:
    """
    Attributes:
        google_play_store_purchase_id (Union[Unset, int]): unique id of the purchase
        changed_date (Union[Unset, datetime.datetime]): date time the purchase was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        purchase_date (Union[Unset, datetime.datetime]): date time the purchase was done with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        token (Union[Unset, str]): token for the purchase
        package_name (Union[Unset, str]): package name of the application the inapp product was sold in
        product_id (Union[Unset, str]): inapp product SKU (for example, 'com.some.thing.inapp1')
        valid (Union[Unset, bool]): flag indicating if purchase is valid
        subscription (Union[Unset, bool]): flag indicating if purchase represents a subscription
        purchase_token (Union[Unset, str]): token provided to the user's device when the inapp product was purchased
        app_store_order_id (Union[Unset, int]): id of the app store order if mapped
        subscription_purchase (Union[Unset, GooglePlaySubscriptionPurchase]):
        product_purchase (Union[Unset, GooglePlayProductPurchase]):
    """

    google_play_store_purchase_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    token: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    subscription: Union[Unset, bool] = UNSET
    purchase_token: Union[Unset, str] = UNSET
    app_store_order_id: Union[Unset, int] = UNSET
    subscription_purchase: Union[Unset, "GooglePlaySubscriptionPurchase"] = UNSET
    product_purchase: Union[Unset, "GooglePlayProductPurchase"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        google_play_store_purchase_id = self.google_play_store_purchase_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        token = self.token
        package_name = self.package_name
        product_id = self.product_id
        valid = self.valid
        subscription = self.subscription
        purchase_token = self.purchase_token
        app_store_order_id = self.app_store_order_id
        subscription_purchase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscription_purchase, Unset):
            subscription_purchase = self.subscription_purchase.to_dict()

        product_purchase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_purchase, Unset):
            product_purchase = self.product_purchase.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if google_play_store_purchase_id is not UNSET:
            field_dict["googlePlayStorePurchaseId"] = google_play_store_purchase_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if token is not UNSET:
            field_dict["token"] = token
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if valid is not UNSET:
            field_dict["valid"] = valid
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if purchase_token is not UNSET:
            field_dict["purchaseToken"] = purchase_token
        if app_store_order_id is not UNSET:
            field_dict["appStoreOrderId"] = app_store_order_id
        if subscription_purchase is not UNSET:
            field_dict["subscriptionPurchase"] = subscription_purchase
        if product_purchase is not UNSET:
            field_dict["productPurchase"] = product_purchase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        d = src_dict.copy()
        google_play_store_purchase_id = d.pop("googlePlayStorePurchaseId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        _purchase_date = d.pop("purchaseDate", UNSET)
        purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        token = d.pop("token", UNSET)

        package_name = d.pop("packageName", UNSET)

        product_id = d.pop("productId", UNSET)

        valid = d.pop("valid", UNSET)

        subscription = d.pop("subscription", UNSET)

        purchase_token = d.pop("purchaseToken", UNSET)

        app_store_order_id = d.pop("appStoreOrderId", UNSET)

        _subscription_purchase = d.pop("subscriptionPurchase", UNSET)
        subscription_purchase: Union[Unset, GooglePlaySubscriptionPurchase]
        if isinstance(_subscription_purchase, Unset):
            subscription_purchase = UNSET
        else:
            subscription_purchase = GooglePlaySubscriptionPurchase.from_dict(_subscription_purchase)

        _product_purchase = d.pop("productPurchase", UNSET)
        product_purchase: Union[Unset, GooglePlayProductPurchase]
        if isinstance(_product_purchase, Unset):
            product_purchase = UNSET
        else:
            product_purchase = GooglePlayProductPurchase.from_dict(_product_purchase)

        google_play_store_purchase = cls(
            google_play_store_purchase_id=google_play_store_purchase_id,
            changed_date=changed_date,
            purchase_date=purchase_date,
            token=token,
            package_name=package_name,
            product_id=product_id,
            valid=valid,
            subscription=subscription,
            purchase_token=purchase_token,
            app_store_order_id=app_store_order_id,
            subscription_purchase=subscription_purchase,
            product_purchase=product_purchase,
        )

        google_play_store_purchase.additional_properties = d
        return google_play_store_purchase

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
