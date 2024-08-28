from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_analog_ivw_rule_ivw_price_type import ProductAnalogIvwRuleIvwPriceType
from ..models.product_analog_ivw_rule_ivw_type import ProductAnalogIvwRuleIvwType

T = TypeVar("T", bound="ProductAnalogIvwRule")


@_attrs_define
class ProductAnalogIvwRule:
    """
    Attributes:
        ivw_type (ProductAnalogIvwRuleIvwType): the ivw type which should be used for this rule
        ivw_price_type (ProductAnalogIvwRuleIvwPriceType): the ivw price type which should be used for this rule
        full_price_divergence_up (float): the divergence up to the price to be the specified ivw type
        full_price_divergence_down (float): the divergence down to the price to be the specified ivw type
        full_price_issue_id (int): id of the price issue associated with this ivw rule
        other_sale_price_divergence_down (float): the divergence down to the price to be the specified ivw type
        other_sale_price_issue_id (int): id of the price issue associated with this ivw rule
    """

    ivw_type: ProductAnalogIvwRuleIvwType
    ivw_price_type: ProductAnalogIvwRuleIvwPriceType
    full_price_divergence_up: float
    full_price_divergence_down: float
    full_price_issue_id: int
    other_sale_price_divergence_down: float
    other_sale_price_issue_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ivw_type = self.ivw_type.value

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
                "ivwType": ivw_type,
                "ivwPriceType": ivw_price_type,
                "fullPriceDivergenceUp": full_price_divergence_up,
                "fullPriceDivergenceDown": full_price_divergence_down,
                "fullPriceIssueId": full_price_issue_id,
                "otherSalePriceDivergenceDown": other_sale_price_divergence_down,
                "otherSalePriceIssueId": other_sale_price_issue_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ivw_type = ProductAnalogIvwRuleIvwType(d.pop("ivwType"))

        ivw_price_type = ProductAnalogIvwRuleIvwPriceType(d.pop("ivwPriceType"))

        full_price_divergence_up = d.pop("fullPriceDivergenceUp")

        full_price_divergence_down = d.pop("fullPriceDivergenceDown")

        full_price_issue_id = d.pop("fullPriceIssueId")

        other_sale_price_divergence_down = d.pop("otherSalePriceDivergenceDown")

        other_sale_price_issue_id = d.pop("otherSalePriceIssueId")

        product_analog_ivw_rule = cls(
            ivw_type=ivw_type,
            ivw_price_type=ivw_price_type,
            full_price_divergence_up=full_price_divergence_up,
            full_price_divergence_down=full_price_divergence_down,
            full_price_issue_id=full_price_issue_id,
            other_sale_price_divergence_down=other_sale_price_divergence_down,
            other_sale_price_issue_id=other_sale_price_issue_id,
        )

        product_analog_ivw_rule.additional_properties = d
        return product_analog_ivw_rule

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
