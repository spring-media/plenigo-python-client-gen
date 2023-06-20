from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferToken")


@attr.s(auto_attribs=True)
class TransferToken:
    """
    Attributes:
        transfer_token (Union[Unset, str]): transfer token to get the the saved customer session for
    """

    transfer_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfer_token = self.transfer_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transfer_token is not UNSET:
            field_dict["transferToken"] = transfer_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transfer_token = d.pop("transferToken", UNSET)

        transfer_token = cls(
            transfer_token=transfer_token,
        )

        transfer_token.additional_properties = d
        return transfer_token

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
