from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cross_client_transaction_paid_status_update_paid_status import (
    CrossClientTransactionPaidStatusUpdatePaidStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossClientTransactionPaidStatusUpdate")


@_attrs_define
class CrossClientTransactionPaidStatusUpdate:
    """
    Attributes:
        paid_status (Union[Unset, CrossClientTransactionPaidStatusUpdatePaidStatus]): paid status update
    """

    paid_status: Union[Unset, CrossClientTransactionPaidStatusUpdatePaidStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paid_status: Union[Unset, str] = UNSET
        if not isinstance(self.paid_status, Unset):
            paid_status = self.paid_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid_status is not UNSET:
            field_dict["paidStatus"] = paid_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _paid_status = d.pop("paidStatus", UNSET)
        paid_status: Union[Unset, CrossClientTransactionPaidStatusUpdatePaidStatus]
        if isinstance(_paid_status, Unset):
            paid_status = UNSET
        else:
            paid_status = CrossClientTransactionPaidStatusUpdatePaidStatus(_paid_status)

        cross_client_transaction_paid_status_update = cls(
            paid_status=paid_status,
        )

        cross_client_transaction_paid_status_update.additional_properties = d
        return cross_client_transaction_paid_status_update

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
