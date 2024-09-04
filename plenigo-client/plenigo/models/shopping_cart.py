import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shopping_cart_item import ShoppingCartItem
    from ..models.shopping_cart_item_group import ShoppingCartItemGroup
    from ..models.shopping_cart_translation import ShoppingCartTranslation


T = TypeVar("T", bound="ShoppingCart")


@_attrs_define
class ShoppingCart:
    """
    Attributes:
        internal_title (str): internal title of the shopping cart
        translations (List['ShoppingCartTranslation']): translations associated with this shopping cart
        shopping_cart_id (int): unique id of the shopping cart within a contract company
        plenigo_shopping_cart_id (str): unique id of the shopping cart within a company
        hint_tm_id (Union[Unset, int]): id of the text module used as hint
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        items (Union[Unset, List['ShoppingCartItem']]): items associated with this shopping cart
        item_groups (Union[Unset, List['ShoppingCartItemGroup']]): item groups associated with this shopping cart
    """

    internal_title: str
    translations: List["ShoppingCartTranslation"]
    shopping_cart_id: int
    plenigo_shopping_cart_id: str
    hint_tm_id: Union[Unset, int] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    items: Union[Unset, List["ShoppingCartItem"]] = UNSET
    item_groups: Union[Unset, List["ShoppingCartItemGroup"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        shopping_cart_id = self.shopping_cart_id

        plenigo_shopping_cart_id = self.plenigo_shopping_cart_id

        hint_tm_id = self.hint_tm_id

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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        item_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_groups, Unset):
            item_groups = []
            for item_groups_item_data in self.item_groups:
                item_groups_item = item_groups_item_data.to_dict()
                item_groups.append(item_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
                "shoppingCartId": shopping_cart_id,
                "plenigoShoppingCartId": plenigo_shopping_cart_id,
            }
        )
        if hint_tm_id is not UNSET:
            field_dict["hintTmId"] = hint_tm_id
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
        if items is not UNSET:
            field_dict["items"] = items
        if item_groups is not UNSET:
            field_dict["itemGroups"] = item_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shopping_cart_item import ShoppingCartItem
        from ..models.shopping_cart_item_group import ShoppingCartItemGroup
        from ..models.shopping_cart_translation import ShoppingCartTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ShoppingCartTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        shopping_cart_id = d.pop("shoppingCartId")

        plenigo_shopping_cart_id = d.pop("plenigoShoppingCartId")

        hint_tm_id = d.pop("hintTmId", UNSET)

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
                created_date_type_0 = isoparse(data)

                return created_date_type_0
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

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ShoppingCartItem.from_dict(items_item_data)

            items.append(items_item)

        item_groups = []
        _item_groups = d.pop("itemGroups", UNSET)
        for item_groups_item_data in _item_groups or []:
            item_groups_item = ShoppingCartItemGroup.from_dict(item_groups_item_data)

            item_groups.append(item_groups_item)

        shopping_cart = cls(
            internal_title=internal_title,
            translations=translations,
            shopping_cart_id=shopping_cart_id,
            plenigo_shopping_cart_id=plenigo_shopping_cart_id,
            hint_tm_id=hint_tm_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            items=items,
            item_groups=item_groups,
        )

        shopping_cart.additional_properties = d
        return shopping_cart

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
