from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerInvoiceEmail")


@_attrs_define
class CustomerInvoiceEmail:
    """
    Attributes:
        invoice_email (Union[Unset, str]): invoice email address
    """

    invoice_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_email = self.invoice_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_email is not UNSET:
            field_dict["invoiceEmail"] = invoice_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_email = d.pop("invoiceEmail", UNSET)

        customer_invoice_email = cls(
            invoice_email=invoice_email,
        )

        customer_invoice_email.additional_properties = d
        return customer_invoice_email

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
