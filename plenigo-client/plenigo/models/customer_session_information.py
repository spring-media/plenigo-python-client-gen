import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerSessionInformation")


@attr.s(auto_attribs=True)
class CustomerSessionInformation:
    """
    Attributes:
        session_id (Union[Unset, str]): unique id of the session
        os (Union[Unset, str]): operating system session was created on
        browser (Union[Unset, str]): browser session was created in
        created_at (Union[Unset, datetime.datetime]): creation date of the session with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
    """

    session_id: Union[Unset, str] = UNSET
    os: Union[Unset, str] = UNSET
    browser: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id
        os = self.os
        browser = self.browser
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if os is not UNSET:
            field_dict["os"] = os
        if browser is not UNSET:
            field_dict["browser"] = browser
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("sessionId", UNSET)

        os = d.pop("os", UNSET)

        browser = d.pop("browser", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        customer_session_information = cls(
            session_id=session_id,
            os=os,
            browser=browser,
            created_at=created_at,
        )

        customer_session_information.additional_properties = d
        return customer_session_information

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
