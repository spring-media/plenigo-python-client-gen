from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_sso_settings import GoogleSsoSettings


T = TypeVar("T", bound="SsoProviderSettings")


@attr.s(auto_attribs=True)
class SsoProviderSettings:
    """
    Attributes:
        active (bool): flag indicating if the SSO providers are active
        google_settings (Union[Unset, GoogleSsoSettings]):
    """

    active: bool
    google_settings: Union[Unset, "GoogleSsoSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        google_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.google_settings, Unset):
            google_settings = self.google_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
            }
        )
        if google_settings is not UNSET:
            field_dict["googleSettings"] = google_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_sso_settings import GoogleSsoSettings

        d = src_dict.copy()
        active = d.pop("active")

        _google_settings = d.pop("googleSettings", UNSET)
        google_settings: Union[Unset, GoogleSsoSettings]
        if isinstance(_google_settings, Unset):
            google_settings = UNSET
        else:
            google_settings = GoogleSsoSettings.from_dict(_google_settings)

        sso_provider_settings = cls(
            active=active,
            google_settings=google_settings,
        )

        sso_provider_settings.additional_properties = d
        return sso_provider_settings

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
