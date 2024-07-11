from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionItemChangeDiscount")


@_attrs_define
class SubscriptionItemChangeDiscount:
    """
    Attributes:
        subscription_item_id (int): unique id of the subscription item to change discount for
        discount_percentage (int): discount offered to the subscription item
    """

    subscription_item_id: int
    discount_percentage: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_item_id = self.subscription_item_id

        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionItemId": subscription_item_id,
                "discountPercentage": discount_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_item_id = d.pop("subscriptionItemId")

        discount_percentage = d.pop("discountPercentage")

        subscription_item_change_discount = cls(
            subscription_item_id=subscription_item_id,
            discount_percentage=discount_percentage,
        )

        subscription_item_change_discount.additional_properties = d
        return subscription_item_change_discount

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
