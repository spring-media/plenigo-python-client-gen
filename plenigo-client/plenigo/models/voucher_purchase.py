from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_order_data import AdditionalOrderData


T = TypeVar("T", bound="VoucherPurchase")


@_attrs_define
class VoucherPurchase:
    """
    Attributes:
        customer_id (str): unique id of the customer the checkout is for
        customer_ip_address (str): ip address of the customer
        voucher_code (str): voucher code to use
        customer_session (Union[Unset, str]): active customer session - if a customer id is provided the customer id
            overrules the session
        invoice_address_id (Union[Unset, int]): unique id of the invoice address to use
        delivery_address_id (Union[Unset, int]): unique id of the delivery address to use
        additional_data (Union[Unset, AdditionalOrderData]):
        overwritten_product_id (Union[Unset, str]): add a custom product id during the voucher checkout - this is only
            allowed for a single offer with one single purchase in it
    """

    customer_id: str
    customer_ip_address: str
    voucher_code: str
    customer_session: Union[Unset, str] = UNSET
    invoice_address_id: Union[Unset, int] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    additional_data: Union[Unset, "AdditionalOrderData"] = UNSET
    overwritten_product_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        customer_ip_address = self.customer_ip_address

        voucher_code = self.voucher_code

        customer_session = self.customer_session

        invoice_address_id = self.invoice_address_id

        delivery_address_id = self.delivery_address_id

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        overwritten_product_id = self.overwritten_product_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "customerIpAddress": customer_ip_address,
                "voucherCode": voucher_code,
            }
        )
        if customer_session is not UNSET:
            field_dict["customerSession"] = customer_session
        if invoice_address_id is not UNSET:
            field_dict["invoiceAddressId"] = invoice_address_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if overwritten_product_id is not UNSET:
            field_dict["overwrittenProductId"] = overwritten_product_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_order_data import AdditionalOrderData

        d = src_dict.copy()
        customer_id = d.pop("customerId")

        customer_ip_address = d.pop("customerIpAddress")

        voucher_code = d.pop("voucherCode")

        customer_session = d.pop("customerSession", UNSET)

        invoice_address_id = d.pop("invoiceAddressId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, AdditionalOrderData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = AdditionalOrderData.from_dict(_additional_data)

        overwritten_product_id = d.pop("overwrittenProductId", UNSET)

        voucher_purchase = cls(
            customer_id=customer_id,
            customer_ip_address=customer_ip_address,
            voucher_code=voucher_code,
            customer_session=customer_session,
            invoice_address_id=invoice_address_id,
            delivery_address_id=delivery_address_id,
            additional_data=additional_data,
            overwritten_product_id=overwritten_product_id,
        )

        voucher_purchase.additional_properties = d
        return voucher_purchase

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
