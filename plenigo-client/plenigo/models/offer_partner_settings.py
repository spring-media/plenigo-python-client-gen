from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_doo_settings import OfferDooSettings


T = TypeVar("T", bound="OfferPartnerSettings")


@_attrs_define
class OfferPartnerSettings:
    """
    Attributes:
        doo_settings (Union[Unset, OfferDooSettings]):
    """

    doo_settings: Union[Unset, "OfferDooSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doo_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.doo_settings, Unset):
            doo_settings = self.doo_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doo_settings is not UNSET:
            field_dict["dooSettings"] = doo_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_doo_settings import OfferDooSettings

        d = src_dict.copy()
        _doo_settings = d.pop("dooSettings", UNSET)
        doo_settings: Union[Unset, OfferDooSettings]
        if isinstance(_doo_settings, Unset) or not _doo_settings:
            doo_settings = UNSET
        else:
            doo_settings = OfferDooSettings.from_dict(_doo_settings)

        offer_partner_settings = cls(
            doo_settings=doo_settings,
        )

        offer_partner_settings.additional_properties = d
        return offer_partner_settings

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
