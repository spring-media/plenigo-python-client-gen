from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.checkout_custom_product_tax_type import CheckoutCustomProductTaxType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutCustomProduct")


@attr.s(auto_attribs=True)
class CheckoutCustomProduct:
    """
    Attributes:
        title (str): translated title
        quantity (int): quantity of purchased entities
        price (float): price of the product
        currency (str): currency of the order formatted as <a href='https://en.wikipedia.org/wiki/ISO_4217'
            target='_blank'>ISO 4217, alphabetic code</a>
        tax_type (CheckoutCustomProductTaxType):
        access_right_unique_id (str): unique id of the access right this order item grants access to
        plenigo_product_id (Union[Unset, str]): id of the plenigo product to buy
        product_id (Union[Unset, str]): external id of the product to buy
        description (Union[Unset, str]): translated description
        legal_text (Union[Unset, str]): translated legal text
        summary_text (Union[Unset, str]): translated summary text
        withdrawal_instruction (Union[Unset, str]): translated withdrawal instruction
        logo_url (Union[Unset, str]): url to get image from
        logo_alt_text (Union[Unset, str]): image alt text
        cost_center (Union[Unset, str]): cost center associated with this product at the time of checkout
        discount_percentage (Union[Unset, int]): discount offered to the order
    """

    title: str
    quantity: int
    price: float
    currency: str
    tax_type: CheckoutCustomProductTaxType
    access_right_unique_id: str
    plenigo_product_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    legal_text: Union[Unset, str] = UNSET
    summary_text: Union[Unset, str] = UNSET
    withdrawal_instruction: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    logo_alt_text: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        quantity = self.quantity
        price = self.price
        currency = self.currency
        tax_type = self.tax_type.value

        access_right_unique_id = self.access_right_unique_id
        plenigo_product_id = self.plenigo_product_id
        product_id = self.product_id
        description = self.description
        legal_text = self.legal_text
        summary_text = self.summary_text
        withdrawal_instruction = self.withdrawal_instruction
        logo_url = self.logo_url
        logo_alt_text = self.logo_alt_text
        cost_center = self.cost_center
        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "quantity": quantity,
                "price": price,
                "currency": currency,
                "taxType": tax_type,
                "accessRightUniqueId": access_right_unique_id,
            }
        )
        if plenigo_product_id is not UNSET:
            field_dict["plenigoProductId"] = plenigo_product_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if description is not UNSET:
            field_dict["description"] = description
        if legal_text is not UNSET:
            field_dict["legalText"] = legal_text
        if summary_text is not UNSET:
            field_dict["summaryText"] = summary_text
        if withdrawal_instruction is not UNSET:
            field_dict["withdrawalInstruction"] = withdrawal_instruction
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if logo_alt_text is not UNSET:
            field_dict["logoAltText"] = logo_alt_text
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        quantity = d.pop("quantity")

        price = d.pop("price")

        currency = d.pop("currency")

        tax_type = CheckoutCustomProductTaxType(d.pop("taxType"))

        access_right_unique_id = d.pop("accessRightUniqueId")

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        product_id = d.pop("productId", UNSET)

        description = d.pop("description", UNSET)

        legal_text = d.pop("legalText", UNSET)

        summary_text = d.pop("summaryText", UNSET)

        withdrawal_instruction = d.pop("withdrawalInstruction", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        logo_alt_text = d.pop("logoAltText", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        checkout_custom_product = cls(
            title=title,
            quantity=quantity,
            price=price,
            currency=currency,
            tax_type=tax_type,
            access_right_unique_id=access_right_unique_id,
            plenigo_product_id=plenigo_product_id,
            product_id=product_id,
            description=description,
            legal_text=legal_text,
            summary_text=summary_text,
            withdrawal_instruction=withdrawal_instruction,
            logo_url=logo_url,
            logo_alt_text=logo_alt_text,
            cost_center=cost_center,
            discount_percentage=discount_percentage,
        )

        checkout_custom_product.additional_properties = d
        return checkout_custom_product

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
