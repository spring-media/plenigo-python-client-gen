from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.age_rule_creation_relational_operator import AgeRuleCreationRelationalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_translation import RuleTranslation


T = TypeVar("T", bound="AgeRuleCreation")


@attr.s(auto_attribs=True)
class AgeRuleCreation:
    """
    Attributes:
        internal_title (Union[Unset, str]): internal title of the age rule
        description (Union[Unset, str]): internal description of the age rule
        relational_operator (Union[Unset, AgeRuleCreationRelationalOperator]): relational operator to use
        age (Union[Unset, int]): age the rule relies on
        protected_plenigo_offer_id (Union[Unset, str]): plenigo offer id that is protected by the age rule
        follow_up_plenigo_offer_id (Union[Unset, str]): optional follow up plenigo offer id to change subscriptions to
            if age rule is no longer fulfilled
        replacement_plenigo_offer_id (Union[Unset, str]): plenigo offer id that is used if rule is not fulfilled
        stop_on_fail (Union[Unset, bool]): flag indicating if age verification is a must have
        translations (Union[Unset, List['RuleTranslation']]): translations for customer texts
    """

    internal_title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    relational_operator: Union[Unset, AgeRuleCreationRelationalOperator] = UNSET
    age: Union[Unset, int] = UNSET
    protected_plenigo_offer_id: Union[Unset, str] = UNSET
    follow_up_plenigo_offer_id: Union[Unset, str] = UNSET
    replacement_plenigo_offer_id: Union[Unset, str] = UNSET
    stop_on_fail: Union[Unset, bool] = UNSET
    translations: Union[Unset, List["RuleTranslation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        description = self.description
        relational_operator: Union[Unset, str] = UNSET
        if not isinstance(self.relational_operator, Unset):
            relational_operator = self.relational_operator.value

        age = self.age
        protected_plenigo_offer_id = self.protected_plenigo_offer_id
        follow_up_plenigo_offer_id = self.follow_up_plenigo_offer_id
        replacement_plenigo_offer_id = self.replacement_plenigo_offer_id
        stop_on_fail = self.stop_on_fail
        translations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()

                translations.append(translations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if description is not UNSET:
            field_dict["description"] = description
        if relational_operator is not UNSET:
            field_dict["relationalOperator"] = relational_operator
        if age is not UNSET:
            field_dict["age"] = age
        if protected_plenigo_offer_id is not UNSET:
            field_dict["protectedPlenigoOfferId"] = protected_plenigo_offer_id
        if follow_up_plenigo_offer_id is not UNSET:
            field_dict["followUpPlenigoOfferId"] = follow_up_plenigo_offer_id
        if replacement_plenigo_offer_id is not UNSET:
            field_dict["replacementPlenigoOfferId"] = replacement_plenigo_offer_id
        if stop_on_fail is not UNSET:
            field_dict["stopOnFail"] = stop_on_fail
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rule_translation import RuleTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle", UNSET)

        description = d.pop("description", UNSET)

        _relational_operator = d.pop("relationalOperator", UNSET)
        relational_operator: Union[Unset, AgeRuleCreationRelationalOperator]
        if isinstance(_relational_operator, Unset):
            relational_operator = UNSET
        else:
            relational_operator = AgeRuleCreationRelationalOperator(_relational_operator)

        age = d.pop("age", UNSET)

        protected_plenigo_offer_id = d.pop("protectedPlenigoOfferId", UNSET)

        follow_up_plenigo_offer_id = d.pop("followUpPlenigoOfferId", UNSET)

        replacement_plenigo_offer_id = d.pop("replacementPlenigoOfferId", UNSET)

        stop_on_fail = d.pop("stopOnFail", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = RuleTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        age_rule_creation = cls(
            internal_title=internal_title,
            description=description,
            relational_operator=relational_operator,
            age=age,
            protected_plenigo_offer_id=protected_plenigo_offer_id,
            follow_up_plenigo_offer_id=follow_up_plenigo_offer_id,
            replacement_plenigo_offer_id=replacement_plenigo_offer_id,
            stop_on_fail=stop_on_fail,
            translations=translations,
        )

        age_rule_creation.additional_properties = d
        return age_rule_creation

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
