import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_item_tax_type import OrderItemTaxType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_address import OrderAddress
    from ..models.voucher_purchase_data import VoucherPurchaseData
    from ..models.voucher_usage_data import VoucherUsageData


T = TypeVar("T", bound="OrderItem")


@attr.s(auto_attribs=True)
class OrderItem:
    """
    Attributes:
        position (int): position of the order item inside the order - creates a unique order item id in combination with
            the orderId
        product_id (str): id of the product bought
        title (str): product title presented to the customer
        tax_type (OrderItemTaxType): unique identification of the tax type the product represents - important for tax
            handling purposes
        price (float): price of the order item
        tax (float): tax percentage operated on this order item
        tax_country (str): country tax is based on formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        quantity (int): purchase quantity
        discount_percentage (int): discount offered to the order item
        delivery_customer_id (str): id of the customer the delivery belongs to (also includes digital products)
        plenigo_offer_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo offer id is
            provided here
        plenigo_product_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo product id is
            provided here - can be identically to the productId
        plenigo_step_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo step id is provided
            here
        access_right_unique_id (Union[Unset, str]): unique id of the access right this order item grants access to
        internal_title (Union[Unset, str]): if the product is based on a plenigo offer the product title for internal
            usage is provided here
        cost_center (Union[Unset, str]): cost center associated with this product at the time of order creation
        voucher_code (Union[Unset, str]): voucher code to purchase this order item
        delivery_address (Union[Unset, OrderAddress]):
        subscription_item_id (Union[Unset, int]): if order item represents a subscription the id of the subscription
            item is provided here
        external_billing (Union[Unset, bool]): indicates if payments are handled by plenigo or an external system
        tax_state (Union[Unset, str]): country state used for taxes - only needed in USA and Brasil
        purchased_addon_id (Union[Unset, int]): unique id of the purchased addon
        validity_end_date (Union[Unset, datetime.datetime]): validity end date with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        voucher_purchase (Union[Unset, VoucherPurchaseData]):
        voucher_usage (Union[Unset, VoucherUsageData]):
    """

    position: int
    product_id: str
    title: str
    tax_type: OrderItemTaxType
    price: float
    tax: float
    tax_country: str
    quantity: int
    discount_percentage: int
    delivery_customer_id: str
    plenigo_offer_id: Union[Unset, str] = UNSET
    plenigo_product_id: Union[Unset, str] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    internal_title: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    voucher_code: Union[Unset, str] = UNSET
    delivery_address: Union[Unset, "OrderAddress"] = UNSET
    subscription_item_id: Union[Unset, int] = UNSET
    external_billing: Union[Unset, bool] = UNSET
    tax_state: Union[Unset, str] = UNSET
    purchased_addon_id: Union[Unset, int] = UNSET
    validity_end_date: Union[Unset, datetime.datetime] = UNSET
    voucher_purchase: Union[Unset, "VoucherPurchaseData"] = UNSET
    voucher_usage: Union[Unset, "VoucherUsageData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        product_id = self.product_id
        title = self.title
        tax_type = self.tax_type.value

        price = self.price
        tax = self.tax
        tax_country = self.tax_country
        quantity = self.quantity
        discount_percentage = self.discount_percentage
        delivery_customer_id = self.delivery_customer_id
        plenigo_offer_id = self.plenigo_offer_id
        plenigo_product_id = self.plenigo_product_id
        plenigo_step_id = self.plenigo_step_id
        access_right_unique_id = self.access_right_unique_id
        internal_title = self.internal_title
        cost_center = self.cost_center
        voucher_code = self.voucher_code
        delivery_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_address, Unset):
            delivery_address = self.delivery_address.to_dict()

        subscription_item_id = self.subscription_item_id
        external_billing = self.external_billing
        tax_state = self.tax_state
        purchased_addon_id = self.purchased_addon_id
        validity_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.validity_end_date, Unset):
            validity_end_date = self.validity_end_date.isoformat()

        voucher_purchase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voucher_purchase, Unset):
            voucher_purchase = self.voucher_purchase.to_dict()

        voucher_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voucher_usage, Unset):
            voucher_usage = self.voucher_usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "productId": product_id,
                "title": title,
                "taxType": tax_type,
                "price": price,
                "tax": tax,
                "taxCountry": tax_country,
                "quantity": quantity,
                "discountPercentage": discount_percentage,
                "deliveryCustomerId": delivery_customer_id,
            }
        )
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if plenigo_product_id is not UNSET:
            field_dict["plenigoProductId"] = plenigo_product_id
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if voucher_code is not UNSET:
            field_dict["voucherCode"] = voucher_code
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if subscription_item_id is not UNSET:
            field_dict["subscriptionItemId"] = subscription_item_id
        if external_billing is not UNSET:
            field_dict["externalBilling"] = external_billing
        if tax_state is not UNSET:
            field_dict["taxState"] = tax_state
        if purchased_addon_id is not UNSET:
            field_dict["purchasedAddonId"] = purchased_addon_id
        if validity_end_date is not UNSET:
            field_dict["validityEndDate"] = validity_end_date
        if voucher_purchase is not UNSET:
            field_dict["voucherPurchase"] = voucher_purchase
        if voucher_usage is not UNSET:
            field_dict["voucherUsage"] = voucher_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_address import OrderAddress
        from ..models.voucher_purchase_data import VoucherPurchaseData
        from ..models.voucher_usage_data import VoucherUsageData

        d = src_dict.copy()
        position = d.pop("position")

        product_id = d.pop("productId")

        title = d.pop("title")

        tax_type = OrderItemTaxType(d.pop("taxType"))

        price = d.pop("price")

        tax = d.pop("tax")

        tax_country = d.pop("taxCountry")

        quantity = d.pop("quantity")

        discount_percentage = d.pop("discountPercentage")

        delivery_customer_id = d.pop("deliveryCustomerId")

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        internal_title = d.pop("internalTitle", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        voucher_code = d.pop("voucherCode", UNSET)

        _delivery_address = d.pop("deliveryAddress", UNSET)
        delivery_address: Union[Unset, OrderAddress]
        if isinstance(_delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = OrderAddress.from_dict(_delivery_address)

        subscription_item_id = d.pop("subscriptionItemId", UNSET)

        external_billing = d.pop("externalBilling", UNSET)

        tax_state = d.pop("taxState", UNSET)

        purchased_addon_id = d.pop("purchasedAddonId", UNSET)

        _validity_end_date = d.pop("validityEndDate", UNSET)
        validity_end_date: Union[Unset, datetime.datetime]
        if isinstance(_validity_end_date, Unset):
            validity_end_date = UNSET
        else:
            validity_end_date = isoparse(_validity_end_date)

        _voucher_purchase = d.pop("voucherPurchase", UNSET)
        voucher_purchase: Union[Unset, VoucherPurchaseData]
        if isinstance(_voucher_purchase, Unset):
            voucher_purchase = UNSET
        else:
            voucher_purchase = VoucherPurchaseData.from_dict(_voucher_purchase)

        _voucher_usage = d.pop("voucherUsage", UNSET)
        voucher_usage: Union[Unset, VoucherUsageData]
        if isinstance(_voucher_usage, Unset):
            voucher_usage = UNSET
        else:
            voucher_usage = VoucherUsageData.from_dict(_voucher_usage)

        order_item = cls(
            position=position,
            product_id=product_id,
            title=title,
            tax_type=tax_type,
            price=price,
            tax=tax,
            tax_country=tax_country,
            quantity=quantity,
            discount_percentage=discount_percentage,
            delivery_customer_id=delivery_customer_id,
            plenigo_offer_id=plenigo_offer_id,
            plenigo_product_id=plenigo_product_id,
            plenigo_step_id=plenigo_step_id,
            access_right_unique_id=access_right_unique_id,
            internal_title=internal_title,
            cost_center=cost_center,
            voucher_code=voucher_code,
            delivery_address=delivery_address,
            subscription_item_id=subscription_item_id,
            external_billing=external_billing,
            tax_state=tax_state,
            purchased_addon_id=purchased_addon_id,
            validity_end_date=validity_end_date,
            voucher_purchase=voucher_purchase,
            voucher_usage=voucher_usage,
        )

        order_item.additional_properties = d
        return order_item

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
