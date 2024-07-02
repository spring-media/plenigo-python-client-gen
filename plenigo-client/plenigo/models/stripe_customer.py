from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeCustomer")


@_attrs_define
class StripeCustomer:
    """
    Attributes:
        stripe_id (Union[Unset, str]): Stripe id of the customer
        customer_id (Union[Unset, str]): unique id of the customer
    """

    stripe_id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_id = self.stripe_id

        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe_id is not UNSET:
            field_dict["stripeId"] = stripe_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stripe_id = d.pop("stripeId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        stripe_customer = cls(
            stripe_id=stripe_id,
            customer_id=customer_id,
        )

        stripe_customer.additional_properties = d
        return stripe_customer

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
