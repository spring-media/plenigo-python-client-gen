import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invoice_payment_method import InvoicePaymentMethod
from ..models.invoice_status import InvoiceStatus
from ..models.invoice_type import InvoiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_address import InvoiceAddress
    from ..models.invoice_item import InvoiceItem


T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """
    Attributes:
        invoice_id (int): unique id of the invoice in the context of a company
        invoice_date (datetime.datetime): invoice date time of the invoice with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        accumulated_price (float): accumulated price of the invoice
        currency (str): currency of the invoice formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (InvoicePaymentMethod): payment method used to pay for the invoice
        invoice_customer_id (str): id of the customer the invoice belongs to
        items (List['InvoiceItem']):
        changed_date (Union[Unset, datetime.datetime]): date the invoice entity was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        customer_email (Union[Unset, str]): email used for sending invoice
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this invoice
        purchase_order_indicator (Union[Unset, str]): purchase invoice indicator if provided by the customer
        invoice_address (Union[Unset, InvoiceAddress]):
        transaction_id (Union[Unset, str]): id of the related transaction if payment was not done via invoice
        type (Union[Unset, InvoiceType]): type of the invoice
        status (Union[Unset, InvoiceStatus]): payment status of the invoice
        payment_changed_to_billing (Union[Unset, bool]): flag indicating if invoice was created because of a failed
            payment process
        precursor_id (Union[Unset, int]): invoice id which was corrected or canccelled
        successor_id (Union[Unset, int]): invoice id of the corrected invoice
        invoice_cancellation_id (Union[Unset, int]): invoice id of the cancellation invoice
    """

    invoice_id: int
    invoice_date: datetime.datetime
    accumulated_price: float
    currency: str
    payment_method: InvoicePaymentMethod
    invoice_customer_id: str
    items: List["InvoiceItem"]
    changed_date: Union[Unset, datetime.datetime] = UNSET
    customer_email: Union[Unset, str] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    invoice_address: Union[Unset, "InvoiceAddress"] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    type: Union[Unset, InvoiceType] = UNSET
    status: Union[Unset, InvoiceStatus] = UNSET
    payment_changed_to_billing: Union[Unset, bool] = UNSET
    precursor_id: Union[Unset, int] = UNSET
    successor_id: Union[Unset, int] = UNSET
    invoice_cancellation_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id
        invoice_date = self.invoice_date.isoformat()

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

        customer_email = self.customer_email
        payment_method_id = self.payment_method_id
        purchase_order_indicator = self.purchase_order_indicator
        invoice_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict()

        transaction_id = self.transaction_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_changed_to_billing = self.payment_changed_to_billing
        precursor_id = self.precursor_id
        successor_id = self.successor_id
        invoice_cancellation_id = self.invoice_cancellation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceId": invoice_id,
                "invoiceDate": invoice_date,
                "accumulatedPrice": accumulated_price,
                "currency": currency,
                "paymentMethod": payment_method,
                "invoiceCustomerId": invoice_customer_id,
                "items": items,
            }
        )
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if customer_email is not UNSET:
            field_dict["customerEmail"] = customer_email
        if payment_method_id is not UNSET:
            field_dict["paymentMethodId"] = payment_method_id
        if purchase_order_indicator is not UNSET:
            field_dict["purchaseOrderIndicator"] = purchase_order_indicator
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if payment_changed_to_billing is not UNSET:
            field_dict["paymentChangedToBilling"] = payment_changed_to_billing
        if precursor_id is not UNSET:
            field_dict["precursorId"] = precursor_id
        if successor_id is not UNSET:
            field_dict["successorId"] = successor_id
        if invoice_cancellation_id is not UNSET:
            field_dict["invoiceCancellationId"] = invoice_cancellation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_address import InvoiceAddress
        from ..models.invoice_item import InvoiceItem

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId")

        invoice_date = isoparse(d.pop("invoiceDate"))

        accumulated_price = d.pop("accumulatedPrice")

        currency = d.pop("currency")

        payment_method = InvoicePaymentMethod(d.pop("paymentMethod"))

        invoice_customer_id = d.pop("invoiceCustomerId")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        customer_email = d.pop("customerEmail", UNSET)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, InvoiceAddress]
        if isinstance(_invoice_address, Unset):
            invoice_address = UNSET
        else:
            invoice_address = InvoiceAddress.from_dict(_invoice_address)

        transaction_id = d.pop("transactionId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InvoiceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InvoiceType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        payment_changed_to_billing = d.pop("paymentChangedToBilling", UNSET)

        precursor_id = d.pop("precursorId", UNSET)

        successor_id = d.pop("successorId", UNSET)

        invoice_cancellation_id = d.pop("invoiceCancellationId", UNSET)

        invoice = cls(
            invoice_id=invoice_id,
            invoice_date=invoice_date,
            accumulated_price=accumulated_price,
            currency=currency,
            payment_method=payment_method,
            invoice_customer_id=invoice_customer_id,
            items=items,
            changed_date=changed_date,
            customer_email=customer_email,
            payment_method_id=payment_method_id,
            purchase_order_indicator=purchase_order_indicator,
            invoice_address=invoice_address,
            transaction_id=transaction_id,
            type=type,
            status=status,
            payment_changed_to_billing=payment_changed_to_billing,
            precursor_id=precursor_id,
            successor_id=successor_id,
            invoice_cancellation_id=invoice_cancellation_id,
        )

        invoice.additional_properties = d
        return invoice

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
