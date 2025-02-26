import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_payment_method import InvoicePaymentMethod
from ..models.invoice_status import InvoiceStatus
from ..models.invoice_type import InvoiceType
from ..models.user_type import UserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_address import InvoiceAddress
    from ..models.invoice_item import InvoiceItem


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        invoice_id (int): unique id of the invoice in the context of a company
        invoice_date (Union[None, datetime.datetime]): invoice date time of the invoice with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        accumulated_price (float): accumulated price of the invoice
        currency (str): currency of the invoice formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (InvoicePaymentMethod): payment method used to pay for the invoice
        invoice_customer_id (str): id of the customer the invoice belongs to
        items (list['InvoiceItem']):
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, UserType]): type of user who performs the action
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, UserType]): type of user who performs the action
        customer_email (Union[Unset, str]): email used for sending invoice
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this invoice
        purchase_order_indicator (Union[Unset, str]): purchase invoice indicator if provided by the customer
        invoice_address (Union[Unset, InvoiceAddress]):
        transaction_id (Union[Unset, str]): id of the related transaction if payment was not done via invoice
        type_ (Union[Unset, InvoiceType]): type of the invoice
        status (Union[Unset, InvoiceStatus]): payment status of the invoice
        payment_changed_to_billing (Union[Unset, bool]): flag indicating if invoice was created because of a failed
            payment process
        precursor_id (Union[Unset, int]): invoice id which was corrected or cancelled
        successor_id (Union[Unset, int]): invoice id of the corrected invoice
        cancellation_invoice_id (Union[Unset, int]): invoice id of the cancellation invoice
    """

    invoice_id: int
    invoice_date: Union[None, datetime.datetime]
    accumulated_price: float
    currency: str
    payment_method: InvoicePaymentMethod
    invoice_customer_id: str
    items: list["InvoiceItem"]
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    customer_email: Union[Unset, str] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    invoice_address: Union[Unset, "InvoiceAddress"] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    type_: Union[Unset, InvoiceType] = UNSET
    status: Union[Unset, InvoiceStatus] = UNSET
    payment_changed_to_billing: Union[Unset, bool] = UNSET
    precursor_id: Union[Unset, int] = UNSET
    successor_id: Union[Unset, int] = UNSET
    cancellation_invoice_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        invoice_date: Union[None, str]
        if isinstance(self.invoice_date, datetime.datetime):
            invoice_date = self.invoice_date.isoformat()
        else:
            invoice_date = self.invoice_date

        accumulated_price = self.accumulated_price

        currency = self.currency

        payment_method = self.payment_method.value

        invoice_customer_id = self.invoice_customer_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        customer_email = self.customer_email

        payment_method_id = self.payment_method_id

        purchase_order_indicator = self.purchase_order_indicator

        invoice_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict()

        transaction_id = self.transaction_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_changed_to_billing = self.payment_changed_to_billing

        precursor_id = self.precursor_id

        successor_id = self.successor_id

        cancellation_invoice_id = self.cancellation_invoice_id

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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if payment_changed_to_billing is not UNSET:
            field_dict["paymentChangedToBilling"] = payment_changed_to_billing
        if precursor_id is not UNSET:
            field_dict["precursorId"] = precursor_id
        if successor_id is not UNSET:
            field_dict["successorId"] = successor_id
        if cancellation_invoice_id is not UNSET:
            field_dict["cancellationInvoiceId"] = cancellation_invoice_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_address import InvoiceAddress
        from ..models.invoice_item import InvoiceItem

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId")

        def _parse_invoice_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_date_type_0 = isoparse(data)

                return invoice_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.datetime], data)

        invoice_date = _parse_invoice_date(d.pop("invoiceDate"))

        accumulated_price = d.pop("accumulatedPrice")

        currency = d.pop("currency")

        payment_method = InvoicePaymentMethod(d.pop("paymentMethod"))

        invoice_customer_id = d.pop("invoiceCustomerId")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, UserType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = UserType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, UserType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = UserType(_changed_by_type)

        customer_email = d.pop("customerEmail", UNSET)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, InvoiceAddress]
        if isinstance(_invoice_address, Unset) or not _invoice_address:
            invoice_address = UNSET
        else:
            invoice_address = InvoiceAddress.from_dict(_invoice_address)

        transaction_id = d.pop("transactionId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, InvoiceType]
        if isinstance(_type_, Unset) or not _type_:
            type_ = UNSET
        else:
            type_ = InvoiceType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatus]
        if isinstance(_status, Unset) or not _status:
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        payment_changed_to_billing = d.pop("paymentChangedToBilling", UNSET)

        precursor_id = d.pop("precursorId", UNSET)

        successor_id = d.pop("successorId", UNSET)

        cancellation_invoice_id = d.pop("cancellationInvoiceId", UNSET)

        invoice = cls(
            invoice_id=invoice_id,
            invoice_date=invoice_date,
            accumulated_price=accumulated_price,
            currency=currency,
            payment_method=payment_method,
            invoice_customer_id=invoice_customer_id,
            items=items,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            customer_email=customer_email,
            payment_method_id=payment_method_id,
            purchase_order_indicator=purchase_order_indicator,
            invoice_address=invoice_address,
            transaction_id=transaction_id,
            type_=type_,
            status=status,
            payment_changed_to_billing=payment_changed_to_billing,
            precursor_id=precursor_id,
            successor_id=successor_id,
            cancellation_invoice_id=cancellation_invoice_id,
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
