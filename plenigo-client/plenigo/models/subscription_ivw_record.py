import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.subscription_ivw_record_ivw_price_type import SubscriptionIvwRecordIvwPriceType
from ..models.subscription_ivw_record_ivw_type import SubscriptionIvwRecordIvwType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionIvwRecord")


@attr.s(auto_attribs=True)
class SubscriptionIvwRecord:
    """
    Attributes:
        subscription_ivw_record_id (int): unique id of the subscription ivw record in the context of a company
        subscription_id (int): unique id of the subscription in the context of a company
        customer_id (str): id of the customer the record belongs to (also includes digital products)
        title (str): title of the subscripiton ivw record
        ivw_rule_title (str): ivw rule title of the subscripiton ivw record
        ivw_type (SubscriptionIvwRecordIvwType): ivw type of the subscription ivw record
        ivw_price_type (SubscriptionIvwRecordIvwPriceType): ivw price type of the subscription ivw record
        country (str): country code formatted as <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"
            target="_blank">ISO 3166-1 alpha-2</a>
        subscription_item_id (Union[Unset, int]): unique id of the subscription item in the context of a company
        delivery_date (Union[Unset, datetime.datetime]): delivery date time of the subscription IVW record with date-
            time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        full_price_divergence_up (Union[Unset, float]): the divergence up to the price to be the specified ivw type
        full_price_divergence_down (Union[Unset, float]): the divergence down to the price to be the specified ivw type
        other_price_divergence_down (Union[Unset, float]): the divergence down to the price to be the specified ivw type
        full_ivw_price (Union[Unset, float]): full ivw price of the subscription ivw record
        other_sale_ivw_price (Union[Unset, float]): other sale ivw price of the subscription ivw record
        invoice_id (Union[Unset, int]): unique id of the invoice in the context of a company
        invoice_date (Union[Unset, datetime.datetime]): invoice date time of the invoice with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        quantity (Union[Unset, int]): purchase amount
        discount_percentage (Union[Unset, int]): discount offered to the invoice item
        discount (Union[Unset, float]): discount price of the subscription ivw record
        tax (Union[Unset, float]): tax percentage operated on this invoice item
        tax_country (Union[Unset, str]): country tax is based on formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        price (Union[Unset, float]): price of the invoice
        period_start_date (Union[Unset, datetime.datetime]): period start date time of the invoice with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        period_end_date (Union[Unset, datetime.datetime]): period end date time of the invoice with date-time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21T17:32:28Z
        deliveries (Union[Unset, int]): deliveries in time of the period
        purchase_order_indicator (Union[Unset, str]): purchase order indicator to set
    """

    subscription_ivw_record_id: int
    subscription_id: int
    customer_id: str
    title: str
    ivw_rule_title: str
    ivw_type: SubscriptionIvwRecordIvwType
    ivw_price_type: SubscriptionIvwRecordIvwPriceType
    country: str
    subscription_item_id: Union[Unset, int] = UNSET
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    full_price_divergence_up: Union[Unset, float] = UNSET
    full_price_divergence_down: Union[Unset, float] = UNSET
    other_price_divergence_down: Union[Unset, float] = UNSET
    full_ivw_price: Union[Unset, float] = UNSET
    other_sale_ivw_price: Union[Unset, float] = UNSET
    invoice_id: Union[Unset, int] = UNSET
    invoice_date: Union[Unset, datetime.datetime] = UNSET
    quantity: Union[Unset, int] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    discount: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    tax_country: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    period_start_date: Union[Unset, datetime.datetime] = UNSET
    period_end_date: Union[Unset, datetime.datetime] = UNSET
    deliveries: Union[Unset, int] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_ivw_record_id = self.subscription_ivw_record_id
        subscription_id = self.subscription_id
        customer_id = self.customer_id
        title = self.title
        ivw_rule_title = self.ivw_rule_title
        ivw_type = self.ivw_type.value

        ivw_price_type = self.ivw_price_type.value

        country = self.country
        subscription_item_id = self.subscription_item_id
        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        full_price_divergence_up = self.full_price_divergence_up
        full_price_divergence_down = self.full_price_divergence_down
        other_price_divergence_down = self.other_price_divergence_down
        full_ivw_price = self.full_ivw_price
        other_sale_ivw_price = self.other_sale_ivw_price
        invoice_id = self.invoice_id
        invoice_date: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_date, Unset):
            invoice_date = self.invoice_date.isoformat()

        quantity = self.quantity
        discount_percentage = self.discount_percentage
        discount = self.discount
        tax = self.tax
        tax_country = self.tax_country
        price = self.price
        period_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.period_start_date, Unset):
            period_start_date = self.period_start_date.isoformat()

        period_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.period_end_date, Unset):
            period_end_date = self.period_end_date.isoformat()

        deliveries = self.deliveries
        purchase_order_indicator = self.purchase_order_indicator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionIvwRecordId": subscription_ivw_record_id,
                "subscriptionId": subscription_id,
                "customerId": customer_id,
                "title": title,
                "ivwRuleTitle": ivw_rule_title,
                "ivwType": ivw_type,
                "ivwPriceType": ivw_price_type,
                "country": country,
            }
        )
        if subscription_item_id is not UNSET:
            field_dict["subscriptionItemId"] = subscription_item_id
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if full_price_divergence_up is not UNSET:
            field_dict["fullPriceDivergenceUp"] = full_price_divergence_up
        if full_price_divergence_down is not UNSET:
            field_dict["fullPriceDivergenceDown"] = full_price_divergence_down
        if other_price_divergence_down is not UNSET:
            field_dict["otherPriceDivergenceDown"] = other_price_divergence_down
        if full_ivw_price is not UNSET:
            field_dict["fullIvwPrice"] = full_ivw_price
        if other_sale_ivw_price is not UNSET:
            field_dict["otherSaleIvwPrice"] = other_sale_ivw_price
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if discount is not UNSET:
            field_dict["discount"] = discount
        if tax is not UNSET:
            field_dict["tax"] = tax
        if tax_country is not UNSET:
            field_dict["taxCountry"] = tax_country
        if price is not UNSET:
            field_dict["price"] = price
        if period_start_date is not UNSET:
            field_dict["periodStartDate"] = period_start_date
        if period_end_date is not UNSET:
            field_dict["periodEndDate"] = period_end_date
        if deliveries is not UNSET:
            field_dict["deliveries"] = deliveries
        if purchase_order_indicator is not UNSET:
            field_dict["purchaseOrderIndicator"] = purchase_order_indicator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_ivw_record_id = d.pop("subscriptionIvwRecordId")

        subscription_id = d.pop("subscriptionId")

        customer_id = d.pop("customerId")

        title = d.pop("title")

        ivw_rule_title = d.pop("ivwRuleTitle")

        ivw_type = SubscriptionIvwRecordIvwType(d.pop("ivwType"))

        ivw_price_type = SubscriptionIvwRecordIvwPriceType(d.pop("ivwPriceType"))

        country = d.pop("country")

        subscription_item_id = d.pop("subscriptionItemId", UNSET)

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        full_price_divergence_up = d.pop("fullPriceDivergenceUp", UNSET)

        full_price_divergence_down = d.pop("fullPriceDivergenceDown", UNSET)

        other_price_divergence_down = d.pop("otherPriceDivergenceDown", UNSET)

        full_ivw_price = d.pop("fullIvwPrice", UNSET)

        other_sale_ivw_price = d.pop("otherSaleIvwPrice", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        _invoice_date = d.pop("invoiceDate", UNSET)
        invoice_date: Union[Unset, datetime.datetime]
        if isinstance(_invoice_date, Unset):
            invoice_date = UNSET
        else:
            invoice_date = isoparse(_invoice_date)

        quantity = d.pop("quantity", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        discount = d.pop("discount", UNSET)

        tax = d.pop("tax", UNSET)

        tax_country = d.pop("taxCountry", UNSET)

        price = d.pop("price", UNSET)

        _period_start_date = d.pop("periodStartDate", UNSET)
        period_start_date: Union[Unset, datetime.datetime]
        if isinstance(_period_start_date, Unset):
            period_start_date = UNSET
        else:
            period_start_date = isoparse(_period_start_date)

        _period_end_date = d.pop("periodEndDate", UNSET)
        period_end_date: Union[Unset, datetime.datetime]
        if isinstance(_period_end_date, Unset):
            period_end_date = UNSET
        else:
            period_end_date = isoparse(_period_end_date)

        deliveries = d.pop("deliveries", UNSET)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        subscription_ivw_record = cls(
            subscription_ivw_record_id=subscription_ivw_record_id,
            subscription_id=subscription_id,
            customer_id=customer_id,
            title=title,
            ivw_rule_title=ivw_rule_title,
            ivw_type=ivw_type,
            ivw_price_type=ivw_price_type,
            country=country,
            subscription_item_id=subscription_item_id,
            delivery_date=delivery_date,
            full_price_divergence_up=full_price_divergence_up,
            full_price_divergence_down=full_price_divergence_down,
            other_price_divergence_down=other_price_divergence_down,
            full_ivw_price=full_ivw_price,
            other_sale_ivw_price=other_sale_ivw_price,
            invoice_id=invoice_id,
            invoice_date=invoice_date,
            quantity=quantity,
            discount_percentage=discount_percentage,
            discount=discount,
            tax=tax,
            tax_country=tax_country,
            price=price,
            period_start_date=period_start_date,
            period_end_date=period_end_date,
            deliveries=deliveries,
            purchase_order_indicator=purchase_order_indicator,
        )

        subscription_ivw_record.additional_properties = d
        return subscription_ivw_record

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
