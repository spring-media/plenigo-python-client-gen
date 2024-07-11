from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_addon_tracking_data_status import UpdateAddonTrackingDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_tracking_data import AddonTrackingData


T = TypeVar("T", bound="UpdateAddonTrackingData")


@_attrs_define
class UpdateAddonTrackingData:
    """
    Attributes:
        status (UpdateAddonTrackingDataStatus): delivery status of the purchased addon
        tracking_data (Union[Unset, AddonTrackingData]):
    """

    status: UpdateAddonTrackingDataStatus
    tracking_data: Union[Unset, "AddonTrackingData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        tracking_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_data, Unset):
            tracking_data = self.tracking_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if tracking_data is not UNSET:
            field_dict["trackingData"] = tracking_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addon_tracking_data import AddonTrackingData

        d = src_dict.copy()
        status = UpdateAddonTrackingDataStatus(d.pop("status"))

        _tracking_data = d.pop("trackingData", UNSET)
        tracking_data: Union[Unset, AddonTrackingData]
        if isinstance(_tracking_data, Unset):
            tracking_data = UNSET
        else:
            tracking_data = AddonTrackingData.from_dict(_tracking_data)

        update_addon_tracking_data = cls(
            status=status,
            tracking_data=tracking_data,
        )

        update_addon_tracking_data.additional_properties = d
        return update_addon_tracking_data

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
