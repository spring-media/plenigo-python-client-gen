from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_ivw_rule_creation_ivw_price_type import ProductIvwRuleCreationIvwPriceType
from ..models.product_ivw_rule_creation_ivw_type import ProductIvwRuleCreationIvwType
from ..models.product_ivw_rule_creation_type import ProductIvwRuleCreationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_analog_ivw_rule import ProductAnalogIvwRule
    from ..models.product_digital_ivw_rule import ProductDigitalIvwRule


T = TypeVar("T", bound="ProductIvwRuleCreation")


@_attrs_define
class ProductIvwRuleCreation:
    """
    Attributes:
        title (str): title of the ivw rule
        internal_title (str): internal title of the ivw rule
        type (ProductIvwRuleCreationType): the type for this rule
        rule (Union['ProductAnalogIvwRule', 'ProductDigitalIvwRule']): the object depends on the type of this rule.
        description (Union[Unset, str]): Internal description of the ivw rule
        ivw_type (Union[Unset, ProductIvwRuleCreationIvwType]): the ivw type which should be used for this rule
        ivw_price_type (Union[Unset, ProductIvwRuleCreationIvwPriceType]): the ivw price type which should be used for
            this rule
        full_price_divergence_up (Union[Unset, float]): the divergence up to the price to be the specified ivw type
        full_price_divergence_down (Union[Unset, float]): the divergence down to the price to be the specified ivw type
        full_price_issue_id (Union[Unset, int]): id of the price issue associated with this ivw rule
        other_sale_price_divergence_down (Union[Unset, float]): the divergence down to the price to be the specified ivw
            type
        other_sale_price_issue_id (Union[Unset, int]): id of the price issue associated with this ivw rule
    """

    title: str
    internal_title: str
    type: ProductIvwRuleCreationType
    rule: Union["ProductAnalogIvwRule", "ProductDigitalIvwRule"]
    description: Union[Unset, str] = UNSET
    ivw_type: Union[Unset, ProductIvwRuleCreationIvwType] = UNSET
    ivw_price_type: Union[Unset, ProductIvwRuleCreationIvwPriceType] = UNSET
    full_price_divergence_up: Union[Unset, float] = UNSET
    full_price_divergence_down: Union[Unset, float] = UNSET
    full_price_issue_id: Union[Unset, int] = UNSET
    other_sale_price_divergence_down: Union[Unset, float] = UNSET
    other_sale_price_issue_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.product_analog_ivw_rule import ProductAnalogIvwRule

        title = self.title

        internal_title = self.internal_title

        type = self.type.value

        rule: Dict[str, Any]
        if isinstance(self.rule, ProductAnalogIvwRule):
            rule = self.rule.to_dict()
        else:
            rule = self.rule.to_dict()

        description = self.description

        ivw_type: Union[Unset, str] = UNSET
        if not isinstance(self.ivw_type, Unset):
            ivw_type = self.ivw_type.value

        ivw_price_type: Union[Unset, str] = UNSET
        if not isinstance(self.ivw_price_type, Unset):
            ivw_price_type = self.ivw_price_type.value

        full_price_divergence_up = self.full_price_divergence_up

        full_price_divergence_down = self.full_price_divergence_down

        full_price_issue_id = self.full_price_issue_id

        other_sale_price_divergence_down = self.other_sale_price_divergence_down

        other_sale_price_issue_id = self.other_sale_price_issue_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "internalTitle": internal_title,
                "type": type,
                "rule": rule,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ivw_type is not UNSET:
            field_dict["ivwType"] = ivw_type
        if ivw_price_type is not UNSET:
            field_dict["ivwPriceType"] = ivw_price_type
        if full_price_divergence_up is not UNSET:
            field_dict["fullPriceDivergenceUp"] = full_price_divergence_up
        if full_price_divergence_down is not UNSET:
            field_dict["fullPriceDivergenceDown"] = full_price_divergence_down
        if full_price_issue_id is not UNSET:
            field_dict["fullPriceIssueId"] = full_price_issue_id
        if other_sale_price_divergence_down is not UNSET:
            field_dict["otherSalePriceDivergenceDown"] = other_sale_price_divergence_down
        if other_sale_price_issue_id is not UNSET:
            field_dict["otherSalePriceIssueId"] = other_sale_price_issue_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_analog_ivw_rule import ProductAnalogIvwRule
        from ..models.product_digital_ivw_rule import ProductDigitalIvwRule

        d = src_dict.copy()
        title = d.pop("title")

        internal_title = d.pop("internalTitle")

        type = ProductIvwRuleCreationType(d.pop("type"))

        def _parse_rule(data: object) -> Union["ProductAnalogIvwRule", "ProductDigitalIvwRule"]:
            # Try to parse the data as ProductAnalogIvwRule
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rule_type_0 = ProductAnalogIvwRule.from_dict(data)

                return rule_type_0
            except:  # noqa: E722
                pass

            # In order to parse the one remaining property in the union,
            # data must be a dict
            if not isinstance(data, dict):
                raise TypeError()

            # Finally, parse the data as ProductDigitalIvwRule
            rule_type_1 = ProductDigitalIvwRule.from_dict(data)

            return rule_type_1

        rule = _parse_rule(d.pop("rule"))

        description = d.pop("description", UNSET)

        _ivw_type = d.pop("ivwType", UNSET)
        ivw_type: Union[Unset, ProductIvwRuleCreationIvwType]
        if isinstance(_ivw_type, Unset) or not _ivw_type:
            ivw_type = UNSET
        else:
            ivw_type = ProductIvwRuleCreationIvwType(_ivw_type)

        _ivw_price_type = d.pop("ivwPriceType", UNSET)
        ivw_price_type: Union[Unset, ProductIvwRuleCreationIvwPriceType]
        if isinstance(_ivw_price_type, Unset) or not _ivw_price_type:
            ivw_price_type = UNSET
        else:
            ivw_price_type = ProductIvwRuleCreationIvwPriceType(_ivw_price_type)

        full_price_divergence_up = d.pop("fullPriceDivergenceUp", UNSET)

        full_price_divergence_down = d.pop("fullPriceDivergenceDown", UNSET)

        full_price_issue_id = d.pop("fullPriceIssueId", UNSET)

        other_sale_price_divergence_down = d.pop("otherSalePriceDivergenceDown", UNSET)

        other_sale_price_issue_id = d.pop("otherSalePriceIssueId", UNSET)

        product_ivw_rule_creation = cls(
            title=title,
            internal_title=internal_title,
            type=type,
            rule=rule,
            description=description,
            ivw_type=ivw_type,
            ivw_price_type=ivw_price_type,
            full_price_divergence_up=full_price_divergence_up,
            full_price_divergence_down=full_price_divergence_down,
            full_price_issue_id=full_price_issue_id,
            other_sale_price_divergence_down=other_sale_price_divergence_down,
            other_sale_price_issue_id=other_sale_price_issue_id,
        )

        product_ivw_rule_creation.additional_properties = d
        return product_ivw_rule_creation

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
