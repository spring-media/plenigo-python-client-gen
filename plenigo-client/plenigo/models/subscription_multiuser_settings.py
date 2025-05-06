from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionMultiuserSettings")


@_attrs_define
class SubscriptionMultiuserSettings:
    """
    Attributes:
        only_bundled_usage (Union[Unset, bool]): Indicates if only bundled usage is allowed.
        enable_self_service (Union[Unset, bool]): Indicates if self-service is enabled.
        invitation_validity_in_days (Union[Unset, int]): Number of days the invitation remains valid.
        invitation_url (Union[Unset, str]): URL for the invitation.
    """

    only_bundled_usage: Union[Unset, bool] = UNSET
    enable_self_service: Union[Unset, bool] = UNSET
    invitation_validity_in_days: Union[Unset, int] = UNSET
    invitation_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        only_bundled_usage = self.only_bundled_usage

        enable_self_service = self.enable_self_service

        invitation_validity_in_days = self.invitation_validity_in_days

        invitation_url = self.invitation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only_bundled_usage is not UNSET:
            field_dict["onlyBundledUsage"] = only_bundled_usage
        if enable_self_service is not UNSET:
            field_dict["enableSelfService"] = enable_self_service
        if invitation_validity_in_days is not UNSET:
            field_dict["invitationValidityInDays"] = invitation_validity_in_days
        if invitation_url is not UNSET:
            field_dict["invitationUrl"] = invitation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        only_bundled_usage = d.pop("onlyBundledUsage", UNSET)

        enable_self_service = d.pop("enableSelfService", UNSET)

        invitation_validity_in_days = d.pop("invitationValidityInDays", UNSET)

        invitation_url = d.pop("invitationUrl", UNSET)

        subscription_multiuser_settings = cls(
            only_bundled_usage=only_bundled_usage,
            enable_self_service=enable_self_service,
            invitation_validity_in_days=invitation_validity_in_days,
            invitation_url=invitation_url,
        )

        subscription_multiuser_settings.additional_properties = d
        return subscription_multiuser_settings

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
