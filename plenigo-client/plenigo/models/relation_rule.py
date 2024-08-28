import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.relation_rule_base_identity_check_type import RelationRuleBaseIdentityCheckType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_tag import ProductTag
    from ..models.rule_translation import RuleTranslation


T = TypeVar("T", bound="RelationRule")


@_attrs_define
class RelationRule:
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
        qualifying_product_tag_ids (Union[Unset, List[int]]): tags that qualifies for a product relation
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        relation_rule_id (Union[Unset, int]): unique id of the relation rule within a contract company
        product_tags (Union[Unset, List['ProductTag']]): tags associated with this product
    """

    internal_title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    related_plenigo_offer_id: Union[Unset, str] = UNSET
    unrelated_plenigo_offer_id: Union[Unset, str] = UNSET
    cancel_unrelated: Union[Unset, bool] = UNSET
    send_customer_email: Union[Unset, bool] = UNSET
    identity_check_type: Union[Unset, RelationRuleBaseIdentityCheckType] = UNSET
    translations: Union[Unset, List["RuleTranslation"]] = UNSET
    qualifying_product_tag_ids: Union[Unset, List[int]] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    relation_rule_id: Union[Unset, int] = UNSET
    product_tags: Union[Unset, List["ProductTag"]] = UNSET
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

        qualifying_product_tag_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.qualifying_product_tag_ids, Unset):
            qualifying_product_tag_ids = self.qualifying_product_tag_ids

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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        relation_rule_id = self.relation_rule_id

        product_tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_tags, Unset):
            product_tags = []
            for product_tags_item_data in self.product_tags:
                product_tags_item = product_tags_item_data.to_dict()
                product_tags.append(product_tags_item)

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
        if qualifying_product_tag_ids is not UNSET:
            field_dict["qualifyingProductTagIds"] = qualifying_product_tag_ids
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if relation_rule_id is not UNSET:
            field_dict["relationRuleId"] = relation_rule_id
        if product_tags is not UNSET:
            field_dict["productTags"] = product_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_tag import ProductTag
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

        qualifying_product_tag_ids = cast(List[int], d.pop("qualifyingProductTagIds", UNSET))

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

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        relation_rule_id = d.pop("relationRuleId", UNSET)

        product_tags = []
        _product_tags = d.pop("productTags", UNSET)
        for product_tags_item_data in _product_tags or []:
            product_tags_item = ProductTag.from_dict(product_tags_item_data)

            product_tags.append(product_tags_item)

        relation_rule = cls(
            internal_title=internal_title,
            description=description,
            related_plenigo_offer_id=related_plenigo_offer_id,
            unrelated_plenigo_offer_id=unrelated_plenigo_offer_id,
            cancel_unrelated=cancel_unrelated,
            send_customer_email=send_customer_email,
            identity_check_type=identity_check_type,
            translations=translations,
            qualifying_product_tag_ids=qualifying_product_tag_ids,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            relation_rule_id=relation_rule_id,
            product_tags=product_tags,
        )

        relation_rule.additional_properties = d
        return relation_rule

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
