from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.additional_customer_data_data_additional_property import AdditionalCustomerDataDataAdditionalProperty


T = TypeVar("T", bound="AdditionalCustomerDataData")


@_attrs_define
class AdditionalCustomerDataData:
    """ """

    additional_properties: Dict[str, "AdditionalCustomerDataDataAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_customer_data_data_additional_property import (
            AdditionalCustomerDataDataAdditionalProperty,
        )

        d = src_dict.copy()
        additional_customer_data_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AdditionalCustomerDataDataAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        additional_customer_data_data.additional_properties = additional_properties
        return additional_customer_data_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AdditionalCustomerDataDataAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AdditionalCustomerDataDataAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
