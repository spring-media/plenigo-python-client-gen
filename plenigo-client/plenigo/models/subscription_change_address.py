from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_change_address_address_type import SubscriptionChangeAddressAddressType

T = TypeVar("T", bound="SubscriptionChangeAddress")


@_attrs_define
class SubscriptionChangeAddress:
    """
    Attributes:
        address_id (int): id of the address to add to the subscription
        address_type (SubscriptionChangeAddressAddressType): address type of the address to change
    """

    address_id: int
    address_type: SubscriptionChangeAddressAddressType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_id = self.address_id

        address_type = self.address_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressId": address_id,
                "addressType": address_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_id = d.pop("addressId")

        address_type = SubscriptionChangeAddressAddressType(d.pop("addressType"))

        subscription_change_address = cls(
            address_id=address_id,
            address_type=address_type,
        )

        subscription_change_address.additional_properties = d
        return subscription_change_address

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
