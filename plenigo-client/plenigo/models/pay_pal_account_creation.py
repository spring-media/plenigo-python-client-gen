from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayPalAccountCreation")


@_attrs_define
class PayPalAccountCreation:
    """
    Attributes:
        billing_agreement_id (str): PayPal billing agreement
        preferred (Union[Unset, bool]): flag indicating if PayPal account is the preferred PayPal account - only one
            PayPal account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        customer_id (Union[Unset, str]): unique id of the customer the PayPal account belongs to
    """

    billing_agreement_id: str
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_agreement_id = self.billing_agreement_id

        preferred = self.preferred

        invalid = self.invalid

        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingAgreementId": billing_agreement_id,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_agreement_id = d.pop("billingAgreementId")

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        customer_id = d.pop("customerId", UNSET)

        pay_pal_account_creation = cls(
            billing_agreement_id=billing_agreement_id,
            preferred=preferred,
            invalid=invalid,
            customer_id=customer_id,
        )

        pay_pal_account_creation.additional_properties = d
        return pay_pal_account_creation

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
