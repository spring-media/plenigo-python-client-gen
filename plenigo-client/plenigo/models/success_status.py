from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuccessStatus")


@_attrs_define
class SuccessStatus:
    """
    Attributes:
        success (Union[Unset, bool]): success status
        promise_id (Union[Unset, str]): in case of long running calls it contains the id that identifies the
            corresponding callback that contains the result
    """

    success: Union[Unset, bool] = UNSET
    promise_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        promise_id = self.promise_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if promise_id is not UNSET:
            field_dict["promiseId"] = promise_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success", UNSET)

        promise_id = d.pop("promiseId", UNSET)

        success_status = cls(
            success=success,
            promise_id=promise_id,
        )

        success_status.additional_properties = d
        return success_status

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
