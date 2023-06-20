from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_translation_image import AddonTranslationImage


T = TypeVar("T", bound="AddonTranslation")


@attr.s(auto_attribs=True)
class AddonTranslation:
    """
    Attributes:
        language (str): language code formatted two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> Example: en.
        title (str): title of the addon Example: Teacup.
        conditions (Union[Unset, str]): condition of the addon Example: You have to be a customer for at least three
            days..
        description (Union[Unset, str]): description of the addon Example: A modern high quality teacup..
        images (Union[Unset, None, List['AddonTranslationImage']]): images that belong to the translation
        preferred (Union[Unset, bool]): flag if the translation is the preferred translation Example: True.
    """

    language: str
    title: str
    conditions: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    images: Union[Unset, None, List["AddonTranslationImage"]] = UNSET
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        title = self.title
        conditions = self.conditions
        description = self.description
        images: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            if self.images is None:
                images = None
            else:
                images = []
                for images_item_data in self.images:
                    images_item = images_item_data.to_dict()

                    images.append(images_item)

        preferred = self.preferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "title": title,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images
        if preferred is not UNSET:
            field_dict["preferred"] = preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addon_translation_image import AddonTranslationImage

        d = src_dict.copy()
        language = d.pop("language")

        title = d.pop("title")

        conditions = d.pop("conditions", UNSET)

        description = d.pop("description", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = AddonTranslationImage.from_dict(images_item_data)

            images.append(images_item)

        preferred = d.pop("preferred", UNSET)

        addon_translation = cls(
            language=language,
            title=title,
            conditions=conditions,
            description=description,
            images=images,
            preferred=preferred,
        )

        addon_translation.additional_properties = d
        return addon_translation

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
