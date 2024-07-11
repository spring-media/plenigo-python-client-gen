from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_play_store_purchase_addition_element import GooglePlayStorePurchaseAdditionElement


T = TypeVar("T", bound="GooglePlayStorePurchaseAddition")


@_attrs_define
class GooglePlayStorePurchaseAddition:
    """
    Attributes:
        package_name (Union[Unset, str]): package name of the application this purchase was done for (for example,
            'com.some.thing').
        receipt_data (Union[Unset, List['GooglePlayStorePurchaseAdditionElement']]):
    """

    package_name: Union[Unset, str] = UNSET
    receipt_data: Union[Unset, List["GooglePlayStorePurchaseAdditionElement"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_name = self.package_name

        receipt_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.receipt_data, Unset):
            receipt_data = []
            for receipt_data_item_data in self.receipt_data:
                receipt_data_item = receipt_data_item_data.to_dict()
                receipt_data.append(receipt_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if receipt_data is not UNSET:
            field_dict["receiptData"] = receipt_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_play_store_purchase_addition_element import GooglePlayStorePurchaseAdditionElement

        d = src_dict.copy()
        package_name = d.pop("packageName", UNSET)

        receipt_data = []
        _receipt_data = d.pop("receiptData", UNSET)
        for receipt_data_item_data in _receipt_data or []:
            receipt_data_item = GooglePlayStorePurchaseAdditionElement.from_dict(receipt_data_item_data)

            receipt_data.append(receipt_data_item)

        google_play_store_purchase_addition = cls(
            package_name=package_name,
            receipt_data=receipt_data,
        )

        google_play_store_purchase_addition.additional_properties = d
        return google_play_store_purchase_addition

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
