from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opt_ins_opt_ins_key import OptInsOptInsKey
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opt_in import OptIn


T = TypeVar("T", bound="OptInsOptIns")


@_attrs_define
class OptInsOptIns:
    """
    Attributes:
        key (Union[Unset, OptInsOptInsKey]): opt in type
        value (Union[Unset, OptIn]):
    """

    key: Union[Unset, OptInsOptInsKey] = UNSET
    value: Union[Unset, "OptIn"] = UNSET
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
        from ..models.opt_in import OptIn

        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, OptInsOptInsKey]
        if isinstance(_key, Unset) or not _key:
            key = UNSET
        else:
            key = OptInsOptInsKey(_key)

        _value = d.pop("value", UNSET)
        value: Union[Unset, OptIn]
        if isinstance(_value, Unset) or not _value:
            value = UNSET
        else:
            value = OptIn.from_dict(_value)

        opt_ins_opt_ins = cls(
            key=key,
            value=value,
        )

        opt_ins_opt_ins.additional_properties = d
        return opt_ins_opt_ins

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
