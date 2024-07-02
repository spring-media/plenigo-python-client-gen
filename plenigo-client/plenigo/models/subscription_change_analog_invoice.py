from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionChangeAnalogInvoice")


@_attrs_define
class SubscriptionChangeAnalogInvoice:
    """
    Attributes:
        analog_invoice (bool): flag indicating if the subscription is a analog invoice
    """

    analog_invoice: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        analog_invoice = self.analog_invoice

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analogInvoice": analog_invoice,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        analog_invoice = d.pop("analogInvoice")

        subscription_change_analog_invoice = cls(
            analog_invoice=analog_invoice,
        )

        subscription_change_analog_invoice.additional_properties = d
        return subscription_change_analog_invoice

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
