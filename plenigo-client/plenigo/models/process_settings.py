from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.process_settings_emergency_mode import ProcessSettingsEmergencyMode
from ..models.process_settings_sso_name import ProcessSettingsSsoName
from ..models.process_settings_token_type import ProcessSettingsTokenType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sso_provider_settings import SsoProviderSettings


T = TypeVar("T", bound="ProcessSettings")


@attr.s(auto_attribs=True)
class ProcessSettings:
    """
    Attributes:
        token_type (Union[Unset, ProcessSettingsTokenType]): type of verfication token
        token_sms_countries (Union[Unset, List[str]]): if SMS is selected for verification token it can be restricted to
            specific countries
        allowed_domains (Union[Unset, str]): domains to be allowed for including the iframe
        sso_name (Union[Unset, ProcessSettingsSsoName]): indicating if first and last name are required, optional or not
            needed at all
        sso_recheck_terms (Union[Unset, bool]): flag indicating if terms should be recheck during login
        sso_opt_in (Union[Unset, bool]): flag indicating if opt in should be requested during registration
        checkout_opt_in (Union[Unset, bool]): flag indicating if opt in should be requested during checkout
        invoice_address_required (Union[Unset, bool]): flag indicating if invoice address should be requested during
            checkout
        delivery_address_required (Union[Unset, bool]): flag indicating if delivery address should be requested during
            checkout
        override_force_username (Union[Unset, bool]): flag indicating if username required is determined by the sub
            company
        force_username (Union[Unset, bool]): flag indicating if username is required
        max_sessions (Union[Unset, int]): maximum allowed parallel sessions for a customer
        additional_checkout_text (Union[Unset, str]): additional text to show during checkout
        sso_opt_in_text (Union[Unset, str]): opt in text to show during SSO
        checkout_opt_in_text (Union[Unset, str]): opt in text to show during checkout
        sso_term_text (Union[Unset, str]): term text to show during SSO
        checkout_term_text (Union[Unset, str]): term text to show during checkout
        emergency_mode (Union[Unset, ProcessSettingsEmergencyMode]): indication if emergency mode is active
        disable_sso_functionality (Union[Unset, bool]): flag indicating if sso functionality is disabled
        sso_providers (Union[Unset, SsoProviderSettings]):
    """

    token_type: Union[Unset, ProcessSettingsTokenType] = UNSET
    token_sms_countries: Union[Unset, List[str]] = UNSET
    allowed_domains: Union[Unset, str] = UNSET
    sso_name: Union[Unset, ProcessSettingsSsoName] = UNSET
    sso_recheck_terms: Union[Unset, bool] = UNSET
    sso_opt_in: Union[Unset, bool] = UNSET
    checkout_opt_in: Union[Unset, bool] = UNSET
    invoice_address_required: Union[Unset, bool] = UNSET
    delivery_address_required: Union[Unset, bool] = UNSET
    override_force_username: Union[Unset, bool] = UNSET
    force_username: Union[Unset, bool] = UNSET
    max_sessions: Union[Unset, int] = UNSET
    additional_checkout_text: Union[Unset, str] = UNSET
    sso_opt_in_text: Union[Unset, str] = UNSET
    checkout_opt_in_text: Union[Unset, str] = UNSET
    sso_term_text: Union[Unset, str] = UNSET
    checkout_term_text: Union[Unset, str] = UNSET
    emergency_mode: Union[Unset, ProcessSettingsEmergencyMode] = UNSET
    disable_sso_functionality: Union[Unset, bool] = UNSET
    sso_providers: Union[Unset, "SsoProviderSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_type: Union[Unset, str] = UNSET
        if not isinstance(self.token_type, Unset):
            token_type = self.token_type.value

        token_sms_countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.token_sms_countries, Unset):
            token_sms_countries = self.token_sms_countries

        allowed_domains = self.allowed_domains
        sso_name: Union[Unset, str] = UNSET
        if not isinstance(self.sso_name, Unset):
            sso_name = self.sso_name.value

        sso_recheck_terms = self.sso_recheck_terms
        sso_opt_in = self.sso_opt_in
        checkout_opt_in = self.checkout_opt_in
        invoice_address_required = self.invoice_address_required
        delivery_address_required = self.delivery_address_required
        override_force_username = self.override_force_username
        force_username = self.force_username
        max_sessions = self.max_sessions
        additional_checkout_text = self.additional_checkout_text
        sso_opt_in_text = self.sso_opt_in_text
        checkout_opt_in_text = self.checkout_opt_in_text
        sso_term_text = self.sso_term_text
        checkout_term_text = self.checkout_term_text
        emergency_mode: Union[Unset, str] = UNSET
        if not isinstance(self.emergency_mode, Unset):
            emergency_mode = self.emergency_mode.value

        disable_sso_functionality = self.disable_sso_functionality
        sso_providers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sso_providers, Unset):
            sso_providers = self.sso_providers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_type is not UNSET:
            field_dict["tokenType"] = token_type
        if token_sms_countries is not UNSET:
            field_dict["tokenSmsCountries"] = token_sms_countries
        if allowed_domains is not UNSET:
            field_dict["allowedDomains"] = allowed_domains
        if sso_name is not UNSET:
            field_dict["ssoName"] = sso_name
        if sso_recheck_terms is not UNSET:
            field_dict["ssoRecheckTerms"] = sso_recheck_terms
        if sso_opt_in is not UNSET:
            field_dict["ssoOptIn"] = sso_opt_in
        if checkout_opt_in is not UNSET:
            field_dict["checkoutOptIn"] = checkout_opt_in
        if invoice_address_required is not UNSET:
            field_dict["invoiceAddressRequired"] = invoice_address_required
        if delivery_address_required is not UNSET:
            field_dict["deliveryAddressRequired"] = delivery_address_required
        if override_force_username is not UNSET:
            field_dict["overrideForceUsername"] = override_force_username
        if force_username is not UNSET:
            field_dict["forceUsername"] = force_username
        if max_sessions is not UNSET:
            field_dict["maxSessions"] = max_sessions
        if additional_checkout_text is not UNSET:
            field_dict["additionalCheckoutText"] = additional_checkout_text
        if sso_opt_in_text is not UNSET:
            field_dict["ssoOptInText"] = sso_opt_in_text
        if checkout_opt_in_text is not UNSET:
            field_dict["checkoutOptInText"] = checkout_opt_in_text
        if sso_term_text is not UNSET:
            field_dict["ssoTermText"] = sso_term_text
        if checkout_term_text is not UNSET:
            field_dict["checkoutTermText"] = checkout_term_text
        if emergency_mode is not UNSET:
            field_dict["emergencyMode"] = emergency_mode
        if disable_sso_functionality is not UNSET:
            field_dict["disableSsoFunctionality"] = disable_sso_functionality
        if sso_providers is not UNSET:
            field_dict["ssoProviders"] = sso_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sso_provider_settings import SsoProviderSettings

        d = src_dict.copy()
        _token_type = d.pop("tokenType", UNSET)
        token_type: Union[Unset, ProcessSettingsTokenType]
        if isinstance(_token_type, Unset):
            token_type = UNSET
        else:
            token_type = ProcessSettingsTokenType(_token_type)

        token_sms_countries = cast(List[str], d.pop("tokenSmsCountries", UNSET))

        allowed_domains = d.pop("allowedDomains", UNSET)

        _sso_name = d.pop("ssoName", UNSET)
        sso_name: Union[Unset, ProcessSettingsSsoName]
        if isinstance(_sso_name, Unset):
            sso_name = UNSET
        else:
            sso_name = ProcessSettingsSsoName(_sso_name)

        sso_recheck_terms = d.pop("ssoRecheckTerms", UNSET)

        sso_opt_in = d.pop("ssoOptIn", UNSET)

        checkout_opt_in = d.pop("checkoutOptIn", UNSET)

        invoice_address_required = d.pop("invoiceAddressRequired", UNSET)

        delivery_address_required = d.pop("deliveryAddressRequired", UNSET)

        override_force_username = d.pop("overrideForceUsername", UNSET)

        force_username = d.pop("forceUsername", UNSET)

        max_sessions = d.pop("maxSessions", UNSET)

        additional_checkout_text = d.pop("additionalCheckoutText", UNSET)

        sso_opt_in_text = d.pop("ssoOptInText", UNSET)

        checkout_opt_in_text = d.pop("checkoutOptInText", UNSET)

        sso_term_text = d.pop("ssoTermText", UNSET)

        checkout_term_text = d.pop("checkoutTermText", UNSET)

        _emergency_mode = d.pop("emergencyMode", UNSET)
        emergency_mode: Union[Unset, ProcessSettingsEmergencyMode]
        if isinstance(_emergency_mode, Unset):
            emergency_mode = UNSET
        else:
            emergency_mode = ProcessSettingsEmergencyMode(_emergency_mode)

        disable_sso_functionality = d.pop("disableSsoFunctionality", UNSET)

        _sso_providers = d.pop("ssoProviders", UNSET)
        sso_providers: Union[Unset, SsoProviderSettings]
        if isinstance(_sso_providers, Unset):
            sso_providers = UNSET
        else:
            sso_providers = SsoProviderSettings.from_dict(_sso_providers)

        process_settings = cls(
            token_type=token_type,
            token_sms_countries=token_sms_countries,
            allowed_domains=allowed_domains,
            sso_name=sso_name,
            sso_recheck_terms=sso_recheck_terms,
            sso_opt_in=sso_opt_in,
            checkout_opt_in=checkout_opt_in,
            invoice_address_required=invoice_address_required,
            delivery_address_required=delivery_address_required,
            override_force_username=override_force_username,
            force_username=force_username,
            max_sessions=max_sessions,
            additional_checkout_text=additional_checkout_text,
            sso_opt_in_text=sso_opt_in_text,
            checkout_opt_in_text=checkout_opt_in_text,
            sso_term_text=sso_term_text,
            checkout_term_text=checkout_term_text,
            emergency_mode=emergency_mode,
            disable_sso_functionality=disable_sso_functionality,
            sso_providers=sso_providers,
        )

        process_settings.additional_properties = d
        return process_settings

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
