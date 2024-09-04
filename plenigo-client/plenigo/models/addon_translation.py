import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_translation_image import AddonTranslationImage


T = TypeVar("T", bound="AddonTranslation")


@_attrs_define
class AddonTranslation:
    """
    Attributes:
        language (str): language code formatted two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> Example: en.
        title (str): title of the addon Example: Teacup.
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        conditions (Union[Unset, str]): condition of the addon Example: You have to be a customer for at least three
            days..
        description (Union[Unset, str]): description of the addon Example: A modern high quality teacup..
        images (Union[Unset, List['AddonTranslationImage']]): images that belong to the translation
        preferred (Union[Unset, bool]): flag if the translation is the preferred translation Example: True.
    """

    language: str
    title: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    conditions: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    images: Union[Unset, List["AddonTranslationImage"]] = UNSET
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language

        title = self.title

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        conditions = self.conditions

        description = self.description

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
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

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

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
            created_date=created_date,
            changed_date=changed_date,
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
