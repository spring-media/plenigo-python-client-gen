from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.offer_translation import OfferTranslation


T = TypeVar("T", bound="OfferProductGroupBase")


@attr.s(auto_attribs=True)
class OfferProductGroupBase:
    """
    Attributes:
        internal_title (str): internal title of the product group
        translations (List['OfferTranslation']): translations associated with this product
    """

    internal_title: str
    translations: List["OfferTranslation"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.offer_translation import OfferTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        offer_product_group_base = cls(
            internal_title=internal_title,
            translations=translations,
        )

        offer_product_group_base.additional_properties = d
        return offer_product_group_base

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
