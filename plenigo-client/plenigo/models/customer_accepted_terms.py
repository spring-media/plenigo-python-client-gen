from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.customer_accepted_term import CustomerAcceptedTerm


T = TypeVar("T", bound="CustomerAcceptedTerms")


@_attrs_define
class CustomerAcceptedTerms:
    """ """

    additional_properties: Dict[str, "CustomerAcceptedTerm"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_accepted_term import CustomerAcceptedTerm

        d = src_dict.copy()
        customer_accepted_terms = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CustomerAcceptedTerm.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        customer_accepted_terms.additional_properties = additional_properties
        return customer_accepted_terms

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CustomerAcceptedTerm":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CustomerAcceptedTerm") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
