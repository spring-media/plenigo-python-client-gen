from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscriptionPurchaseOrderIndicator")


@attr.s(auto_attribs=True)
class SubscriptionPurchaseOrderIndicator:
    """
    Attributes:
        purchase_order_indicator (str): purchase order indicator to set
    """

    purchase_order_indicator: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_indicator = self.purchase_order_indicator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderIndicator": purchase_order_indicator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_indicator = d.pop("purchaseOrderIndicator")

        subscription_purchase_order_indicator = cls(
            purchase_order_indicator=purchase_order_indicator,
        )

        subscription_purchase_order_indicator.additional_properties = d
        return subscription_purchase_order_indicator

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
