import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShoppingCartItem")


@_attrs_define
class ShoppingCartItem:
    """
    Attributes:
        position (int): item position within the shopping cart or shopping cart group - must start with one and be in
            order
        option (bool): flag indicating if product is an option - can be booked optionally and is not automatically part
            of the checkout
        default_selected (bool): flag indicating if product should be selected by default
        shopping_cart_item_id (int): unique id of the shopping cart item within a contract company
        offer_id (Union[Unset, int]): id of the offer associated with this shopping cart item
        bonus (Union[Unset, int]): id of the bonus associated with this shopping cart item
        connected_offer_id (Union[Unset, int]): id of the connected offer associated with this shopping cart item
        connected_leading_plenigo_offer_id (Union[Unset, str]): unique id of the offer the connected offer is associated
            with
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        plenigo_offer_id (Union[Unset, str]): unique id of the offer within the shopping cart
        plenigo_bonus_id (Union[Unset, str]): unique id of the bonus within the shopping cart
        connected_plenigo_offer_id (Union[Unset, str]): unique id of the connected offer within the shopping cart
        connected_offer_company_id (Union[Unset, str]): companyId of connected company
    """

    position: int
    option: bool
    default_selected: bool
    shopping_cart_item_id: int
    offer_id: Union[Unset, int] = UNSET
    bonus: Union[Unset, int] = UNSET
    connected_offer_id: Union[Unset, int] = UNSET
    connected_leading_plenigo_offer_id: Union[Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    plenigo_bonus_id: Union[Unset, str] = UNSET
    connected_plenigo_offer_id: Union[Unset, str] = UNSET
    connected_offer_company_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        option = self.option

        default_selected = self.default_selected

        shopping_cart_item_id = self.shopping_cart_item_id

        offer_id = self.offer_id

        bonus = self.bonus

        connected_offer_id = self.connected_offer_id

        connected_leading_plenigo_offer_id = self.connected_leading_plenigo_offer_id

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

        plenigo_offer_id = self.plenigo_offer_id

        plenigo_bonus_id = self.plenigo_bonus_id

        connected_plenigo_offer_id = self.connected_plenigo_offer_id

        connected_offer_company_id = self.connected_offer_company_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "option": option,
                "defaultSelected": default_selected,
                "shoppingCartItemId": shopping_cart_item_id,
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if plenigo_bonus_id is not UNSET:
            field_dict["plenigoBonusId"] = plenigo_bonus_id
        if connected_plenigo_offer_id is not UNSET:
            field_dict["connectedPlenigoOfferId"] = connected_plenigo_offer_id
        if connected_offer_company_id is not UNSET:
            field_dict["connectedOfferCompanyId"] = connected_offer_company_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        option = d.pop("option")

        default_selected = d.pop("defaultSelected")

        shopping_cart_item_id = d.pop("shoppingCartItemId")

        offer_id = d.pop("offerId", UNSET)

        bonus = d.pop("bonus", UNSET)

        connected_offer_id = d.pop("connectedOfferId", UNSET)

        connected_leading_plenigo_offer_id = d.pop("connectedLeadingPlenigoOfferId", UNSET)

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
                created_date_type_1 = isoparse(data)

                return created_date_type_1
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
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        plenigo_bonus_id = d.pop("plenigoBonusId", UNSET)

        connected_plenigo_offer_id = d.pop("connectedPlenigoOfferId", UNSET)

        connected_offer_company_id = d.pop("connectedOfferCompanyId", UNSET)

        shopping_cart_item = cls(
            position=position,
            option=option,
            default_selected=default_selected,
            shopping_cart_item_id=shopping_cart_item_id,
            offer_id=offer_id,
            bonus=bonus,
            connected_offer_id=connected_offer_id,
            connected_leading_plenigo_offer_id=connected_leading_plenigo_offer_id,
            created_date=created_date,
            changed_date=changed_date,
            plenigo_offer_id=plenigo_offer_id,
            plenigo_bonus_id=plenigo_bonus_id,
            connected_plenigo_offer_id=connected_plenigo_offer_id,
            connected_offer_company_id=connected_offer_company_id,
        )

        shopping_cart_item.additional_properties = d
        return shopping_cart_item

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
