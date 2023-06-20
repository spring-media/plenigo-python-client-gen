import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerLogInAttemptBase")


@attr.s(auto_attribs=True)
class CustomerLogInAttemptBase:
    """
    Attributes:
        customer_id (Union[Unset, str]): id of the customer the login attempt is done for
        login_date (Union[Unset, datetime.datetime]): date time the login attempt happened with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        browser (Union[Unset, str]): browser used for log in attempt if available
        os (Union[Unset, str]): os used for log in attempt if available
        source (Union[Unset, str]): login source of the user for log in attempt if available
        source_url (Union[Unset, str]): souce url for log in attempt if available
        country (Union[Unset, str]): country of log in attempt if available
    """

    customer_id: Union[Unset, str] = UNSET
    login_date: Union[Unset, datetime.datetime] = UNSET
    browser: Union[Unset, str] = UNSET
    os: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        login_date: Union[Unset, str] = UNSET
        if not isinstance(self.login_date, Unset):
            login_date = self.login_date.isoformat()

        browser = self.browser
        os = self.os
        source = self.source
        source_url = self.source_url
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if login_date is not UNSET:
            field_dict["loginDate"] = login_date
        if browser is not UNSET:
            field_dict["browser"] = browser
        if os is not UNSET:
            field_dict["os"] = os
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        _login_date = d.pop("loginDate", UNSET)
        login_date: Union[Unset, datetime.datetime]
        if isinstance(_login_date, Unset):
            login_date = UNSET
        else:
            login_date = isoparse(_login_date)

        browser = d.pop("browser", UNSET)

        os = d.pop("os", UNSET)

        source = d.pop("source", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        country = d.pop("country", UNSET)

        customer_log_in_attempt_base = cls(
            customer_id=customer_id,
            login_date=login_date,
            browser=browser,
            os=os,
            source=source,
            source_url=source_url,
            country=country,
        )

        customer_log_in_attempt_base.additional_properties = d
        return customer_log_in_attempt_base

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
