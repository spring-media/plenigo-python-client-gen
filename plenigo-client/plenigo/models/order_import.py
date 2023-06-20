import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.order_import_payment_method import OrderImportPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderImport")


@attr.s(auto_attribs=True)
class OrderImport:
    """
    Attributes:
        external_system_id (str): external system id of the order import
        plenigo_offer_id (str): unique id of the offer within a company
        invoice_customer_id (str): id of the customer the order belongs to
        quantity (int): purchase quantity
        start_date (datetime.datetime): date time the order was created and also the start date of the subscription with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        payment_method (OrderImportPaymentMethod): payment method used to pay for the order (ZERO indicates a free
            subscription)
        invoice_address_id (Union[Unset, int]): unique id of the invoice address to use for this order
        variant_delivery_address_id (Union[Unset, int]): variant delivery address for deliveries
        delivery_customer_id (Union[Unset, str]): id of the delivery customer the order belongs to
        delivery_address_id (Union[Unset, int]): unique id of the delivery address to use for this order
        discount_percentage (Union[Unset, int]): discount offered to the order item
        order_date (Union[Unset, datetime.datetime]): date time the order was done if differs from start date with date-
            time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        end_date (Union[Unset, datetime.datetime]): date time the subscriptions ends with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        reference_start_date (Union[Unset, datetime.datetime]): date time that should be used as reference for bookings
            and cancellations with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z - must not be before the start date and not more than one year in the past
        next_booking_date (Union[Unset, datetime.datetime]): date time the subscription should be booked with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this order
        plenigo_bonus_ids (Union[Unset, List[str]]): if the offer should contain bonuses the plenigo bonus id can be
            added here
    """

    external_system_id: str
    plenigo_offer_id: str
    invoice_customer_id: str
    quantity: int
    start_date: datetime.datetime
    payment_method: OrderImportPaymentMethod
    invoice_address_id: Union[Unset, int] = UNSET
    variant_delivery_address_id: Union[Unset, int] = UNSET
    delivery_customer_id: Union[Unset, str] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    order_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    reference_start_date: Union[Unset, datetime.datetime] = UNSET
    next_booking_date: Union[Unset, datetime.datetime] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_system_id = self.external_system_id
        plenigo_offer_id = self.plenigo_offer_id
        invoice_customer_id = self.invoice_customer_id
        quantity = self.quantity
        start_date = self.start_date.isoformat()

        payment_method = self.payment_method.value

        invoice_address_id = self.invoice_address_id
        variant_delivery_address_id = self.variant_delivery_address_id
        delivery_customer_id = self.delivery_customer_id
        delivery_address_id = self.delivery_address_id
        discount_percentage = self.discount_percentage
        order_date: Union[Unset, str] = UNSET
        if not isinstance(self.order_date, Unset):
            order_date = self.order_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        reference_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.reference_start_date, Unset):
            reference_start_date = self.reference_start_date.isoformat()

        next_booking_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_booking_date, Unset):
            next_booking_date = self.next_booking_date.isoformat()

        payment_method_id = self.payment_method_id
        plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.plenigo_bonus_ids, Unset):
            plenigo_bonus_ids = self.plenigo_bonus_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalSystemId": external_system_id,
                "plenigoOfferId": plenigo_offer_id,
                "invoiceCustomerId": invoice_customer_id,
                "quantity": quantity,
                "startDate": start_date,
                "paymentMethod": payment_method,
            }
        )
        if invoice_address_id is not UNSET:
            field_dict["invoiceAddressId"] = invoice_address_id
        if variant_delivery_address_id is not UNSET:
            field_dict["variantDeliveryAddressId"] = variant_delivery_address_id
        if delivery_customer_id is not UNSET:
            field_dict["deliveryCustomerId"] = delivery_customer_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if reference_start_date is not UNSET:
            field_dict["referenceStartDate"] = reference_start_date
        if next_booking_date is not UNSET:
            field_dict["nextBookingDate"] = next_booking_date
        if payment_method_id is not UNSET:
            field_dict["paymentMethodId"] = payment_method_id
        if plenigo_bonus_ids is not UNSET:
            field_dict["plenigoBonusIds"] = plenigo_bonus_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_system_id = d.pop("externalSystemId")

        plenigo_offer_id = d.pop("plenigoOfferId")

        invoice_customer_id = d.pop("invoiceCustomerId")

        quantity = d.pop("quantity")

        start_date = isoparse(d.pop("startDate"))

        payment_method = OrderImportPaymentMethod(d.pop("paymentMethod"))

        invoice_address_id = d.pop("invoiceAddressId", UNSET)

        variant_delivery_address_id = d.pop("variantDeliveryAddressId", UNSET)

        delivery_customer_id = d.pop("deliveryCustomerId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        _order_date = d.pop("orderDate", UNSET)
        order_date: Union[Unset, datetime.datetime]
        if isinstance(_order_date, Unset):
            order_date = UNSET
        else:
            order_date = isoparse(_order_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _reference_start_date = d.pop("referenceStartDate", UNSET)
        reference_start_date: Union[Unset, datetime.datetime]
        if isinstance(_reference_start_date, Unset):
            reference_start_date = UNSET
        else:
            reference_start_date = isoparse(_reference_start_date)

        _next_booking_date = d.pop("nextBookingDate", UNSET)
        next_booking_date: Union[Unset, datetime.datetime]
        if isinstance(_next_booking_date, Unset):
            next_booking_date = UNSET
        else:
            next_booking_date = isoparse(_next_booking_date)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        plenigo_bonus_ids = cast(List[str], d.pop("plenigoBonusIds", UNSET))

        order_import = cls(
            external_system_id=external_system_id,
            plenigo_offer_id=plenigo_offer_id,
            invoice_customer_id=invoice_customer_id,
            quantity=quantity,
            start_date=start_date,
            payment_method=payment_method,
            invoice_address_id=invoice_address_id,
            variant_delivery_address_id=variant_delivery_address_id,
            delivery_customer_id=delivery_customer_id,
            delivery_address_id=delivery_address_id,
            discount_percentage=discount_percentage,
            order_date=order_date,
            end_date=end_date,
            reference_start_date=reference_start_date,
            next_booking_date=next_booking_date,
            payment_method_id=payment_method_id,
            plenigo_bonus_ids=plenigo_bonus_ids,
        )

        order_import.additional_properties = d
        return order_import

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
