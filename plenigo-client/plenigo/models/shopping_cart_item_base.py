from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShoppingCartItemBase")


@_attrs_define
class ShoppingCartItemBase:
    """
    Attributes:
        position (int): item position within the shopping cart or shopping cart group - must start with one and be in
            order
        option (bool): flag indicating if product is an option - can be booked optionally and is not automatically part
            of the checkout
        default_selected (bool): flag indicating if product should be selected by default
        offer_id (Union[Unset, int]): id of the offer associated with this shopping cart item
        bonus (Union[Unset, int]): id of the bonus associated with this shopping cart item
        connected_offer_id (Union[Unset, int]): id of the connected offer associated with this shopping cart item
        connected_leading_plenigo_offer_id (Union[Unset, str]): unique id of the offer the connected offer is associated
            with
    """

    position: int
    option: bool
    default_selected: bool
    offer_id: Union[Unset, int] = UNSET
    bonus: Union[Unset, int] = UNSET
    connected_offer_id: Union[Unset, int] = UNSET
    connected_leading_plenigo_offer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        option = self.option

        default_selected = self.default_selected

        offer_id = self.offer_id

        bonus = self.bonus

        connected_offer_id = self.connected_offer_id

        connected_leading_plenigo_offer_id = self.connected_leading_plenigo_offer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "option": option,
                "defaultSelected": default_selected,
            }
        )
        if offer_id is not UNSET:
            field_dict["offerId"] = offer_id
        if bonus is not UNSET:
            field_dict["bonus"] = bonus
        if connected_offer_id is not UNSET:
            field_dict["connectedOfferId"] = connected_offer_id
        if connected_leading_plenigo_offer_id is not UNSET:
            field_dict["connectedLeadingPlenigoOfferId"] = connected_leading_plenigo_offer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        option = d.pop("option")

        default_selected = d.pop("defaultSelected")

        offer_id = d.pop("offerId", UNSET)

        bonus = d.pop("bonus", UNSET)

        connected_offer_id = d.pop("connectedOfferId", UNSET)

        connected_leading_plenigo_offer_id = d.pop("connectedLeadingPlenigoOfferId", UNSET)

        shopping_cart_item_base = cls(
            position=position,
            option=option,
            default_selected=default_selected,
            offer_id=offer_id,
            bonus=bonus,
            connected_offer_id=connected_offer_id,
            connected_leading_plenigo_offer_id=connected_leading_plenigo_offer_id,
        )

        shopping_cart_item_base.additional_properties = d
        return shopping_cart_item_base

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
