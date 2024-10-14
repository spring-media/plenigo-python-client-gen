import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.age_rule_creation_relational_operator import AgeRuleCreationRelationalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate


T = TypeVar("T", bound="AgeRule")


@_attrs_define
class AgeRule:
    """
    Attributes:
        internal_title (str): internal title of the age rule
        relational_operator (AgeRuleCreationRelationalOperator): relational operator to use
        age (int): age the rule relies on
        protected_plenigo_offer_id (str): plenigo offer id that is protected by the age rule
        description (Union[Unset, str]): internal description of the age rule
        follow_up_plenigo_offer_id (Union[Unset, str]): optional follow up plenigo offer id to change subscriptions to
            if age rule is no longer fulfilled
        replacement_plenigo_offer_id (Union[Unset, str]): plenigo offer id that is used if rule is not fulfilled
        stop_on_fail (Union[Unset, bool]): flag indicating if age verification is a must have
        translations (Union[Unset, List['ApiBaseDate']]): translations for customer texts
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        age_rule_id (Union[Unset, int]): unique id of the age rule within a contract company
    """

    internal_title: str
    relational_operator: AgeRuleCreationRelationalOperator
    age: int
    protected_plenigo_offer_id: str
    description: Union[Unset, str] = UNSET
    follow_up_plenigo_offer_id: Union[Unset, str] = UNSET
    replacement_plenigo_offer_id: Union[Unset, str] = UNSET
    stop_on_fail: Union[Unset, bool] = UNSET
    translations: Union[Unset, List["ApiBaseDate"]] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    age_rule_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        relational_operator = self.relational_operator.value

        age = self.age

        protected_plenigo_offer_id = self.protected_plenigo_offer_id

        description = self.description

        follow_up_plenigo_offer_id = self.follow_up_plenigo_offer_id

        replacement_plenigo_offer_id = self.replacement_plenigo_offer_id

        stop_on_fail = self.stop_on_fail

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

        age_rule_id = self.age_rule_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "relationalOperator": relational_operator,
                "age": age,
                "protectedPlenigoOfferId": protected_plenigo_offer_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if follow_up_plenigo_offer_id is not UNSET:
            field_dict["followUpPlenigoOfferId"] = follow_up_plenigo_offer_id
        if replacement_plenigo_offer_id is not UNSET:
            field_dict["replacementPlenigoOfferId"] = replacement_plenigo_offer_id
        if stop_on_fail is not UNSET:
            field_dict["stopOnFail"] = stop_on_fail
        if translations is not UNSET:
            field_dict["translations"] = translations
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if age_rule_id is not UNSET:
            field_dict["ageRuleId"] = age_rule_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        relational_operator = AgeRuleCreationRelationalOperator(d.pop("relationalOperator"))

        age = d.pop("age")

        protected_plenigo_offer_id = d.pop("protectedPlenigoOfferId")

        description = d.pop("description", UNSET)

        follow_up_plenigo_offer_id = d.pop("followUpPlenigoOfferId", UNSET)

        replacement_plenigo_offer_id = d.pop("replacementPlenigoOfferId", UNSET)

        stop_on_fail = d.pop("stopOnFail", UNSET)

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

        age_rule_id = d.pop("ageRuleId", UNSET)

        age_rule = cls(
            internal_title=internal_title,
            relational_operator=relational_operator,
            age=age,
            protected_plenigo_offer_id=protected_plenigo_offer_id,
            description=description,
            follow_up_plenigo_offer_id=follow_up_plenigo_offer_id,
            replacement_plenigo_offer_id=replacement_plenigo_offer_id,
            stop_on_fail=stop_on_fail,
            translations=translations,
            created_date=created_date,
            changed_date=changed_date,
            age_rule_id=age_rule_id,
        )

        age_rule.additional_properties = d
        return age_rule

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
