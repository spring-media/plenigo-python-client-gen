from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.refund_status_change_status import RefundStatusChangeStatus

T = TypeVar("T", bound="RefundStatusChange")


@_attrs_define
class RefundStatusChange:
    """
    Attributes:
        status (RefundStatusChangeStatus): status of the refund
        reason (str): reason for status change
    """

    status: RefundStatusChangeStatus
    reason: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = RefundStatusChangeStatus(d.pop("status"))

        reason = d.pop("reason")

        refund_status_change = cls(
            status=status,
            reason=reason,
        )

        refund_status_change.additional_properties = d
        return refund_status_change

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
