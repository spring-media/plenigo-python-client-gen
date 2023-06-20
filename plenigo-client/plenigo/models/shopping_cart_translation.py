from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shopping_cart_translation_image import ShoppingCartTranslationImage


T = TypeVar("T", bound="ShoppingCartTranslation")


@attr.s(auto_attribs=True)
class ShoppingCartTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        title (str): translated title
        description (Union[Unset, str]): translated description
        legal_text (Union[Unset, str]): translated legal text
        preferred (Union[Unset, bool]): flag indicating if language is default fallback language if no suitable language
            is found
        images (Union[Unset, List['ShoppingCartTranslationImage']]): images associated with translation
    """

    language: str
    title: str
    description: Union[Unset, str] = UNSET
    legal_text: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    images: Union[Unset, List["ShoppingCartTranslationImage"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        title = self.title
        description = self.description
        legal_text = self.legal_text
        preferred = self.preferred
        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()

                images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if legal_text is not UNSET:
            field_dict["legalText"] = legal_text
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shopping_cart_translation_image import ShoppingCartTranslationImage

        d = src_dict.copy()
        language = d.pop("language")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        legal_text = d.pop("legalText", UNSET)

        preferred = d.pop("preferred", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ShoppingCartTranslationImage.from_dict(images_item_data)

            images.append(images_item)

        shopping_cart_translation = cls(
            language=language,
            title=title,
            description=description,
            legal_text=legal_text,
            preferred=preferred,
            images=images,
        )

        shopping_cart_translation.additional_properties = d
        return shopping_cart_translation

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
