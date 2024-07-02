from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionDeliveryAddition")


@_attrs_define
class SubscriptionDeliveryAddition:
    """
    Attributes:
        delivery_addition (int): amount of deliveries to add to open deliveries
    """

    delivery_addition: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_addition = self.delivery_addition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliveryAddition": delivery_addition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delivery_addition = d.pop("deliveryAddition")

        subscription_delivery_addition = cls(
            delivery_addition=delivery_addition,
        )

        subscription_delivery_addition.additional_properties = d
        return subscription_delivery_addition

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
