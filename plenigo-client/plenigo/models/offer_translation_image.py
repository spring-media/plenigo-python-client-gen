from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_translation_image_image_type import OfferTranslationImageImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferTranslationImage")


@attr.s(auto_attribs=True)
class OfferTranslationImage:
    """
    Attributes:
        image_type (OfferTranslationImageImageType): type of the image - there can only be one image of each type per
            translation
        name (str): name of the image
        url (str): url to get image from
        alt_text (Union[Unset, str]): image alt text
    """

    image_type: OfferTranslationImageImageType
    name: str
    url: str
    alt_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_type = self.image_type.value

        name = self.name
        url = self.url
        alt_text = self.alt_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "imageType": image_type,
                "name": name,
                "url": url,
            }
        )
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_type = OfferTranslationImageImageType(d.pop("imageType"))

        name = d.pop("name")

        url = d.pop("url")

        alt_text = d.pop("altText", UNSET)

        offer_translation_image = cls(
            image_type=image_type,
            name=name,
            url=url,
            alt_text=alt_text,
        )

        offer_translation_image.additional_properties = d
        return offer_translation_image

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
