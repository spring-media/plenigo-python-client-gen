from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_ivw_rule_creation_ivw_price_type import ProductIvwRuleCreationIvwPriceType
from ..models.product_ivw_rule_creation_ivw_type import ProductIvwRuleCreationIvwType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductIvwRuleCreation")


@attr.s(auto_attribs=True)
class ProductIvwRuleCreation:
    """
    Attributes:
        title (str): title of the ivw rule
        internal_title (str): internal title of the ivw rule
        ivw_type (ProductIvwRuleCreationIvwType): the ivw type which should be used for this rule
        ivw_price_type (ProductIvwRuleCreationIvwPriceType): the ivw price type which should be used for this rule
        full_price_divergence_up (float): the divergence up to the price to be the specified ivw type
        full_price_divergence_down (float): the divergence down to the price to be the specified ivw type
        full_price_issue_id (int): id of the price issue associated with this ivw rule
        other_sale_price_divergence_down (float): the divergence down to the price to be the specified ivw type
        other_sale_price_issue_id (int): id of the price issue associated with this ivw rule
        description (Union[Unset, str]): Internal description of the ivw rule
    """

    title: str
    internal_title: str
    ivw_type: ProductIvwRuleCreationIvwType
    ivw_price_type: ProductIvwRuleCreationIvwPriceType
    full_price_divergence_up: float
    full_price_divergence_down: float
    full_price_issue_id: int
    other_sale_price_divergence_down: float
    other_sale_price_issue_id: int
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        internal_title = self.internal_title
        ivw_type = self.ivw_type.value

        ivw_price_type = self.ivw_price_type.value

        full_price_divergence_up = self.full_price_divergence_up
        full_price_divergence_down = self.full_price_divergence_down
        full_price_issue_id = self.full_price_issue_id
        other_sale_price_divergence_down = self.other_sale_price_divergence_down
        other_sale_price_issue_id = self.other_sale_price_issue_id
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "internalTitle": internal_title,
                "ivwType": ivw_type,
                "ivwPriceType": ivw_price_type,
                "fullPriceDivergenceUp": full_price_divergence_up,
                "fullPriceDivergenceDown": full_price_divergence_down,
                "fullPriceIssueId": full_price_issue_id,
                "otherSalePriceDivergenceDown": other_sale_price_divergence_down,
                "otherSalePriceIssueId": other_sale_price_issue_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        internal_title = d.pop("internalTitle")

        ivw_type = ProductIvwRuleCreationIvwType(d.pop("ivwType"))

        ivw_price_type = ProductIvwRuleCreationIvwPriceType(d.pop("ivwPriceType"))

        full_price_divergence_up = d.pop("fullPriceDivergenceUp")

        full_price_divergence_down = d.pop("fullPriceDivergenceDown")

        full_price_issue_id = d.pop("fullPriceIssueId")

        other_sale_price_divergence_down = d.pop("otherSalePriceDivergenceDown")

        other_sale_price_issue_id = d.pop("otherSalePriceIssueId")

        description = d.pop("description", UNSET)

        product_ivw_rule_creation = cls(
            title=title,
            internal_title=internal_title,
            ivw_type=ivw_type,
            ivw_price_type=ivw_price_type,
            full_price_divergence_up=full_price_divergence_up,
            full_price_divergence_down=full_price_divergence_down,
            full_price_issue_id=full_price_issue_id,
            other_sale_price_divergence_down=other_sale_price_divergence_down,
            other_sale_price_issue_id=other_sale_price_issue_id,
            description=description,
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
