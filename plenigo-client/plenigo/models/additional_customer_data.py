from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_customer_data_data import AdditionalCustomerDataData


T = TypeVar("T", bound="AdditionalCustomerData")


@_attrs_define
class AdditionalCustomerData:
    """
    Attributes:
        data (Union[Unset, AdditionalCustomerDataData]):
    """

    data: Union[Unset, "AdditionalCustomerDataData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_customer_data_data import AdditionalCustomerDataData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, AdditionalCustomerDataData]
        if isinstance(_data, Unset) or not _data:
            data = UNSET
        else:
            data = AdditionalCustomerDataData.from_dict(_data)

        additional_customer_data = cls(
            data=data,
        )

        additional_customer_data.additional_properties = d
        return additional_customer_data

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
