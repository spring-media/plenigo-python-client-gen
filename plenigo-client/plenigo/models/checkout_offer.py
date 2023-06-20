from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_custom_product import CheckoutCustomProduct


T = TypeVar("T", bound="CheckoutOffer")


@attr.s(auto_attribs=True)
class CheckoutOffer:
    """
    Attributes:
        plenigo_offer_id (str): if the product is based on a plenigo offer the plenigo product id is to provide here
        quantity (int): quantity of purchased entities
        title (str): translated title
        legal_text (str): translated legal text
        summary_text (str): translated summary text
        products (List['CheckoutCustomProduct']): customized products to buy
        plenigo_bonus_ids (Union[Unset, List[str]]): if the offer should contain bonuses the plenigo bonus id can be
            added here
        description (Union[Unset, str]): translated description
        withdrawal_instruction (Union[Unset, str]): translated withdrawal instruction
        logo_url (Union[Unset, str]): url to get image from
        logo_alt_text (Union[Unset, str]): image alt text
    """

    plenigo_offer_id: str
    quantity: int
    title: str
    legal_text: str
    summary_text: str
    products: List["CheckoutCustomProduct"]
    plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    withdrawal_instruction: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    logo_alt_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plenigo_offer_id = self.plenigo_offer_id
        quantity = self.quantity
        title = self.title
        legal_text = self.legal_text
        summary_text = self.summary_text
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()

            products.append(products_item)

        plenigo_bonus_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.plenigo_bonus_ids, Unset):
            plenigo_bonus_ids = self.plenigo_bonus_ids

        description = self.description
        withdrawal_instruction = self.withdrawal_instruction
        logo_url = self.logo_url
        logo_alt_text = self.logo_alt_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plenigoOfferId": plenigo_offer_id,
                "quantity": quantity,
                "title": title,
                "legalText": legal_text,
                "summaryText": summary_text,
                "products": products,
            }
        )
        if plenigo_bonus_ids is not UNSET:
            field_dict["plenigoBonusIds"] = plenigo_bonus_ids
        if description is not UNSET:
            field_dict["description"] = description
        if withdrawal_instruction is not UNSET:
            field_dict["withdrawalInstruction"] = withdrawal_instruction
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if logo_alt_text is not UNSET:
            field_dict["logoAltText"] = logo_alt_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_custom_product import CheckoutCustomProduct

        d = src_dict.copy()
        plenigo_offer_id = d.pop("plenigoOfferId")

        quantity = d.pop("quantity")

        title = d.pop("title")

        legal_text = d.pop("legalText")

        summary_text = d.pop("summaryText")

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = CheckoutCustomProduct.from_dict(products_item_data)

            products.append(products_item)

        plenigo_bonus_ids = cast(List[str], d.pop("plenigoBonusIds", UNSET))

        description = d.pop("description", UNSET)

        withdrawal_instruction = d.pop("withdrawalInstruction", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        logo_alt_text = d.pop("logoAltText", UNSET)

        checkout_offer = cls(
            plenigo_offer_id=plenigo_offer_id,
            quantity=quantity,
            title=title,
            legal_text=legal_text,
            summary_text=summary_text,
            products=products,
            plenigo_bonus_ids=plenigo_bonus_ids,
            description=description,
            withdrawal_instruction=withdrawal_instruction,
            logo_url=logo_url,
            logo_alt_text=logo_alt_text,
        )

        checkout_offer.additional_properties = d
        return checkout_offer

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
