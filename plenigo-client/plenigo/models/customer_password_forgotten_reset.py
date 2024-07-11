from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerPasswordForgottenReset")


@_attrs_define
class CustomerPasswordForgottenReset:
    """
    Attributes:
        token (str): The token to validate the step.
        password (str): new password of the customer
        os (Union[Unset, str]): operating system session was created on
        browser (Union[Unset, str]): browser session was created in
        source (Union[Unset, str]): source domain or app name
        source_url (Union[Unset, str]): source url
        ip_address (Union[Unset, str]): ip address
        country (Union[Unset, str]): country code formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
    """

    token: str
    password: str
    os: Union[Unset, str] = UNSET
    browser: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        password = self.password

        os = self.os

        browser = self.browser

        source = self.source

        source_url = self.source_url

        ip_address = self.ip_address

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "password": password,
            }
        )
        if os is not UNSET:
            field_dict["os"] = os
        if browser is not UNSET:
            field_dict["browser"] = browser
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        password = d.pop("password")

        os = d.pop("os", UNSET)

        browser = d.pop("browser", UNSET)

        source = d.pop("source", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        country = d.pop("country", UNSET)

        customer_password_forgotten_reset = cls(
            token=token,
            password=password,
            os=os,
            browser=browser,
            source=source,
            source_url=source_url,
            ip_address=ip_address,
            country=country,
        )

        customer_password_forgotten_reset.additional_properties = d
        return customer_password_forgotten_reset

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
