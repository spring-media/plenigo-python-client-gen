import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_campaign_base_changed_by_type import ApiCampaignBaseChangedByType
from ..models.api_campaign_base_status import ApiCampaignBaseStatus
from ..models.api_campaign_base_voucher_type import ApiCampaignBaseVoucherType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCampaignBase")


@attr.s(auto_attribs=True)
class ApiCampaignBase:
    """
    Attributes:
        changed_date (datetime.datetime): changed date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_by (str): id who changed the campaign
        changed_by_type (ApiCampaignBaseChangedByType): type of changed by
        campaign_name (str): name of the campaign
        voucher_type (ApiCampaignBaseVoucherType): represents the type of the vouchers of this campaign
        status (ApiCampaignBaseStatus): status of the campaign
        start_date (datetime.date): start date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        campaign_id (Union[Unset, str]): unique id of the campaign in the context of a company
        plenigo_offer_id (Union[Unset, str]): offer id the vouchers are for
        end_date (Union[Unset, datetime.date]): end date of the campaign with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
    """

    changed_date: datetime.datetime
    changed_by: str
    changed_by_type: ApiCampaignBaseChangedByType
    campaign_name: str
    voucher_type: ApiCampaignBaseVoucherType
    status: ApiCampaignBaseStatus
    start_date: datetime.date
    campaign_id: Union[Unset, str] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        changed_date = self.changed_date.isoformat()

        changed_by = self.changed_by
        changed_by_type = self.changed_by_type.value

        campaign_name = self.campaign_name
        voucher_type = self.voucher_type.value

        status = self.status.value

        start_date = self.start_date.isoformat()
        campaign_id = self.campaign_id
        plenigo_offer_id = self.plenigo_offer_id
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changedDate": changed_date,
                "changedBy": changed_by,
                "changedByType": changed_by_type,
                "campaignName": campaign_name,
                "voucherType": voucher_type,
                "status": status,
                "startDate": start_date,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        changed_date = isoparse(d.pop("changedDate"))

        changed_by = d.pop("changedBy")

        changed_by_type = ApiCampaignBaseChangedByType(d.pop("changedByType"))

        campaign_name = d.pop("campaignName")

        voucher_type = ApiCampaignBaseVoucherType(d.pop("voucherType"))

        status = ApiCampaignBaseStatus(d.pop("status"))

        start_date = isoparse(d.pop("startDate")).date()

        campaign_id = d.pop("campaignId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        api_campaign_base = cls(
            changed_date=changed_date,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            campaign_name=campaign_name,
            voucher_type=voucher_type,
            status=status,
            start_date=start_date,
            campaign_id=campaign_id,
            plenigo_offer_id=plenigo_offer_id,
            end_date=end_date,
        )

        api_campaign_base.additional_properties = d
        return api_campaign_base

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
