from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate


T = TypeVar("T", bound="ShoppingCartBase")


@_attrs_define
class ShoppingCartBase:
    """
    Attributes:
        internal_title (str): internal title of the shopping cart
        translations (List['ApiBaseDate']): translations associated with this shopping cart
        hint_tm_id (Union[Unset, int]): id of the text module used as hint
    """

    internal_title: str
    translations: List["ApiBaseDate"]
    hint_tm_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        hint_tm_id = self.hint_tm_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
            }
        )
        if hint_tm_id is not UNSET:
            field_dict["hintTmId"] = hint_tm_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ApiBaseDate.from_dict(translations_item_data)

            translations.append(translations_item)

        hint_tm_id = d.pop("hintTmId", UNSET)

        shopping_cart_base = cls(
            internal_title=internal_title,
            translations=translations,
            hint_tm_id=hint_tm_id,
        )

        shopping_cart_base.additional_properties = d
        return shopping_cart_base

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
