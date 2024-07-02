from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppleAppStorePurchaseAddition")


@_attrs_define
class AppleAppStorePurchaseAddition:
    """
    Attributes:
        app_identifier (Union[Unset, str]): identifier of the application as defined in the plenigo backend to retrieve
            the according secret
        receipt_data (Union[Unset, List[str]]):
    """

    app_identifier: Union[Unset, str] = UNSET
    receipt_data: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_identifier = self.app_identifier

        receipt_data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.receipt_data, Unset):
            receipt_data = self.receipt_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_identifier is not UNSET:
            field_dict["appIdentifier"] = app_identifier
        if receipt_data is not UNSET:
            field_dict["receiptData"] = receipt_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_identifier = d.pop("appIdentifier", UNSET)

        receipt_data = cast(List[str], d.pop("receiptData", UNSET))

        apple_app_store_purchase_addition = cls(
            app_identifier=app_identifier,
            receipt_data=receipt_data,
        )

        apple_app_store_purchase_addition.additional_properties = d
        return apple_app_store_purchase_addition

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
