from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_digital_ivw_rule_price_corridor import ProductDigitalIvwRulePriceCorridor


T = TypeVar("T", bound="ProductDigitalIvwRule")


@_attrs_define
class ProductDigitalIvwRule:
    """
    Attributes:
        price_corridor (ProductDigitalIvwRulePriceCorridor): the ivw price corridors which should be used for this rule,
            starting with the lowest value.
    """

    price_corridor: "ProductDigitalIvwRulePriceCorridor"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_corridor = self.price_corridor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priceCorridor": price_corridor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_digital_ivw_rule_price_corridor import ProductDigitalIvwRulePriceCorridor

        d = src_dict.copy()
        price_corridor = ProductDigitalIvwRulePriceCorridor.from_dict(d.pop("priceCorridor"))

        product_digital_ivw_rule = cls(
            price_corridor=price_corridor,
        )

        product_digital_ivw_rule.additional_properties = d
        return product_digital_ivw_rule

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
