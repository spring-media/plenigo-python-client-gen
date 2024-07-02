import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_access_rights import AppStoreAccessRights


T = TypeVar("T", bound="AppStorePurchaseDetail")


@_attrs_define
class AppStorePurchaseDetail:
    """
    Attributes:
        purchase_date (Union[None, Unset, datetime.datetime]): date the product was purchased with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        valid (Union[Unset, bool]): flag indicating purchase is still valid
        access_right_unique_id (Union[Unset, str]): access right unique id that will be associated with this app store
            purchase after association
        app_store_product_id (Union[Unset, str]): id of the product as set in the app store
        access_rights (Union[Unset, AppStoreAccessRights]):
    """

    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    valid: Union[Unset, bool] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    app_store_product_id: Union[Unset, str] = UNSET
    access_rights: Union[Unset, "AppStoreAccessRights"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_date: Union[None, Unset, str]
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        valid = self.valid

        access_right_unique_id = self.access_right_unique_id

        app_store_product_id = self.app_store_product_id

        access_rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_rights, Unset):
            access_rights = self.access_rights.to_dict()

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
        if access_rights is not UNSET:
            field_dict["accessRights"] = access_rights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_store_access_rights import AppStoreAccessRights

        d = src_dict.copy()

        def _parse_purchase_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_1 = isoparse(data)

                return purchase_date_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        purchase_date = _parse_purchase_date(d.pop("purchaseDate", UNSET))

        valid = d.pop("valid", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        app_store_product_id = d.pop("appStoreProductId", UNSET)

        _access_rights = d.pop("accessRights", UNSET)
        access_rights: Union[Unset, AppStoreAccessRights]
        if isinstance(_access_rights, Unset):
            access_rights = UNSET
        else:
            access_rights = AppStoreAccessRights.from_dict(_access_rights)

        app_store_purchase_detail = cls(
            purchase_date=purchase_date,
            valid=valid,
            access_right_unique_id=access_right_unique_id,
            app_store_product_id=app_store_product_id,
            access_rights=access_rights,
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
