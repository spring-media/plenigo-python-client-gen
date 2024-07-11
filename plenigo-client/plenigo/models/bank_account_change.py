from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankAccountChange")


@_attrs_define
class BankAccountChange:
    """
    Attributes:
        owner (str): name on bank account
        iban (str): <a href="https://en.wikipedia.org/wiki/International_Bank_Account_Number" target="_blank">IBAN</a>
        bic (Union[Unset, str]): <a href="https://en.wikipedia.org/wiki/ISO_9362" target="_blank">BIC</a> - only
            necessary for countries outside the EU
        preferred (Union[Unset, bool]): flag indicating if bank account is the preferred bank account - only one bank
            account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
    """

    owner: str
    iban: str
    bic: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner

        iban = self.iban

        bic = self.bic

        preferred = self.preferred

        invalid = self.invalid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "iban": iban,
            }
        )
        if bic is not UNSET:
            field_dict["bic"] = bic
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        iban = d.pop("iban")

        bic = d.pop("bic", UNSET)

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        bank_account_change = cls(
            owner=owner,
            iban=iban,
            bic=bic,
            preferred=preferred,
            invalid=invalid,
        )

        bank_account_change.additional_properties = d
        return bank_account_change

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
