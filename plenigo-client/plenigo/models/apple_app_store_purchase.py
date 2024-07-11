import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apple_app_store_receipt import AppleAppStoreReceipt


T = TypeVar("T", bound="AppleAppStorePurchase")


@_attrs_define
class AppleAppStorePurchase:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        apple_app_store_purchase_id (Union[Unset, int]): unique id of the purchase
        purchase_date (Union[None, Unset, datetime.datetime]): date of the purchase
        token (Union[Unset, str]): token for the purchase
        valid (Union[Unset, bool]): flag indicating if purchase is valid
        app_store_order_id (Union[Unset, int]): id of the app store order if mapped
        receipt (Union[Unset, AppleAppStoreReceipt]):
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    apple_app_store_purchase_id: Union[Unset, int] = UNSET
    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    token: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    app_store_order_id: Union[Unset, int] = UNSET
    receipt: Union[Unset, "AppleAppStoreReceipt"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        apple_app_store_purchase_id = self.apple_app_store_purchase_id

        purchase_date: Union[None, Unset, str]
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        token = self.token

        valid = self.valid

        app_store_order_id = self.app_store_order_id

        receipt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receipt, Unset):
            receipt = self.receipt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if apple_app_store_purchase_id is not UNSET:
            field_dict["appleAppStorePurchaseId"] = apple_app_store_purchase_id
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset):
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        apple_app_store_purchase_id = d.pop("appleAppStorePurchaseId", UNSET)

        def _parse_purchase_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)

                return purchase_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        purchase_date = _parse_purchase_date(d.pop("purchaseDate", UNSET))

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
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            apple_app_store_purchase_id=apple_app_store_purchase_id,
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
