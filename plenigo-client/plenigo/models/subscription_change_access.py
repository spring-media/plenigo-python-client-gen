from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscriptionChangeAccess")


@attr.s(auto_attribs=True)
class SubscriptionChangeAccess:
    """
    Attributes:
        access_blocked (bool): flag indicating if the access should be blocked
    """

    access_blocked: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_blocked = self.access_blocked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessBlocked": access_blocked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_blocked = d.pop("accessBlocked")

        subscription_change_access = cls(
            access_blocked=access_blocked,
        )

        subscription_change_access.additional_properties = d
        return subscription_change_access

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
