from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_marks_data_tags_key import CustomerMarksDataTagsKey
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wbz_customer_mark import WbzCustomerMark


T = TypeVar("T", bound="CustomerMarksDataTags")


@_attrs_define
class CustomerMarksDataTags:
    """
    Attributes:
        key (Union[Unset, CustomerMarksDataTagsKey]): customer tags
        value (Union[Unset, WbzCustomerMark]):
    """

    key: Union[Unset, CustomerMarksDataTagsKey] = UNSET
    value: Union[Unset, "WbzCustomerMark"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

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
        from ..models.wbz_customer_mark import WbzCustomerMark

        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, CustomerMarksDataTagsKey]
        if isinstance(_key, Unset) or not _key:
            key = UNSET
        else:
            key = CustomerMarksDataTagsKey(_key)

        _value = d.pop("value", UNSET)
        value: Union[Unset, WbzCustomerMark]
        if isinstance(_value, Unset) or not _value:
            value = UNSET
        else:
            value = WbzCustomerMark.from_dict(_value)

        customer_marks_data_tags = cls(
            key=key,
            value=value,
        )

        customer_marks_data_tags.additional_properties = d
        return customer_marks_data_tags

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
