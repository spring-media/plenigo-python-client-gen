import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_address import InvoiceAddress


T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    """
    Attributes:
        position (int): position of the invoice item inside the invoice - creates a unique invoice item id in
            combination with the invoiceId
        title (str): title of the item
        price (float): price of the invoice item
        tax (float): tax percentage operated on this invoice item
        tax_country (str): country tax is based on formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        quantity (int): purchase amount
        delivery_customer_id (str): id of the customer the delivery belongs to (also includes digital products)
        product_id (Union[Unset, str]): product id - will be identical with the plenigo product id if not overwritten
            during checkout
        plenigo_offer_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo offer id is
            provided here
        plenigo_product_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo product id is
            provided here
        plenigo_step_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo step id is provided
            here
        cost_center (Union[Unset, str]): cost center associated with this product at the time of invoice creation
        delivery_address (Union[Unset, InvoiceAddress]):
        subscription_item_id (Union[Unset, int]): if invoice item represents a subscription the id of the subscription
            item is provided here
        period_start_date (Union[Unset, datetime.datetime]): if invoice item represents a subscription the period start
            date is the start date of the invoice period
        period_end_date (Union[Unset, datetime.datetime]): if invoice item represents a subscription the period end date
            is the end date of the invoice period
        order_item_id (Union[Unset, int]): if invoice item represents an order the id of the order item is provided here
        discount_percentage (Union[Unset, int]): discount offered to the invoice item
    """

    position: int
    title: str
    price: float
    tax: float
    tax_country: str
    quantity: int
    delivery_customer_id: str
    product_id: Union[Unset, str] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    plenigo_product_id: Union[Unset, str] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    delivery_address: Union[Unset, "InvoiceAddress"] = UNSET
    subscription_item_id: Union[Unset, int] = UNSET
    period_start_date: Union[Unset, datetime.datetime] = UNSET
    period_end_date: Union[Unset, datetime.datetime] = UNSET
    order_item_id: Union[Unset, int] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        title = self.title
        price = self.price
        tax = self.tax
        tax_country = self.tax_country
        quantity = self.quantity
        delivery_customer_id = self.delivery_customer_id
        product_id = self.product_id
        plenigo_offer_id = self.plenigo_offer_id
        plenigo_product_id = self.plenigo_product_id
        plenigo_step_id = self.plenigo_step_id
        cost_center = self.cost_center
        delivery_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_address, Unset):
            delivery_address = self.delivery_address.to_dict()

        subscription_item_id = self.subscription_item_id
        period_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.period_start_date, Unset):
            period_start_date = self.period_start_date.isoformat()

        period_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.period_end_date, Unset):
            period_end_date = self.period_end_date.isoformat()

        order_item_id = self.order_item_id
        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "title": title,
                "price": price,
                "tax": tax,
                "taxCountry": tax_country,
                "quantity": quantity,
                "deliveryCustomerId": delivery_customer_id,
            }
        )
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if plenigo_product_id is not UNSET:
            field_dict["plenigoProductId"] = plenigo_product_id
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if subscription_item_id is not UNSET:
            field_dict["subscriptionItemId"] = subscription_item_id
        if period_start_date is not UNSET:
            field_dict["periodStartDate"] = period_start_date
        if period_end_date is not UNSET:
            field_dict["periodEndDate"] = period_end_date
        if order_item_id is not UNSET:
            field_dict["orderItemId"] = order_item_id
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_address import InvoiceAddress

        d = src_dict.copy()
        position = d.pop("position")

        title = d.pop("title")

        price = d.pop("price")

        tax = d.pop("tax")

        tax_country = d.pop("taxCountry")

        quantity = d.pop("quantity")

        delivery_customer_id = d.pop("deliveryCustomerId")

        product_id = d.pop("productId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        _delivery_address = d.pop("deliveryAddress", UNSET)
        delivery_address: Union[Unset, InvoiceAddress]
        if isinstance(_delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = InvoiceAddress.from_dict(_delivery_address)

        subscription_item_id = d.pop("subscriptionItemId", UNSET)

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

        order_item_id = d.pop("orderItemId", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        invoice_item = cls(
            position=position,
            title=title,
            price=price,
            tax=tax,
            tax_country=tax_country,
            quantity=quantity,
            delivery_customer_id=delivery_customer_id,
            product_id=product_id,
            plenigo_offer_id=plenigo_offer_id,
            plenigo_product_id=plenigo_product_id,
            plenigo_step_id=plenigo_step_id,
            cost_center=cost_center,
            delivery_address=delivery_address,
            subscription_item_id=subscription_item_id,
            period_start_date=period_start_date,
            period_end_date=period_end_date,
            order_item_id=order_item_id,
            discount_percentage=discount_percentage,
        )

        invoice_item.additional_properties = d
        return invoice_item

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
