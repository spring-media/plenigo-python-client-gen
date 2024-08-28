from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_rule_base_identity_check_type import RelationRuleBaseIdentityCheckType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_translation import RuleTranslation


T = TypeVar("T", bound="RelationRuleBase")


@_attrs_define
class RelationRuleBase:
    """
    Attributes:
        internal_title (Union[Unset, str]): internal title of the relation rule
        description (Union[Unset, str]): internal description of the relation rule
        related_plenigo_offer_id (Union[Unset, str]): plenigo offer id that is used if relation rule matches
        unrelated_plenigo_offer_id (Union[Unset, str]): plenigo offer id that is used if relation rule does not matches
        cancel_unrelated (Union[Unset, bool]): offer is cancelled if relation rule is not matched
        send_customer_email (Union[Unset, bool]): flag indicating if customer email should be sent in case of a
            cancellation
        identity_check_type (Union[Unset, RelationRuleBaseIdentityCheckType]): identity check type to use
        translations (Union[Unset, List['RuleTranslation']]): translations for customer texts
    """

    internal_title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    related_plenigo_offer_id: Union[Unset, str] = UNSET
    unrelated_plenigo_offer_id: Union[Unset, str] = UNSET
    cancel_unrelated: Union[Unset, bool] = UNSET
    send_customer_email: Union[Unset, bool] = UNSET
    identity_check_type: Union[Unset, RelationRuleBaseIdentityCheckType] = UNSET
    translations: Union[Unset, List["RuleTranslation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        description = self.description

        related_plenigo_offer_id = self.related_plenigo_offer_id

        unrelated_plenigo_offer_id = self.unrelated_plenigo_offer_id

        cancel_unrelated = self.cancel_unrelated

        send_customer_email = self.send_customer_email

        identity_check_type: Union[Unset, str] = UNSET
        if not isinstance(self.identity_check_type, Unset):
            identity_check_type = self.identity_check_type.value

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
        if related_plenigo_offer_id is not UNSET:
            field_dict["relatedPlenigoOfferId"] = related_plenigo_offer_id
        if unrelated_plenigo_offer_id is not UNSET:
            field_dict["unrelatedPlenigoOfferId"] = unrelated_plenigo_offer_id
        if cancel_unrelated is not UNSET:
            field_dict["cancelUnrelated"] = cancel_unrelated
        if send_customer_email is not UNSET:
            field_dict["sendCustomerEmail"] = send_customer_email
        if identity_check_type is not UNSET:
            field_dict["identityCheckType"] = identity_check_type
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rule_translation import RuleTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle", UNSET)

        description = d.pop("description", UNSET)

        related_plenigo_offer_id = d.pop("relatedPlenigoOfferId", UNSET)

        unrelated_plenigo_offer_id = d.pop("unrelatedPlenigoOfferId", UNSET)

        cancel_unrelated = d.pop("cancelUnrelated", UNSET)

        send_customer_email = d.pop("sendCustomerEmail", UNSET)

        _identity_check_type = d.pop("identityCheckType", UNSET)
        identity_check_type: Union[Unset, RelationRuleBaseIdentityCheckType]
        if isinstance(_identity_check_type, Unset) or not _identity_check_type:
            identity_check_type = UNSET
        else:
            identity_check_type = RelationRuleBaseIdentityCheckType(_identity_check_type)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = RuleTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        relation_rule_base = cls(
            internal_title=internal_title,
            description=description,
            related_plenigo_offer_id=related_plenigo_offer_id,
            unrelated_plenigo_offer_id=unrelated_plenigo_offer_id,
            cancel_unrelated=cancel_unrelated,
            send_customer_email=send_customer_email,
            identity_check_type=identity_check_type,
            translations=translations,
        )

        relation_rule_base.additional_properties = d
        return relation_rule_base

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
