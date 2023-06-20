from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayPalAccountChange")


@attr.s(auto_attribs=True)
class PayPalAccountChange:
    """
    Attributes:
        billing_agreement_id (str): PayPal billing agreement
        preferred (Union[Unset, bool]): flag indicating if PayPal account is the preferred PayPal account - only one
            PayPal account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
    """

    billing_agreement_id: str
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_agreement_id = self.billing_agreement_id
        preferred = self.preferred
        invalid = self.invalid

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_agreement_id = d.pop("billingAgreementId")

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        pay_pal_account_change = cls(
            billing_agreement_id=billing_agreement_id,
            preferred=preferred,
            invalid=invalid,
        )

        pay_pal_account_change.additional_properties = d
        return pay_pal_account_change

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
