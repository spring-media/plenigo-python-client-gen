from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossSellingTranslation")


@attr.s(auto_attribs=True)
class CrossSellingTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        title (str): translated title
        description (Union[Unset, str]): translated description
        submit_text (Union[Unset, str]): text shown on submit page
        preferred (Union[Unset, bool]): flag indicating if language is default fallback language if no suitable language
            is found
    """

    language: str
    title: str
    description: Union[Unset, str] = UNSET
    submit_text: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        title = self.title
        description = self.description
        submit_text = self.submit_text
        preferred = self.preferred

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
        if submit_text is not UNSET:
            field_dict["submitText"] = submit_text
        if preferred is not UNSET:
            field_dict["preferred"] = preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        submit_text = d.pop("submitText", UNSET)

        preferred = d.pop("preferred", UNSET)

        cross_selling_translation = cls(
            language=language,
            title=title,
            description=description,
            submit_text=submit_text,
            preferred=preferred,
        )

        cross_selling_translation.additional_properties = d
        return cross_selling_translation

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
