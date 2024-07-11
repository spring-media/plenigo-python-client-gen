from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerSessionToken")


@_attrs_define
class CustomerSessionToken:
    """
    Attributes:
        customer_session (Union[Unset, str]): customer session string to be provided for all functionality that needs an
            active customer session - the string size can be very long so don't
            set any length restrictions if saved within a database or something similar
    """

    customer_session: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_session = self.customer_session

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_session is not UNSET:
            field_dict["customerSession"] = customer_session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_session = d.pop("customerSession", UNSET)

        customer_session_token = cls(
            customer_session=customer_session,
        )

        customer_session_token.additional_properties = d
        return customer_session_token

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
