from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opt_in_update_status import OptInUpdateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptInUpdate")


@_attrs_define
class OptInUpdate:
    """
    Attributes:
        status (Union[Unset, OptInUpdateStatus]): status of the opt in
    """

    status: Union[Unset, OptInUpdateStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, OptInUpdateStatus]
        if isinstance(_status, Unset) or not _status:
            status = UNSET
        else:
            status = OptInUpdateStatus(_status)

        opt_in_update = cls(
            status=status,
        )

        opt_in_update.additional_properties = d
        return opt_in_update

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
