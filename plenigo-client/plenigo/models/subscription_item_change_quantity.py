from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscriptionItemChangeQuantity")


@attr.s(auto_attribs=True)
class SubscriptionItemChangeQuantity:
    """
    Attributes:
        subscription_item_id (int): unique id of the subscription item to change discount for
        quantity (int): quantity of purchased entities
    """

    subscription_item_id: int
    quantity: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_item_id = self.subscription_item_id
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionItemId": subscription_item_id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_item_id = d.pop("subscriptionItemId")

        quantity = d.pop("quantity")

        subscription_item_change_quantity = cls(
            subscription_item_id=subscription_item_id,
            quantity=quantity,
        )

        subscription_item_change_quantity.additional_properties = d
        return subscription_item_change_quantity

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
