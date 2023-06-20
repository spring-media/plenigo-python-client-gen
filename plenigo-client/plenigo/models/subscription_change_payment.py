from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.subscription_change_payment_payment_method import SubscriptionChangePaymentPaymentMethod

T = TypeVar("T", bound="SubscriptionChangePayment")


@attr.s(auto_attribs=True)
class SubscriptionChangePayment:
    """
    Attributes:
        payment_method (SubscriptionChangePaymentPaymentMethod): payment method used to pay for the subscription
        payment_method_id (int): id of the payment method that is associated with this subscription
    """

    payment_method: SubscriptionChangePaymentPaymentMethod
    payment_method_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method = self.payment_method.value

        payment_method_id = self.payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentMethod": payment_method,
                "paymentMethodId": payment_method_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_method = SubscriptionChangePaymentPaymentMethod(d.pop("paymentMethod"))

        payment_method_id = d.pop("paymentMethodId")

        subscription_change_payment = cls(
            payment_method=payment_method,
            payment_method_id=payment_method_id,
        )

        subscription_change_payment.additional_properties = d
        return subscription_change_payment

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
