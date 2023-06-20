import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apple_app_store_receipt import AppleAppStoreReceipt


T = TypeVar("T", bound="AppleAppStorePurchase")


@attr.s(auto_attribs=True)
class AppleAppStorePurchase:
    """
    Attributes:
        apple_app_store_purchase_id (Union[Unset, int]): unique id of the purchase
        changed_date (Union[Unset, datetime.datetime]): date time the purchase entity was changed with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        purchase_date (Union[Unset, datetime.datetime]): date of the purchase
        token (Union[Unset, str]): token for the purchase
        valid (Union[Unset, bool]): flag indicating if purchase is valid
        app_store_order_id (Union[Unset, int]): id of the app store order if mapped
        receipt (Union[Unset, AppleAppStoreReceipt]):
    """

    apple_app_store_purchase_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    token: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    app_store_order_id: Union[Unset, int] = UNSET
    receipt: Union[Unset, "AppleAppStoreReceipt"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apple_app_store_purchase_id = self.apple_app_store_purchase_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        token = self.token
        valid = self.valid
        app_store_order_id = self.app_store_order_id
        receipt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receipt, Unset):
            receipt = self.receipt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple_app_store_purchase_id is not UNSET:
            field_dict["appleAppStorePurchaseId"] = apple_app_store_purchase_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if token is not UNSET:
            field_dict["token"] = token
        if valid is not UNSET:
            field_dict["valid"] = valid
        if app_store_order_id is not UNSET:
            field_dict["appStoreOrderId"] = app_store_order_id
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apple_app_store_receipt import AppleAppStoreReceipt

        d = src_dict.copy()
        apple_app_store_purchase_id = d.pop("appleAppStorePurchaseId", UNSET)

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

        valid = d.pop("valid", UNSET)

        app_store_order_id = d.pop("appStoreOrderId", UNSET)

        _receipt = d.pop("receipt", UNSET)
        receipt: Union[Unset, AppleAppStoreReceipt]
        if isinstance(_receipt, Unset):
            receipt = UNSET
        else:
            receipt = AppleAppStoreReceipt.from_dict(_receipt)

        apple_app_store_purchase = cls(
            apple_app_store_purchase_id=apple_app_store_purchase_id,
            changed_date=changed_date,
            purchase_date=purchase_date,
            token=token,
            valid=valid,
            app_store_order_id=app_store_order_id,
            receipt=receipt,
        )

        apple_app_store_purchase.additional_properties = d
        return apple_app_store_purchase

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
