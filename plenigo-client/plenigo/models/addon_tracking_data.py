import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_tracking_data_additional_data import AddonTrackingDataAdditionalData


T = TypeVar("T", bound="AddonTrackingData")


@attr.s(auto_attribs=True)
class AddonTrackingData:
    """
    Attributes:
        tracking_id (Union[Unset, str]): tracking id of the transportation service provider
        tracking_url (Union[Unset, str]): tracking url to track delivery
        service_provider (Union[Unset, str]): transportation service provider
        sending_date (Union[Unset, datetime.datetime]): date the sending was starting with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        arrival_date (Union[Unset, datetime.datetime]): date the delivery arrived with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        additional_data (Union[Unset, AddonTrackingDataAdditionalData]):
    """

    tracking_id: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    service_provider: Union[Unset, str] = UNSET
    sending_date: Union[Unset, datetime.datetime] = UNSET
    arrival_date: Union[Unset, datetime.datetime] = UNSET
    additional_data: Union[Unset, "AddonTrackingDataAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracking_id = self.tracking_id
        tracking_url = self.tracking_url
        service_provider = self.service_provider
        sending_date: Union[Unset, str] = UNSET
        if not isinstance(self.sending_date, Unset):
            sending_date = self.sending_date.isoformat()

        arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_date, Unset):
            arrival_date = self.arrival_date.isoformat()

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url
        if service_provider is not UNSET:
            field_dict["serviceProvider"] = service_provider
        if sending_date is not UNSET:
            field_dict["sendingDate"] = sending_date
        if arrival_date is not UNSET:
            field_dict["arrivalDate"] = arrival_date
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addon_tracking_data_additional_data import AddonTrackingDataAdditionalData

        d = src_dict.copy()
        tracking_id = d.pop("trackingId", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        service_provider = d.pop("serviceProvider", UNSET)

        _sending_date = d.pop("sendingDate", UNSET)
        sending_date: Union[Unset, datetime.datetime]
        if isinstance(_sending_date, Unset):
            sending_date = UNSET
        else:
            sending_date = isoparse(_sending_date)

        _arrival_date = d.pop("arrivalDate", UNSET)
        arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_arrival_date, Unset):
            arrival_date = UNSET
        else:
            arrival_date = isoparse(_arrival_date)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, AddonTrackingDataAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = AddonTrackingDataAdditionalData.from_dict(_additional_data)

        addon_tracking_data = cls(
            tracking_id=tracking_id,
            tracking_url=tracking_url,
            service_provider=service_provider,
            sending_date=sending_date,
            arrival_date=arrival_date,
            additional_data=additional_data,
        )

        addon_tracking_data.additional_properties = d
        return addon_tracking_data

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
