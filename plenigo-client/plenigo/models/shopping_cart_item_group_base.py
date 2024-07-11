from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shopping_cart_translation import ShoppingCartTranslation


T = TypeVar("T", bound="ShoppingCartItemGroupBase")


@_attrs_define
class ShoppingCartItemGroupBase:
    """
    Attributes:
        internal_title (str): internal title of the shopping cart item group
        translations (List['ShoppingCartTranslation']): translations associated with this shopping cart item group
    """

    internal_title: str
    translations: List["ShoppingCartTranslation"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shopping_cart_translation import ShoppingCartTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ShoppingCartTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        shopping_cart_item_group_base = cls(
            internal_title=internal_title,
            translations=translations,
        )

        shopping_cart_item_group_base.additional_properties = d
        return shopping_cart_item_group_base

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
