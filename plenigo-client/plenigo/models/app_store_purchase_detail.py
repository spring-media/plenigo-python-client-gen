import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStorePurchaseDetail")


@attr.s(auto_attribs=True)
class AppStorePurchaseDetail:
    """
    Attributes:
        purchase_date (Union[Unset, datetime.datetime]): date the product was purchased with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        valid (Union[Unset, bool]): flag indicating purchase is still valid
        access_right_unique_id (Union[Unset, str]): access right unique id that will be associated with this app store
            purchase after association
        app_store_product_id (Union[Unset, str]): id of the product as set in the app store
    """

    purchase_date: Union[Unset, datetime.datetime] = UNSET
    valid: Union[Unset, bool] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    app_store_product_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        valid = self.valid
        access_right_unique_id = self.access_right_unique_id
        app_store_product_id = self.app_store_product_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if valid is not UNSET:
            field_dict["valid"] = valid
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id
        if app_store_product_id is not UNSET:
            field_dict["appStoreProductId"] = app_store_product_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _purchase_date = d.pop("purchaseDate", UNSET)
        purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        valid = d.pop("valid", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        app_store_product_id = d.pop("appStoreProductId", UNSET)

        app_store_purchase_detail = cls(
            purchase_date=purchase_date,
            valid=valid,
            access_right_unique_id=access_right_unique_id,
            app_store_product_id=app_store_product_id,
        )

        app_store_purchase_detail.additional_properties = d
        return app_store_purchase_detail

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
