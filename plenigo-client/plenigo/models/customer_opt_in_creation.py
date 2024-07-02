from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_opt_in_creation_included_types_item import CustomerOptInCreationIncludedTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_opt_in_translation_base import CustomerOptInTranslationBase


T = TypeVar("T", bound="CustomerOptInCreation")


@_attrs_define
class CustomerOptInCreation:
    """
    Attributes:
        internal_title (str): internal title of the opt in
        unique_id (str): unique id to associate with the user after user has accepted opt in
        included_types (List[CustomerOptInCreationIncludedTypesItem]): types that are included with this opt-in
        translations (List['CustomerOptInTranslationBase']): translations associated with this opt in
        active (Union[Unset, bool]): flag indicating if opt in is currently active
    """

    internal_title: str
    unique_id: str
    included_types: List[CustomerOptInCreationIncludedTypesItem]
    translations: List["CustomerOptInTranslationBase"]
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        unique_id = self.unique_id

        included_types = []
        for included_types_item_data in self.included_types:
            included_types_item = included_types_item_data.value
            included_types.append(included_types_item)

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
                "includedTypes": included_types,
                "translations": translations,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_opt_in_translation_base import CustomerOptInTranslationBase

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        unique_id = d.pop("uniqueId")

        included_types = []
        _included_types = d.pop("includedTypes")
        for included_types_item_data in _included_types:
            included_types_item = CustomerOptInCreationIncludedTypesItem(included_types_item_data)

            included_types.append(included_types_item)

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CustomerOptInTranslationBase.from_dict(translations_item_data)

            translations.append(translations_item)

        active = d.pop("active", UNSET)

        customer_opt_in_creation = cls(
            internal_title=internal_title,
            unique_id=unique_id,
            included_types=included_types,
            translations=translations,
            active=active,
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
