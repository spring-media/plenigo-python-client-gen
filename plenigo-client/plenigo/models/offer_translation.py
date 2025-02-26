import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_translation_image import OfferTranslationImage


T = TypeVar("T", bound="OfferTranslation")


@_attrs_define
class OfferTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        title (str): translated title
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        title_additions (Union[Unset, str]): translated additional title information
        description (Union[Unset, str]): translated description
        legal_text (Union[Unset, str]): translated legal text
        summary_text (Union[Unset, str]): translated summary text
        withdrawal_instruction (Union[Unset, str]): translated withdrawal instruction
        preferred (Union[Unset, bool]): flag indicating if language is default fallback language if no suitable language
            is found
        images (Union[Unset, list['OfferTranslationImage']]): images associated with translation
    """

    language: str
    title: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    title_additions: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    legal_text: Union[Unset, str] = UNSET
    summary_text: Union[Unset, str] = UNSET
    withdrawal_instruction: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    images: Union[Unset, list["OfferTranslationImage"]] = UNSET
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

        title_additions = self.title_additions

        description = self.description

        legal_text = self.legal_text

        summary_text = self.summary_text

        withdrawal_instruction = self.withdrawal_instruction

        preferred = self.preferred

        images: Union[Unset, list[dict[str, Any]]] = UNSET
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if title_additions is not UNSET:
            field_dict["titleAdditions"] = title_additions
        if description is not UNSET:
            field_dict["description"] = description
        if legal_text is not UNSET:
            field_dict["legalText"] = legal_text
        if summary_text is not UNSET:
            field_dict["summaryText"] = summary_text
        if withdrawal_instruction is not UNSET:
            field_dict["withdrawalInstruction"] = withdrawal_instruction
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_translation_image import OfferTranslationImage

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

        title_additions = d.pop("titleAdditions", UNSET)

        description = d.pop("description", UNSET)

        legal_text = d.pop("legalText", UNSET)

        summary_text = d.pop("summaryText", UNSET)

        withdrawal_instruction = d.pop("withdrawalInstruction", UNSET)

        preferred = d.pop("preferred", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = OfferTranslationImage.from_dict(images_item_data)

            images.append(images_item)

        offer_translation = cls(
            language=language,
            title=title,
            created_date=created_date,
            changed_date=changed_date,
            title_additions=title_additions,
            description=description,
            legal_text=legal_text,
            summary_text=summary_text,
            withdrawal_instruction=withdrawal_instruction,
            preferred=preferred,
            images=images,
        )

        offer_translation.additional_properties = d
        return offer_translation

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
