from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_google_sso_authentication_sso_provider import CustomerGoogleSsoAuthenticationSsoProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_sso_authentication import GoogleSsoAuthentication


T = TypeVar("T", bound="CustomerGoogleSsoAuthentication")


@_attrs_define
class CustomerGoogleSsoAuthentication:
    """
    Attributes:
        sso_provider (CustomerGoogleSsoAuthenticationSsoProvider): sso provider name
        authentication_data (GoogleSsoAuthentication):
        os (Union[Unset, str]): operating system session was created on
        browser (Union[Unset, str]): browser session was created in
        source (Union[Unset, str]): source domain or app name
        source_url (Union[Unset, str]): source url
        ip_address (Union[Unset, str]): ip address
        country (Union[Unset, str]): country code formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        language (Union[Unset, str]): language of the customer
    """

    sso_provider: CustomerGoogleSsoAuthenticationSsoProvider
    authentication_data: "GoogleSsoAuthentication"
    os: Union[Unset, str] = UNSET
    browser: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sso_provider = self.sso_provider.value

        authentication_data = self.authentication_data.to_dict()

        os = self.os

        browser = self.browser

        source = self.source

        source_url = self.source_url

        ip_address = self.ip_address

        country = self.country

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssoProvider": sso_provider,
                "authenticationData": authentication_data,
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
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_sso_authentication import GoogleSsoAuthentication

        d = src_dict.copy()
        sso_provider = CustomerGoogleSsoAuthenticationSsoProvider(d.pop("ssoProvider"))

        authentication_data = GoogleSsoAuthentication.from_dict(d.pop("authenticationData"))

        os = d.pop("os", UNSET)

        browser = d.pop("browser", UNSET)

        source = d.pop("source", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        country = d.pop("country", UNSET)

        language = d.pop("language", UNSET)

        customer_google_sso_authentication = cls(
            sso_provider=sso_provider,
            authentication_data=authentication_data,
            os=os,
            browser=browser,
            source=source,
            source_url=source_url,
            ip_address=ip_address,
            country=country,
            language=language,
        )

        customer_google_sso_authentication.additional_properties = d
        return customer_google_sso_authentication

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
