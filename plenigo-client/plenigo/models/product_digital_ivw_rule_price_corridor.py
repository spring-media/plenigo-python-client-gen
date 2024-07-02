import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductDigitalIvwRulePriceCorridor")


@_attrs_define
class ProductDigitalIvwRulePriceCorridor:
    """the ivw price corridors which should be used for this rule, starting with the lowest value.

    Attributes:
        key (Union[Unset, datetime.date]): date the price corridor is valid from in full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        value (Union[Unset, List[float]]):
    """

    key: Union[Unset, datetime.date] = UNSET
    value: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.isoformat()

        value: Union[Unset, List[float]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

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
        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, datetime.date]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = isoparse(_key).date()

        value = cast(List[float], d.pop("value", UNSET))

        product_digital_ivw_rule_price_corridor = cls(
            key=key,
            value=value,
        )

        product_digital_ivw_rule_price_corridor.additional_properties = d
        return product_digital_ivw_rule_price_corridor

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
