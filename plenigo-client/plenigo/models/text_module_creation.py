from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_module_creation_type import TextModuleCreationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_module_translation import TextModuleTranslation


T = TypeVar("T", bound="TextModuleCreation")


@_attrs_define
class TextModuleCreation:
    """
    Attributes:
        internal_title (str): internal title of the text module
        type (TextModuleCreationType): type of text the module represents
        translations (List['TextModuleTranslation']): translations associated with this term
        leaf_id (Union[Unset, int]): id of the tree leaf this price issue should be associated with
    """

    internal_title: str
    type: TextModuleCreationType
    translations: List["TextModuleTranslation"]
    leaf_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        type = self.type.value

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        leaf_id = self.leaf_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "type": type,
                "translations": translations,
            }
        )
        if leaf_id is not UNSET:
            field_dict["leafId"] = leaf_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_module_translation import TextModuleTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        type = TextModuleCreationType(d.pop("type"))

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = TextModuleTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        leaf_id = d.pop("leafId", UNSET)

        text_module_creation = cls(
            internal_title=internal_title,
            type=type,
            translations=translations,
            leaf_id=leaf_id,
        )

        text_module_creation.additional_properties = d
        return text_module_creation

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
