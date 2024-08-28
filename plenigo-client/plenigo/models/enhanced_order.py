import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.order_payment_method import OrderPaymentMethod
from ..models.order_status import OrderStatus
from ..models.order_type import OrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_used_by import ApiUsedBy
    from ..models.gift_info import GiftInfo
    from ..models.order_address import OrderAddress
    from ..models.order_item import OrderItem
    from ..models.payment_method_details import PaymentMethodDetails


T = TypeVar("T", bound="EnhancedOrder")


@_attrs_define
class EnhancedOrder:
    """
    Attributes:
        order_id (int): unique id of the order in the context of a company
        order_date (Union[None, datetime.datetime]): order date time of the order with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        accumulated_price (float): accumulated price of the order
        currency (str): currency of the order formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (OrderPaymentMethod): payment method used to pay for the order (ZERO indicates a free
            subscription)
        invoice_customer_id (str): id of the customer the invoice belongs to
        items (List['OrderItem']):
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
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
        invoice_address (Union[Unset, OrderAddress]):
        used_by (Union[Unset, ApiUsedBy]):
    """

    order_id: int
    order_date: Union[None, datetime.datetime]
    accumulated_price: float
    currency: str
    payment_method: OrderPaymentMethod
    invoice_customer_id: str
    items: List["OrderItem"]
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
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
    invoice_address: Union[Unset, "OrderAddress"] = UNSET
    used_by: Union[Unset, "ApiUsedBy"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        order_date: Union[None, str]
        if isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date

        accumulated_price = self.accumulated_price

        currency = self.currency

        payment_method = self.payment_method.value

        invoice_customer_id = self.invoice_customer_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
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

        invoice_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict()

        used_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.used_by, Unset):
            used_by = self.used_by.to_dict()

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
        if used_by is not UNSET:
            field_dict["usedBy"] = used_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_used_by import ApiUsedBy
        from ..models.gift_info import GiftInfo
        from ..models.order_address import OrderAddress
        from ..models.order_item import OrderItem
        from ..models.payment_method_details import PaymentMethodDetails

        d = src_dict.copy()
        order_id = d.pop("orderId")

        def _parse_order_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_date_type_0 = isoparse(data)

                return order_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        order_date = _parse_order_date(d.pop("orderDate"))

        accumulated_price = d.pop("accumulatedPrice")

        currency = d.pop("currency")

        payment_method = OrderPaymentMethod(d.pop("paymentMethod"))

        invoice_customer_id = d.pop("invoiceCustomerId")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            if isinstance(data, Unset):
                return data
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
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        external_system_id = d.pop("externalSystemId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        if isinstance(_status, Unset) or not _status:
            status = UNSET
        else:
            status = OrderStatus(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OrderType]
        if isinstance(_type, Unset) or not _type:
            type = UNSET
        else:
            type = OrderType(_type)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        _payment_method_details = d.pop("paymentMethodDetails", UNSET)
        payment_method_details: Union[Unset, PaymentMethodDetails]
        if isinstance(_payment_method_details, Unset) or not _payment_method_details:
            payment_method_details = UNSET
        else:
            payment_method_details = PaymentMethodDetails.from_dict(_payment_method_details)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        analog_invoice = d.pop("analogInvoice", UNSET)

        managed_external = d.pop("managedExternal", UNSET)

        suppress_invoice_sending = d.pop("suppressInvoiceSending", UNSET)

        _gift_info = d.pop("giftInfo", UNSET)
        gift_info: Union[Unset, GiftInfo]
        if isinstance(_gift_info, Unset) or not _gift_info:
            gift_info = UNSET
        else:
            gift_info = GiftInfo.from_dict(_gift_info)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, OrderAddress]
        if isinstance(_invoice_address, Unset) or not _invoice_address:
            invoice_address = UNSET
        else:
            invoice_address = OrderAddress.from_dict(_invoice_address)

        _used_by = d.pop("usedBy", UNSET)
        used_by: Union[Unset, ApiUsedBy]
        if isinstance(_used_by, Unset) or not _used_by:
            used_by = UNSET
        else:
            used_by = ApiUsedBy.from_dict(_used_by)

        enhanced_order = cls(
            order_id=order_id,
            order_date=order_date,
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
            used_by=used_by,
        )

        enhanced_order.additional_properties = d
        return enhanced_order

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
