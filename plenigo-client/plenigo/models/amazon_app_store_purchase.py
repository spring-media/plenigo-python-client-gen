import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_store_response import AmazonAppStoreResponse


T = TypeVar("T", bound="AmazonAppStorePurchase")


@attr.s(auto_attribs=True)
class AmazonAppStorePurchase:
    """
    Attributes:
        amazon_app_store_purchase_id (Union[Unset, int]): unique identifier for the purchase
        changed_date (Union[Unset, datetime.datetime]): date time the purchase was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        purchase_date (Union[Unset, datetime.datetime]): date time the purchase was done with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        token (Union[Unset, str]): token for the purchase
        user_id (Union[Unset, str]): ID representing a distinct Amazon customer for your appstore app
        receipt_id (Union[Unset, str]): unique ID for the purchase
        valid (Union[Unset, bool]): flag indicating if purchase is valid
        app_store_order_id (Union[Unset, int]): id of the app store order if mapped
        response (Union[Unset, AmazonAppStoreResponse]):
    """

    amazon_app_store_purchase_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    token: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    receipt_id: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    app_store_order_id: Union[Unset, int] = UNSET
    response: Union[Unset, "AmazonAppStoreResponse"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_app_store_purchase_id = self.amazon_app_store_purchase_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        token = self.token
        user_id = self.user_id
        receipt_id = self.receipt_id
        valid = self.valid
        app_store_order_id = self.app_store_order_id
        response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_app_store_purchase_id is not UNSET:
            field_dict["amazonAppStorePurchaseId"] = amazon_app_store_purchase_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if receipt_id is not UNSET:
            field_dict["receiptId"] = receipt_id
        if valid is not UNSET:
            field_dict["valid"] = valid
        if app_store_order_id is not UNSET:
            field_dict["appStoreOrderId"] = app_store_order_id
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_app_store_response import AmazonAppStoreResponse

        d = src_dict.copy()
        amazon_app_store_purchase_id = d.pop("amazonAppStorePurchaseId", UNSET)

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

        user_id = d.pop("userId", UNSET)

        receipt_id = d.pop("receiptId", UNSET)

        valid = d.pop("valid", UNSET)

        app_store_order_id = d.pop("appStoreOrderId", UNSET)

        _response = d.pop("response", UNSET)
        response: Union[Unset, AmazonAppStoreResponse]
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = AmazonAppStoreResponse.from_dict(_response)

        amazon_app_store_purchase = cls(
            amazon_app_store_purchase_id=amazon_app_store_purchase_id,
            changed_date=changed_date,
            purchase_date=purchase_date,
            token=token,
            user_id=user_id,
            receipt_id=receipt_id,
            valid=valid,
            app_store_order_id=app_store_order_id,
            response=response,
        )

        amazon_app_store_purchase.additional_properties = d
        return amazon_app_store_purchase

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
