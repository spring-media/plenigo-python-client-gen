from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_status_change_status import CustomerStatusChangeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerStatusChange")


@_attrs_define
class CustomerStatusChange:
    """
    Attributes:
        status (Union[Unset, CustomerStatusChangeStatus]): new status the customer should become

            | Status      | Description
            |
            | ----------- | ------------------------------------------------------------------------------------------------
            ----------------------------------------------------------|
            | ACTIVATED   | customer is active and can log in and use full functionality
            |
            | BLOCKED     | customer is blocked and needs to reset his password to be able to log in again
            |
            | DEACTIVATED | customer is deactivated and cannot log in - the customer cannot change this state by himself and
            a log in attempt is handled like a false password log in |
    """

    status: Union[Unset, CustomerStatusChangeStatus] = UNSET
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
        status: Union[Unset, CustomerStatusChangeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CustomerStatusChangeStatus(_status)

        customer_status_change = cls(
            status=status,
        )

        customer_status_change.additional_properties = d
        return customer_status_change

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
