import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_channel_base_changed_by_type import ApiChannelBaseChangedByType
from ..models.api_channel_base_status import ApiChannelBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiChannelBase")


@attr.s(auto_attribs=True)
class ApiChannelBase:
    """
    Attributes:
        id (str): unique id of the channel in the context of a company
        changed_date (datetime.datetime): changed date of the channel with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_by (str): id who changed the channel
        changed_by_type (ApiChannelBaseChangedByType): type of changed by
        channel_name (str): name of the channel
        voucher_amount (int): represents the amount of the vouchers of this channel
        status (ApiChannelBaseStatus): status of the campaign
        custom_data (Union[Unset, str]): free text field
    """

    id: str
    changed_date: datetime.datetime
    changed_by: str
    changed_by_type: ApiChannelBaseChangedByType
    channel_name: str
    voucher_amount: int
    status: ApiChannelBaseStatus
    custom_data: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        changed_date = self.changed_date.isoformat()

        changed_by = self.changed_by
        changed_by_type = self.changed_by_type.value

        channel_name = self.channel_name
        voucher_amount = self.voucher_amount
        status = self.status.value

        custom_data = self.custom_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "changedDate": changed_date,
                "changedBy": changed_by,
                "changedByType": changed_by_type,
                "channelName": channel_name,
                "voucherAmount": voucher_amount,
                "status": status,
            }
        )
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        changed_date = isoparse(d.pop("changedDate"))

        changed_by = d.pop("changedBy")

        changed_by_type = ApiChannelBaseChangedByType(d.pop("changedByType"))

        channel_name = d.pop("channelName")

        voucher_amount = d.pop("voucherAmount")

        status = ApiChannelBaseStatus(d.pop("status"))

        custom_data = d.pop("customData", UNSET)

        api_channel_base = cls(
            id=id,
            changed_date=changed_date,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            channel_name=channel_name,
            voucher_amount=voucher_amount,
            status=status,
            custom_data=custom_data,
        )

        api_channel_base.additional_properties = d
        return api_channel_base

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
