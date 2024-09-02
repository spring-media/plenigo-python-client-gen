import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_sessions import ActiveSessions


T = TypeVar("T", bound="SessionLimitReached")


@_attrs_define
class SessionLimitReached:
    """
    Attributes:
        active_sessions (Union[Unset, ActiveSessions]):
        removal_token (Union[None, Unset, datetime.datetime]): temporary session for removing active session
    """

    active_sessions: Union[Unset, "ActiveSessions"] = UNSET
    removal_token: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_sessions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_sessions, Unset):
            active_sessions = self.active_sessions.to_dict()

        removal_token: Union[None, Unset, str]
        if isinstance(self.removal_token, Unset) or self.removal_token is None:
            removal_token = UNSET
        elif isinstance(self.removal_token, datetime.datetime):
            removal_token = self.removal_token.isoformat()
        else:
            removal_token = self.removal_token

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
        from ..models.active_sessions import ActiveSessions

        d = src_dict.copy()
        _active_sessions = d.pop("activeSessions", UNSET)
        active_sessions: Union[Unset, ActiveSessions]
        if isinstance(_active_sessions, Unset) or not _active_sessions:
            active_sessions = UNSET
        else:
            active_sessions = ActiveSessions.from_dict(_active_sessions)

        def _parse_removal_token(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removal_token_type_0 = isoparse(data)

                return removal_token_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        removal_token = _parse_removal_token(d.pop("removalToken", UNSET))

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
