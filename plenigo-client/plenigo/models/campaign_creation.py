import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.campaign_creation_voucher_type import CampaignCreationVoucherType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_creation import ChannelCreation


T = TypeVar("T", bound="CampaignCreation")


@_attrs_define
class CampaignCreation:
    """
    Attributes:
        campaign_name (str): name of the campaign
        voucher_type (CampaignCreationVoucherType): represents the type of the vouchers of this campaign
        plenigo_offer_id (str): plenigo offer id the vouchers are for
        start_date (Union[None, datetime.date]): start date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        channels (List['ChannelCreation']):
        end_date (Union[None, Unset, datetime.date]): end date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
    """

    campaign_name: str
    voucher_type: CampaignCreationVoucherType
    plenigo_offer_id: str
    start_date: Union[None, datetime.date]
    channels: List["ChannelCreation"]
    end_date: Union[None, Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        campaign_name = self.campaign_name

        voucher_type = self.voucher_type.value

        plenigo_offer_id = self.plenigo_offer_id

        start_date: Union[None, str]
        if isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset) or self.end_date is None:
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignName": campaign_name,
                "voucherType": voucher_type,
                "plenigoOfferId": plenigo_offer_id,
                "startDate": start_date,
                "channels": channels,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel_creation import ChannelCreation

        d = src_dict.copy()
        campaign_name = d.pop("campaignName")

        voucher_type = CampaignCreationVoucherType(d.pop("voucherType"))

        plenigo_offer_id = d.pop("plenigoOfferId")

        def _parse_start_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.date], data)

        start_date = _parse_start_date(d.pop("startDate"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ChannelCreation.from_dict(channels_item_data)

            channels.append(channels_item)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        campaign_creation = cls(
            campaign_name=campaign_name,
            voucher_type=voucher_type,
            plenigo_offer_id=plenigo_offer_id,
            start_date=start_date,
            channels=channels,
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
