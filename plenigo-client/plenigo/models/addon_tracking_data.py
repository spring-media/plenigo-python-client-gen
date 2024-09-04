import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_tracking_data_additional_data import AddonTrackingDataAdditionalData


T = TypeVar("T", bound="AddonTrackingData")


@_attrs_define
class AddonTrackingData:
    """
    Attributes:
        tracking_id (Union[Unset, str]): tracking id of the transportation service provider
        tracking_url (Union[Unset, str]): tracking url to track delivery
        service_provider (Union[Unset, str]): transportation service provider
        sending_date (Union[None, Unset, datetime.datetime]): date the sending was starting with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        arrival_date (Union[None, Unset, datetime.datetime]): date the delivery arrived with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        additional_data (Union[Unset, AddonTrackingDataAdditionalData]):
    """

    tracking_id: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    service_provider: Union[Unset, str] = UNSET
    sending_date: Union[None, Unset, datetime.datetime] = UNSET
    arrival_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_data: Union[Unset, "AddonTrackingDataAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracking_id = self.tracking_id

        tracking_url = self.tracking_url

        service_provider = self.service_provider

        sending_date: Union[None, Unset, str]
        if isinstance(self.sending_date, Unset) or self.sending_date is None:
            sending_date = UNSET
        elif isinstance(self.sending_date, datetime.datetime):
            sending_date = self.sending_date.isoformat()
        else:
            sending_date = self.sending_date

        arrival_date: Union[None, Unset, str]
        if isinstance(self.arrival_date, Unset) or self.arrival_date is None:
            arrival_date = UNSET
        elif isinstance(self.arrival_date, datetime.datetime):
            arrival_date = self.arrival_date.isoformat()
        else:
            arrival_date = self.arrival_date

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

        def _parse_sending_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sending_date_type_0 = isoparse(data)

                return sending_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        sending_date = _parse_sending_date(d.pop("sendingDate", UNSET))

        def _parse_arrival_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                arrival_date_type_0 = isoparse(data)

                return arrival_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        arrival_date = _parse_arrival_date(d.pop("arrivalDate", UNSET))

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, AddonTrackingDataAdditionalData]
        if isinstance(_additional_data, Unset) or not _additional_data:
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
