import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_payment_method import OrderPaymentMethod
from ..models.order_status import OrderStatus
from ..models.order_type import OrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_info import GiftInfo
    from ..models.order_address import OrderAddress
    from ..models.order_item import OrderItem
    from ..models.payment_method_details import PaymentMethodDetails


T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """
    Attributes:
        order_id (int): unique id of the order in the context of a company
        order_date (datetime.datetime): order date time of the order with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        accumulated_price (float): accumulated price of the order
        currency (str): currency of the order formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (OrderPaymentMethod): payment method used to pay for the order (ZERO indicates a free
            subscription)
        invoice_customer_id (str): id of the customer the invoice belongs to
        items (List['OrderItem']):
        changed_date (Union[Unset, datetime.datetime]): date the order entity was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        external_system_id (Union[Unset, str]): if order was imported from another system this field contains the unique
            id of the other system
        status (Union[Unset, OrderStatus]): current status of the order
        type (Union[Unset, OrderType]): current type of the order
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this order
        payment_method_details (Union[Unset, PaymentMethodDetails]):
        purchase_order_indicator (Union[Unset, str]): purchase order indicator if provided by the customer
        analog_invoice (Union[Unset, bool]): flag indicating if order should produce analog invoices
        managed_external (Union[Unset, bool]): flag indicates if a subscription is not managed by plenigo
        suppress_invoice_sending (Union[Unset, bool]): flag indicating if the subscription invoice sending is suppressed
        gift_info (Union[Unset, GiftInfo]):
        invoice_address (Union[Unset, None, OrderAddress]):
    """

    order_id: int
    order_date: datetime.datetime
    accumulated_price: float
    currency: str
    payment_method: OrderPaymentMethod
    invoice_customer_id: str
    items: List["OrderItem"]
    changed_date: Union[Unset, datetime.datetime] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    status: Union[Unset, OrderStatus] = UNSET
    type: Union[Unset, OrderType] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    payment_method_details: Union[Unset, "PaymentMethodDetails"] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    analog_invoice: Union[Unset, bool] = UNSET
    managed_external: Union[Unset, bool] = UNSET
    suppress_invoice_sending: Union[Unset, bool] = UNSET
    gift_info: Union[Unset, "GiftInfo"] = UNSET
    invoice_address: Union[Unset, None, "OrderAddress"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        order_date = self.order_date.isoformat()

        accumulated_price = self.accumulated_price
        currency = self.currency
        payment_method = self.payment_method.value

        invoice_customer_id = self.invoice_customer_id
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        external_system_id = self.external_system_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        payment_method_id = self.payment_method_id
        payment_method_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_details, Unset):
            payment_method_details = self.payment_method_details.to_dict()

        purchase_order_indicator = self.purchase_order_indicator
        analog_invoice = self.analog_invoice
        managed_external = self.managed_external
        suppress_invoice_sending = self.suppress_invoice_sending
        gift_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_info, Unset):
            gift_info = self.gift_info.to_dict()

        invoice_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict() if self.invoice_address else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "orderDate": order_date,
                "accumulatedPrice": accumulated_price,
                "currency": currency,
                "paymentMethod": payment_method,
                "invoiceCustomerId": invoice_customer_id,
                "items": items,
            }
        )
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if external_system_id is not UNSET:
            field_dict["externalSystemId"] = external_system_id
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if payment_method_id is not UNSET:
            field_dict["paymentMethodId"] = payment_method_id
        if payment_method_details is not UNSET:
            field_dict["paymentMethodDetails"] = payment_method_details
        if purchase_order_indicator is not UNSET:
            field_dict["purchaseOrderIndicator"] = purchase_order_indicator
        if analog_invoice is not UNSET:
            field_dict["analogInvoice"] = analog_invoice
        if managed_external is not UNSET:
            field_dict["managedExternal"] = managed_external
        if suppress_invoice_sending is not UNSET:
            field_dict["suppressInvoiceSending"] = suppress_invoice_sending
        if gift_info is not UNSET:
            field_dict["giftInfo"] = gift_info
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_info import GiftInfo
        from ..models.order_address import OrderAddress
        from ..models.order_item import OrderItem
        from ..models.payment_method_details import PaymentMethodDetails

        d = src_dict.copy()
        order_id = d.pop("orderId")

        order_date = isoparse(d.pop("orderDate"))

        accumulated_price = d.pop("accumulatedPrice")

        currency = d.pop("currency")

        payment_method = OrderPaymentMethod(d.pop("paymentMethod"))

        invoice_customer_id = d.pop("invoiceCustomerId")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        external_system_id = d.pop("externalSystemId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderStatus(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OrderType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OrderType(_type)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        _payment_method_details = d.pop("paymentMethodDetails", UNSET)
        payment_method_details: Union[Unset, PaymentMethodDetails]
        if isinstance(_payment_method_details, Unset):
            payment_method_details = UNSET
        else:
            payment_method_details = PaymentMethodDetails.from_dict(_payment_method_details)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        analog_invoice = d.pop("analogInvoice", UNSET)

        managed_external = d.pop("managedExternal", UNSET)

        suppress_invoice_sending = d.pop("suppressInvoiceSending", UNSET)

        _gift_info = d.pop("giftInfo", UNSET)
        gift_info: Union[Unset, GiftInfo]
        if isinstance(_gift_info, Unset):
            gift_info = UNSET
        else:
            gift_info = GiftInfo.from_dict(_gift_info)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, None, OrderAddress]
        if _invoice_address is None:
            invoice_address = None
        elif isinstance(_invoice_address, Unset):
            invoice_address = UNSET
        else:
            invoice_address = OrderAddress.from_dict(_invoice_address)

        order = cls(
            order_id=order_id,
            order_date=order_date,
            accumulated_price=accumulated_price,
            currency=currency,
            payment_method=payment_method,
            invoice_customer_id=invoice_customer_id,
            items=items,
            changed_date=changed_date,
            external_system_id=external_system_id,
            status=status,
            type=type,
            payment_method_id=payment_method_id,
            payment_method_details=payment_method_details,
            purchase_order_indicator=purchase_order_indicator,
            analog_invoice=analog_invoice,
            managed_external=managed_external,
            suppress_invoice_sending=suppress_invoice_sending,
            gift_info=gift_info,
            invoice_address=invoice_address,
        )

        order.additional_properties = d
        return order

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
