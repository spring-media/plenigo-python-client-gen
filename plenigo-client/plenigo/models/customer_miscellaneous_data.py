from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerMiscellaneousData")


@_attrs_define
class CustomerMiscellaneousData:
    """
    Attributes:
        leitweg_id (Union[Unset, str]): leitweg id used for xml invoices
    """

    leitweg_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leitweg_id = self.leitweg_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leitweg_id is not UNSET:
            field_dict["leitwegId"] = leitweg_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        leitweg_id = d.pop("leitwegId", UNSET)

        customer_miscellaneous_data = cls(
            leitweg_id=leitweg_id,
        )

        customer_miscellaneous_data.additional_properties = d
        return customer_miscellaneous_data

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
