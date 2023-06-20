from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockedIbanBase")


@attr.s(auto_attribs=True)
class BlockedIbanBase:
    """
    Attributes:
        iban (str): <a href="https://en.wikipedia.org/wiki/International_Bank_Account_Number" target="_blank">IBAN</a>
        description (Union[Unset, str]): description of the blocked iban
    """

    iban: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iban = self.iban
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iban": iban,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iban = d.pop("iban")

        description = d.pop("description", UNSET)

        blocked_iban_base = cls(
            iban=iban,
            description=description,
        )

        blocked_iban_base.additional_properties = d
        return blocked_iban_base

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
