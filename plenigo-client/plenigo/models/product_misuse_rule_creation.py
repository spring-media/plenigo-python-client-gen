from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_misuse_rule_creation_duration_timespan import ProductMisuseRuleCreationDurationTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.misuse_rule_translation import MisuseRuleTranslation


T = TypeVar("T", bound="ProductMisuseRuleCreation")


@attr.s(auto_attribs=True)
class ProductMisuseRuleCreation:
    """
    Attributes:
        internal_title (str): internal title of the misuse rule
        alternative_plenigo_offer_id (str): plenigo offer id of the offer to sell if product is already bought
        description (Union[Unset, str]): Internal description of the misuse rule
        duration (Union[Unset, int]): time duration the customer must wait to be able to buy the offer again - zero
            means forever
        duration_timespan (Union[Unset, ProductMisuseRuleCreationDurationTimespan]): time span that the duration is
            related to
        translations (Union[Unset, List['MisuseRuleTranslation']]): translations associated with this misuse rule
    """

    internal_title: str
    alternative_plenigo_offer_id: str
    description: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    duration_timespan: Union[Unset, ProductMisuseRuleCreationDurationTimespan] = UNSET
    translations: Union[Unset, List["MisuseRuleTranslation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        alternative_plenigo_offer_id = self.alternative_plenigo_offer_id
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "alternativePlenigoOfferId": alternative_plenigo_offer_id,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.misuse_rule_translation import MisuseRuleTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        alternative_plenigo_offer_id = d.pop("alternativePlenigoOfferId")

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        _duration_timespan = d.pop("durationTimespan", UNSET)
        duration_timespan: Union[Unset, ProductMisuseRuleCreationDurationTimespan]
        if isinstance(_duration_timespan, Unset):
            duration_timespan = UNSET
        else:
            duration_timespan = ProductMisuseRuleCreationDurationTimespan(_duration_timespan)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = MisuseRuleTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        product_misuse_rule_creation = cls(
            internal_title=internal_title,
            alternative_plenigo_offer_id=alternative_plenigo_offer_id,
            description=description,
            duration=duration,
            duration_timespan=duration_timespan,
            translations=translations,
        )

        product_misuse_rule_creation.additional_properties = d
        return product_misuse_rule_creation

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
