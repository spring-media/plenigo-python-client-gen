from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionChangeSuppressInvoiceSending")


@_attrs_define
class SubscriptionChangeSuppressInvoiceSending:
    """
    Attributes:
        suppress_invoice_sending (bool): flag indicating if the subscription invoice sending is suppressed
    """

    suppress_invoice_sending: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suppress_invoice_sending = self.suppress_invoice_sending

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suppressInvoiceSending": suppress_invoice_sending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suppress_invoice_sending = d.pop("suppressInvoiceSending")

        subscription_change_suppress_invoice_sending = cls(
            suppress_invoice_sending=suppress_invoice_sending,
        )

        subscription_change_suppress_invoice_sending.additional_properties = d
        return subscription_change_suppress_invoice_sending

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
