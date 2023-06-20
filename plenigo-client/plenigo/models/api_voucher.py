import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_voucher_changed_by_type import ApiVoucherChangedByType
from ..models.api_voucher_status import ApiVoucherStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiVoucher")


@attr.s(auto_attribs=True)
class ApiVoucher:
    """
    Attributes:
        id (str): unique id of the voucher in the context of a company
        created_date (datetime.datetime): created date of the channel with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_date (datetime.datetime): changed date of the channel with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_by (str): id who changed the channel
        changed_by_type (ApiVoucherChangedByType): type of changed by
        voucher_code (str): voucher code
        status (ApiVoucherStatus): status of the voucher
        custom_data (Union[Unset, str]): free text field
        order_id (Union[Unset, int]): order id this voucher was used
    """

    id: str
    created_date: datetime.datetime
    changed_date: datetime.datetime
    changed_by: str
    changed_by_type: ApiVoucherChangedByType
    voucher_code: str
    status: ApiVoucherStatus
    custom_data: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_date = self.created_date.isoformat()

        changed_date = self.changed_date.isoformat()

        changed_by = self.changed_by
        changed_by_type = self.changed_by_type.value

        voucher_code = self.voucher_code
        status = self.status.value

        custom_data = self.custom_data
        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdDate": created_date,
                "changedDate": changed_date,
                "changedBy": changed_by,
                "changedByType": changed_by_type,
                "voucherCode": voucher_code,
                "status": status,
            }
        )
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_date = isoparse(d.pop("createdDate"))

        changed_date = isoparse(d.pop("changedDate"))

        changed_by = d.pop("changedBy")

        changed_by_type = ApiVoucherChangedByType(d.pop("changedByType"))

        voucher_code = d.pop("voucherCode")

        status = ApiVoucherStatus(d.pop("status"))

        custom_data = d.pop("customData", UNSET)

        order_id = d.pop("orderId", UNSET)

        api_voucher = cls(
            id=id,
            created_date=created_date,
            changed_date=changed_date,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            voucher_code=voucher_code,
            status=status,
            custom_data=custom_data,
            order_id=order_id,
        )

        api_voucher.additional_properties = d
        return api_voucher

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
