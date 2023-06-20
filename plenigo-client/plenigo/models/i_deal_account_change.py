from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IDealAccountChange")


@attr.s(auto_attribs=True)
class IDealAccountChange:
    """
    Attributes:
        owner (str): name on bank account
        obfuscated_iban (str): obfuscated IBAN
        psp_account_id (str): payment service provider iDeal account id
        fingerprint (str): fingerprint to check account uniqueness
        preferred (bool): flag indicating if iDeal account is the preferred one
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
    """

    owner: str
    obfuscated_iban: str
    psp_account_id: str
    fingerprint: str
    preferred: bool
    invalid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner
        obfuscated_iban = self.obfuscated_iban
        psp_account_id = self.psp_account_id
        fingerprint = self.fingerprint
        preferred = self.preferred
        invalid = self.invalid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "obfuscatedIban": obfuscated_iban,
                "pspAccountId": psp_account_id,
                "fingerprint": fingerprint,
                "preferred": preferred,
            }
        )
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        obfuscated_iban = d.pop("obfuscatedIban")

        psp_account_id = d.pop("pspAccountId")

        fingerprint = d.pop("fingerprint")

        preferred = d.pop("preferred")

        invalid = d.pop("invalid", UNSET)

        i_deal_account_change = cls(
            owner=owner,
            obfuscated_iban=obfuscated_iban,
            psp_account_id=psp_account_id,
            fingerprint=fingerprint,
            preferred=preferred,
            invalid=invalid,
        )

        i_deal_account_change.additional_properties = d
        return i_deal_account_change

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
