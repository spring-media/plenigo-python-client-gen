from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomerPasswordForgottenTwoFactor")


@_attrs_define
class CustomerPasswordForgottenTwoFactor:
    """
    Attributes:
        token (str): The token to validate the step.
        two_factor_token (str): two factor token to verify the customer
    """

    token: str
    two_factor_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        two_factor_token = self.two_factor_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "twoFactorToken": two_factor_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        two_factor_token = d.pop("twoFactorToken")

        customer_password_forgotten_two_factor = cls(
            token=token,
            two_factor_token=two_factor_token,
        )

        customer_password_forgotten_two_factor.additional_properties = d
        return customer_password_forgotten_two_factor

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
