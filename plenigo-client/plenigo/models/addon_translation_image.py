import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddonTranslationImage")


@_attrs_define
class AddonTranslationImage:
    """
    Attributes:
        name (str): description of the image Example: Promotion image.
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        addon_translation_image_id (Union[Unset, int]): unique id of the image within the contract company Example:
            100324.
        alt_text (Union[Unset, str]): alt text of the image Example: A very nice promotion.
        image (Union[Unset, List[int]]): image as byte array
        meta_data (Union[Unset, Any]): additional meta data
        url (Union[Unset, str]): url to the image Example: https://example.com/test.jpg.
    """

    name: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    addon_translation_image_id: Union[Unset, int] = UNSET
    alt_text: Union[Unset, str] = UNSET
    image: Union[Unset, List[int]] = UNSET
    meta_data: Union[Unset, Any] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        addon_translation_image_id = self.addon_translation_image_id

        alt_text = self.alt_text

        image: Union[Unset, List[int]] = UNSET
        if not isinstance(self.image, Unset):
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        addon_translation_image_id = d.pop("addonTranslationImageId", UNSET)

        alt_text = d.pop("altText", UNSET)

        image = cast(List[int], d.pop("image", UNSET))

        meta_data = d.pop("metaData", UNSET)

        url = d.pop("url", UNSET)

        addon_translation_image = cls(
            name=name,
            created_date=created_date,
            changed_date=changed_date,
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
