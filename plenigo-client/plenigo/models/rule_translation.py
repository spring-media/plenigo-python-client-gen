from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleTranslation")


@attr.s(auto_attribs=True)
class RuleTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        title (str): translated title
        pre_description (Union[Unset, str]): text to show to the customer before rule starts
        success_description (Union[Unset, str]): text to show to the customer if rule was successful
        failure_description (Union[Unset, str]): text to show to the customer if rule failed
        preferred (Union[Unset, bool]): flag indicating if language is default fallback language if no suitable language
            is found
    """

    language: str
    title: str
    pre_description: Union[Unset, str] = UNSET
    success_description: Union[Unset, str] = UNSET
    failure_description: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        title = self.title
        pre_description = self.pre_description
        success_description = self.success_description
        failure_description = self.failure_description
        preferred = self.preferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "title": title,
            }
        )
        if pre_description is not UNSET:
            field_dict["preDescription"] = pre_description
        if success_description is not UNSET:
            field_dict["successDescription"] = success_description
        if failure_description is not UNSET:
            field_dict["failureDescription"] = failure_description
        if preferred is not UNSET:
            field_dict["preferred"] = preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        title = d.pop("title")

        pre_description = d.pop("preDescription", UNSET)

        success_description = d.pop("successDescription", UNSET)

        failure_description = d.pop("failureDescription", UNSET)

        preferred = d.pop("preferred", UNSET)

        rule_translation = cls(
            language=language,
            title=title,
            pre_description=pre_description,
            success_description=success_description,
            failure_description=failure_description,
            preferred=preferred,
        )

        rule_translation.additional_properties = d
        return rule_translation

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
