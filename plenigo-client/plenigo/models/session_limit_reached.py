import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_customer_sessions import ActiveCustomerSessions


T = TypeVar("T", bound="SessionLimitReached")


@attr.s(auto_attribs=True)
class SessionLimitReached:
    """
    Attributes:
        active_sessions (Union[Unset, ActiveCustomerSessions]):
        removal_token (Union[Unset, datetime.datetime]): temporary session for removing active session
    """

    active_sessions: Union[Unset, "ActiveCustomerSessions"] = UNSET
    removal_token: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_sessions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_sessions, Unset):
            active_sessions = self.active_sessions.to_dict()

        removal_token: Union[Unset, str] = UNSET
        if not isinstance(self.removal_token, Unset):
            removal_token = self.removal_token.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_sessions is not UNSET:
            field_dict["activeSessions"] = active_sessions
        if removal_token is not UNSET:
            field_dict["removalToken"] = removal_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.active_customer_sessions import ActiveCustomerSessions

        d = src_dict.copy()
        _active_sessions = d.pop("activeSessions", UNSET)
        active_sessions: Union[Unset, ActiveCustomerSessions]
        if isinstance(_active_sessions, Unset):
            active_sessions = UNSET
        else:
            active_sessions = ActiveCustomerSessions.from_dict(_active_sessions)

        _removal_token = d.pop("removalToken", UNSET)
        removal_token: Union[Unset, datetime.datetime]
        if isinstance(_removal_token, Unset):
            removal_token = UNSET
        else:
            removal_token = isoparse(_removal_token)

        session_limit_reached = cls(
            active_sessions=active_sessions,
            removal_token=removal_token,
        )

        session_limit_reached.additional_properties = d
        return session_limit_reached

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
