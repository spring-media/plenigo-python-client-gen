from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invoice_payment_status_change_status import InvoicePaymentStatusChangeStatus

T = TypeVar("T", bound="InvoicePaymentStatusChange")


@attr.s(auto_attribs=True)
class InvoicePaymentStatusChange:
    """
    Attributes:
        status (InvoicePaymentStatusChangeStatus): payment status of the invoice
    """

    status: InvoicePaymentStatusChangeStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = InvoicePaymentStatusChangeStatus(d.pop("status"))

        invoice_payment_status_change = cls(
            status=status,
        )

        invoice_payment_status_change.additional_properties = d
        return invoice_payment_status_change

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
