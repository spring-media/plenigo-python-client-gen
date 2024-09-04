import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleTranslation")


@_attrs_define
class RuleTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        title (str): translated title
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        pre_description (Union[Unset, str]): text to show to the customer before rule starts
        success_description (Union[Unset, str]): text to show to the customer if rule was successful
        failure_description (Union[Unset, str]): text to show to the customer if rule failed
        preferred (Union[Unset, bool]): flag indicating if language is default fallback language if no suitable language
            is found
    """

    language: str
    title: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    pre_description: Union[Unset, str] = UNSET
    success_description: Union[Unset, str] = UNSET
    failure_description: Union[Unset, str] = UNSET
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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

        pre_description = d.pop("preDescription", UNSET)

        success_description = d.pop("successDescription", UNSET)

        failure_description = d.pop("failureDescription", UNSET)

        preferred = d.pop("preferred", UNSET)

        rule_translation = cls(
            language=language,
            title=title,
            created_date=created_date,
            changed_date=changed_date,
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
