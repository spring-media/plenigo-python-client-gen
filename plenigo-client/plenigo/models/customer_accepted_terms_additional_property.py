from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_accepted_term import CustomerAcceptedTerm


T = TypeVar("T", bound="CustomerAcceptedTermsAdditionalProperty")


@_attrs_define
class CustomerAcceptedTermsAdditionalProperty:
    """
    Attributes:
        key (Union[Unset, str]): id of the company opt in was accepted for
        value (Union[Unset, CustomerAcceptedTerm]):
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, "CustomerAcceptedTerm"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_accepted_term import CustomerAcceptedTerm

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, CustomerAcceptedTerm]
        if isinstance(_value, Unset) or not _value:
            value = UNSET
        else:
            value = CustomerAcceptedTerm.from_dict(_value)

        customer_accepted_terms_additional_property = cls(
            key=key,
            value=value,
        )

        customer_accepted_terms_additional_property.additional_properties = d
        return customer_accepted_terms_additional_property

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
