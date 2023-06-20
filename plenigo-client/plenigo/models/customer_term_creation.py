from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_term_translation import CustomerTermTranslation


T = TypeVar("T", bound="CustomerTermCreation")


@attr.s(auto_attribs=True)
class CustomerTermCreation:
    """
    Attributes:
        internal_title (str): internal title of the term
        unique_id (str): unique id to associate with the user after user has accepted term
        translations (List['CustomerTermTranslation']): translations associated with this term
        active (Union[Unset, bool]): flag indicating if term is currently active
    """

    internal_title: str
    unique_id: str
    translations: List["CustomerTermTranslation"]
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        unique_id = self.unique_id
        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()

            translations.append(translations_item)

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "uniqueId": unique_id,
                "translations": translations,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_term_translation import CustomerTermTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        unique_id = d.pop("uniqueId")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CustomerTermTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        active = d.pop("active", UNSET)

        customer_term_creation = cls(
            internal_title=internal_title,
            unique_id=unique_id,
            translations=translations,
            active=active,
        )

        customer_term_creation.additional_properties = d
        return customer_term_creation

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
