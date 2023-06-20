import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_multi_voucher_changed_by_type import ApiMultiVoucherChangedByType
from ..models.api_multi_voucher_status import ApiMultiVoucherStatus

T = TypeVar("T", bound="ApiMultiVoucher")


@attr.s(auto_attribs=True)
class ApiMultiVoucher:
    """
    Attributes:
        id (str): unique id of the multi voucher in the context of a company
        created_date (datetime.datetime): created date of the multi voucher with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_date (datetime.datetime): changed date of the multi voucher with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        changed_by (str): id who changed the multi voucher
        changed_by_type (ApiMultiVoucherChangedByType): type of changed by
        voucher_code (str): voucher code
        status (ApiMultiVoucherStatus): status of the multi voucher
        voucher_amount (int): amount how often the voucher code can be used
        voucher_used (int): amount of how often the voucher code is already used
    """

    id: str
    created_date: datetime.datetime
    changed_date: datetime.datetime
    changed_by: str
    changed_by_type: ApiMultiVoucherChangedByType
    voucher_code: str
    status: ApiMultiVoucherStatus
    voucher_amount: int
    voucher_used: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_date = self.created_date.isoformat()

        changed_date = self.changed_date.isoformat()

        changed_by = self.changed_by
        changed_by_type = self.changed_by_type.value

        voucher_code = self.voucher_code
        status = self.status.value

        voucher_amount = self.voucher_amount
        voucher_used = self.voucher_used

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
                "voucherAmount": voucher_amount,
                "voucherUsed": voucher_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_date = isoparse(d.pop("createdDate"))

        changed_date = isoparse(d.pop("changedDate"))

        changed_by = d.pop("changedBy")

        changed_by_type = ApiMultiVoucherChangedByType(d.pop("changedByType"))

        voucher_code = d.pop("voucherCode")

        status = ApiMultiVoucherStatus(d.pop("status"))

        voucher_amount = d.pop("voucherAmount")

        voucher_used = d.pop("voucherUsed")

        api_multi_voucher = cls(
            id=id,
            created_date=created_date,
            changed_date=changed_date,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            voucher_code=voucher_code,
            status=status,
            voucher_amount=voucher_amount,
            voucher_used=voucher_used,
        )

        api_multi_voucher.additional_properties = d
        return api_multi_voucher

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
