import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_misuse_rule_creation_duration_timespan import ProductMisuseRuleCreationDurationTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate


T = TypeVar("T", bound="ProductMisuseRule")


@_attrs_define
class ProductMisuseRule:
    """
    Attributes:
        internal_title (str): internal title of the misuse rule
        alternative_plenigo_offer_id (str): plenigo offer id of the offer to sell if product is already bought
        misuse_rule_id (int): unique id of the misuse rule within a contract company
        description (Union[Unset, str]): Internal description of the misuse rule
        duration (Union[Unset, int]): time duration the customer must wait to be able to buy the offer again - zero
            means forever
        duration_timespan (Union[Unset, ProductMisuseRuleCreationDurationTimespan]): timespan that the duration is
            related to
        translations (Union[Unset, List['ApiBaseDate']]): translations associated with this misuse rule
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
    """

    internal_title: str
    alternative_plenigo_offer_id: str
    misuse_rule_id: int
    description: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    duration_timespan: Union[Unset, ProductMisuseRuleCreationDurationTimespan] = UNSET
    translations: Union[Unset, List["ApiBaseDate"]] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        alternative_plenigo_offer_id = self.alternative_plenigo_offer_id

        misuse_rule_id = self.misuse_rule_id

        description = self.description

        duration = self.duration

        duration_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.duration_timespan, Unset):
            duration_timespan = self.duration_timespan.value

        translations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "alternativePlenigoOfferId": alternative_plenigo_offer_id,
                "misuseRuleId": misuse_rule_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_timespan is not UNSET:
            field_dict["durationTimespan"] = duration_timespan
        if translations is not UNSET:
            field_dict["translations"] = translations
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        alternative_plenigo_offer_id = d.pop("alternativePlenigoOfferId")

        misuse_rule_id = d.pop("misuseRuleId")

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        _duration_timespan = d.pop("durationTimespan", UNSET)
        duration_timespan: Union[Unset, ProductMisuseRuleCreationDurationTimespan]
        if isinstance(_duration_timespan, Unset) or not _duration_timespan:
            duration_timespan = UNSET
        else:
            duration_timespan = ProductMisuseRuleCreationDurationTimespan(_duration_timespan)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = ApiBaseDate.from_dict(translations_item_data)

            translations.append(translations_item)

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
                created_date_type_1 = isoparse(data)

                return created_date_type_1
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
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        product_misuse_rule = cls(
            internal_title=internal_title,
            alternative_plenigo_offer_id=alternative_plenigo_offer_id,
            misuse_rule_id=misuse_rule_id,
            description=description,
            duration=duration,
            duration_timespan=duration_timespan,
            translations=translations,
            created_date=created_date,
            changed_date=changed_date,
        )

        product_misuse_rule.additional_properties = d
        return product_misuse_rule

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
