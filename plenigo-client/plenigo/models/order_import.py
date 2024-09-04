import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.order_import_managed_by import OrderImportManagedBy
from ..models.order_import_payment_method import OrderImportPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderImport")


@_attrs_define
class OrderImport:
    """
    Attributes:
        external_system_id (str): external system id of the order import
        plenigo_offer_id (str): unique id of the offer within a company
        invoice_customer_id (str): id of the customer the order belongs to
        quantity (int): purchase quantity
        start_date (Union[None, datetime.datetime]): date time the order was created and also the start date of the
            subscription with date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6"
            target="_blank">RFC 3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        payment_method (OrderImportPaymentMethod): payment method used to pay for the order (ZERO indicates a free
            subscription)
        invoice_address_id (Union[Unset, int]): unique id of the invoice address to use for this order
        variant_delivery_address_id (Union[Unset, int]): variant delivery address for deliveries
        delivery_customer_id (Union[Unset, str]): id of the delivery customer the order belongs to
        delivery_address_id (Union[Unset, int]): unique id of the delivery address to use for this order
        discount_percentage (Union[Unset, int]): discount offered to the order item
        order_date (Union[None, Unset, datetime.datetime]): date time the order was done if differs from start date with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        end_date (Union[None, Unset, datetime.datetime]): date time the subscriptions ends with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        reference_start_date (Union[None, Unset, datetime.datetime]): date time that should be used as reference for
            bookings and cancellations with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z - must not be before the start date and not more than one year in the past
        next_booking_date (Union[None, Unset, datetime.datetime]): date time the subscription should be booked with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this order
        plenigo_bonus_ids (Union[Unset, List[str]]): if the offer should contain bonuses the plenigo bonus id can be
            added here
        managed_by (Union[Unset, OrderImportManagedBy]): managed by of the given order.
    """

    external_system_id: str
    plenigo_offer_id: str
    invoice_customer_id: str
    quantity: int
    start_date: Union[None, datetime.datetime]
    payment_method: OrderImportPaymentMethod
    invoice_address_id: Union[Unset, int] = UNSET
    variant_delivery_address_id: Union[Unset, int] = UNSET
    delivery_customer_id: Union[Unset, str] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    order_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    reference_start_date: Union[None, Unset, datetime.datetime] = UNSET
    next_booking_date: Union[None, Unset, datetime.datetime] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
    managed_by: Union[Unset, OrderImportManagedBy] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_system_id = self.external_system_id

        plenigo_offer_id = self.plenigo_offer_id

        invoice_customer_id = self.invoice_customer_id

        quantity = self.quantity

        start_date: Union[None, str]
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        payment_method = self.payment_method.value

        invoice_address_id = self.invoice_address_id

        variant_delivery_address_id = self.variant_delivery_address_id

        delivery_customer_id = self.delivery_customer_id

        delivery_address_id = self.delivery_address_id

        discount_percentage = self.discount_percentage

        order_date: Union[None, Unset, str]
        if isinstance(self.order_date, Unset) or self.order_date is None:
            order_date = UNSET
        elif isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset) or self.end_date is None:
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        reference_start_date: Union[None, Unset, str]
        if isinstance(self.reference_start_date, Unset) or self.reference_start_date is None:
            reference_start_date = UNSET
        elif isinstance(self.reference_start_date, datetime.datetime):
            reference_start_date = self.reference_start_date.isoformat()
        else:
            reference_start_date = self.reference_start_date

        next_booking_date: Union[None, Unset, str]
        if isinstance(self.next_booking_date, Unset) or self.next_booking_date is None:
            next_booking_date = UNSET
        elif isinstance(self.next_booking_date, datetime.datetime):
            next_booking_date = self.next_booking_date.isoformat()
        else:
            next_booking_date = self.next_booking_date

        payment_method_id = self.payment_method_id

        plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.plenigo_bonus_ids, Unset):
            plenigo_bonus_ids = self.plenigo_bonus_ids

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value

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
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_system_id = d.pop("externalSystemId")

        plenigo_offer_id = d.pop("plenigoOfferId")

        invoice_customer_id = d.pop("invoiceCustomerId")

        quantity = d.pop("quantity")

        def _parse_start_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("startDate"))

        payment_method = OrderImportPaymentMethod(d.pop("paymentMethod"))

        invoice_address_id = d.pop("invoiceAddressId", UNSET)

        variant_delivery_address_id = d.pop("variantDeliveryAddressId", UNSET)

        delivery_customer_id = d.pop("deliveryCustomerId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        def _parse_order_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                order_date_type_0 = isoparse(data)

                return order_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        order_date = _parse_order_date(d.pop("orderDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_reference_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                reference_start_date_type_0 = isoparse(data)

                return reference_start_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        reference_start_date = _parse_reference_start_date(d.pop("referenceStartDate", UNSET))

        def _parse_next_booking_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                next_booking_date_type_0 = isoparse(data)

                return next_booking_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        next_booking_date = _parse_next_booking_date(d.pop("nextBookingDate", UNSET))

        payment_method_id = d.pop("paymentMethodId", UNSET)

        plenigo_bonus_ids = cast(List[str], d.pop("plenigoBonusIds", UNSET))

        _managed_by = d.pop("managedBy", UNSET)
        managed_by: Union[Unset, OrderImportManagedBy]
        if isinstance(_managed_by, Unset) or not _managed_by:
            managed_by = UNSET
        else:
            managed_by = OrderImportManagedBy(_managed_by)

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
            managed_by=managed_by,
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
