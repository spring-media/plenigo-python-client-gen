from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkout_address_settings_take_over import CheckoutAddressSettingsTakeOver
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutAddressSettings")


@_attrs_define
class CheckoutAddressSettings:
    """
    Attributes:
        take_over (Union[Unset, CheckoutAddressSettingsTakeOver]): flag that controls the checkbox to automatically take
            over one address as another (e.g. invoice address as delivery address) and indirectly
            controls the flow of the checkout because if e.g. DELIVERY_ADDRESS_DEFAULT is selected the delivery address will
            be requested first if required -
            the default value is INVOICE_ADDRESS_DEFAULT
        invoice_address_required (Union[Unset, bool]): is the invoice address required during the checkout
        delivery_address_required (Union[Unset, bool]): is the delivery address required during the checkout
    """

    take_over: Union[Unset, CheckoutAddressSettingsTakeOver] = UNSET
    invoice_address_required: Union[Unset, bool] = UNSET
    delivery_address_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        take_over: Union[Unset, str] = UNSET
        if not isinstance(self.take_over, Unset):
            take_over = self.take_over.value

        invoice_address_required = self.invoice_address_required

        delivery_address_required = self.delivery_address_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if take_over is not UNSET:
            field_dict["takeOver"] = take_over
        if invoice_address_required is not UNSET:
            field_dict["invoiceAddressRequired"] = invoice_address_required
        if delivery_address_required is not UNSET:
            field_dict["deliveryAddressRequired"] = delivery_address_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _take_over = d.pop("takeOver", UNSET)
        take_over: Union[Unset, CheckoutAddressSettingsTakeOver]
        if isinstance(_take_over, Unset) or not _take_over:
            take_over = UNSET
        else:
            take_over = CheckoutAddressSettingsTakeOver(_take_over)

        invoice_address_required = d.pop("invoiceAddressRequired", UNSET)

        delivery_address_required = d.pop("deliveryAddressRequired", UNSET)

        checkout_address_settings = cls(
            take_over=take_over,
            invoice_address_required=invoice_address_required,
            delivery_address_required=delivery_address_required,
        )

        checkout_address_settings.additional_properties = d
        return checkout_address_settings

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
