from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddonTranslationImage")


@attr.s(auto_attribs=True)
class AddonTranslationImage:
    """
    Attributes:
        name (str): description of the image Example: Promotion image.
        addon_translation_image_id (Union[Unset, int]): unique id of the image within the contract company Example:
            100324.
        alt_text (Union[Unset, str]): alt text of the image Example: A very nice promotion.
        image (Union[Unset, None, List[int]]): image as byte array
        meta_data (Union[Unset, Any]): additional meta data
        url (Union[Unset, str]): url to the image Example: https://example.com/test.jpg.
    """

    name: str
    addon_translation_image_id: Union[Unset, int] = UNSET
    alt_text: Union[Unset, str] = UNSET
    image: Union[Unset, None, List[int]] = UNSET
    meta_data: Union[Unset, Any] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        addon_translation_image_id = self.addon_translation_image_id
        alt_text = self.alt_text
        image: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.image, Unset):
            if self.image is None:
                image = None
            else:
                image = self.image

        meta_data = self.meta_data
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if addon_translation_image_id is not UNSET:
            field_dict["addonTranslationImageId"] = addon_translation_image_id
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text
        if image is not UNSET:
            field_dict["image"] = image
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        addon_translation_image_id = d.pop("addonTranslationImageId", UNSET)

        alt_text = d.pop("altText", UNSET)

        image = cast(List[int], d.pop("image", UNSET))

        meta_data = d.pop("metaData", UNSET)

        url = d.pop("url", UNSET)

        addon_translation_image = cls(
            name=name,
            addon_translation_image_id=addon_translation_image_id,
            alt_text=alt_text,
            image=image,
            meta_data=meta_data,
            url=url,
        )

        addon_translation_image.additional_properties = d
        return addon_translation_image

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
