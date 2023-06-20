from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreditUsageBase")


@attr.s(auto_attribs=True)
class CreditUsageBase:
    """
    Attributes:
        customer_id (str): id of the customer the credit usage should be accounted to
        unique_id (str): unique id of the wallet to use
        credits_used (int): amount of credits used
        reason (str): reason for credit usage
    """

    customer_id: str
    unique_id: str
    credits_used: int
    reason: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        unique_id = self.unique_id
        credits_used = self.credits_used
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "uniqueId": unique_id,
                "creditsUsed": credits_used,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("customerId")

        unique_id = d.pop("uniqueId")

        credits_used = d.pop("creditsUsed")

        reason = d.pop("reason")

        credit_usage_base = cls(
            customer_id=customer_id,
            unique_id=unique_id,
            credits_used=credits_used,
            reason=reason,
        )

        credit_usage_base.additional_properties = d
        return credit_usage_base

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
