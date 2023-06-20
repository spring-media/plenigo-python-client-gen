import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.campaign_creation_voucher_type import CampaignCreationVoucherType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_creation import ChannelCreation


T = TypeVar("T", bound="CampaignCreation")


@attr.s(auto_attribs=True)
class CampaignCreation:
    """
    Attributes:
        campaign_name (str): name of the campaign
        voucher_type (CampaignCreationVoucherType): represents the type of the vouchers of this campaign
        start_date (datetime.date): start date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        channels (List['ChannelCreation']):
        plenigo_offer_id (Union[Unset, str]): plenigo offer id the vouchers are for
        end_date (Union[Unset, datetime.date]): end date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
    """

    campaign_name: str
    voucher_type: CampaignCreationVoucherType
    start_date: datetime.date
    channels: List["ChannelCreation"]
    plenigo_offer_id: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        campaign_name = self.campaign_name
        voucher_type = self.voucher_type.value

        start_date = self.start_date.isoformat()
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        plenigo_offer_id = self.plenigo_offer_id
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignName": campaign_name,
                "voucherType": voucher_type,
                "startDate": start_date,
                "channels": channels,
            }
        )
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel_creation import ChannelCreation

        d = src_dict.copy()
        campaign_name = d.pop("campaignName")

        voucher_type = CampaignCreationVoucherType(d.pop("voucherType"))

        start_date = isoparse(d.pop("startDate")).date()

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ChannelCreation.from_dict(channels_item_data)

            channels.append(channels_item)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        campaign_creation = cls(
            campaign_name=campaign_name,
            voucher_type=voucher_type,
            start_date=start_date,
            channels=channels,
            plenigo_offer_id=plenigo_offer_id,
            end_date=end_date,
        )

        campaign_creation.additional_properties = d
        return campaign_creation

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
