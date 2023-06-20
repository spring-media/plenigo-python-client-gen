from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_opt_in_creation_included_types_item import CustomerOptInCreationIncludedTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_opt_in_translation import CustomerOptInTranslation


T = TypeVar("T", bound="CustomerOptInCreation")


@attr.s(auto_attribs=True)
class CustomerOptInCreation:
    """
    Attributes:
        internal_title (str): internal title of the opt in
        unique_id (str): unique id to associate with the user after user has accepted opt in
        translations (List['CustomerOptInTranslation']): translations associated with this opt in
        active (Union[Unset, bool]): flag indicating if opt in is currently active
        included_types (Union[Unset, List[CustomerOptInCreationIncludedTypesItem]]): types that are included with this
            opt-in
    """

    internal_title: str
    unique_id: str
    translations: List["CustomerOptInTranslation"]
    active: Union[Unset, bool] = UNSET
    included_types: Union[Unset, List[CustomerOptInCreationIncludedTypesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        unique_id = self.unique_id
        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()

            translations.append(translations_item)

        active = self.active
        included_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.included_types, Unset):
            included_types = []
            for included_types_item_data in self.included_types:
                included_types_item = included_types_item_data.value

                included_types.append(included_types_item)

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
        if included_types is not UNSET:
            field_dict["includedTypes"] = included_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_opt_in_translation import CustomerOptInTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        unique_id = d.pop("uniqueId")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CustomerOptInTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        active = d.pop("active", UNSET)

        included_types = []
        _included_types = d.pop("includedTypes", UNSET)
        for included_types_item_data in _included_types or []:
            included_types_item = CustomerOptInCreationIncludedTypesItem(included_types_item_data)

            included_types.append(included_types_item)

        customer_opt_in_creation = cls(
            internal_title=internal_title,
            unique_id=unique_id,
            translations=translations,
            active=active,
            included_types=included_types,
        )

        customer_opt_in_creation.additional_properties = d
        return customer_opt_in_creation

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
