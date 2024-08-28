import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherPurchaseData")


@_attrs_define
class VoucherPurchaseData:
    """
    Attributes:
        voucher_template_id (int): id fo the voucher template associated with this voucher item purchase
        voucher_end_date (Union[None, datetime.datetime]): validity time of voucher with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        voucher_code (Union[Unset, str]): voucher code created with this voucher item purchase
    """

    voucher_template_id: int
    voucher_end_date: Union[None, datetime.datetime]
    voucher_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voucher_template_id = self.voucher_template_id

        voucher_end_date: Union[None, str]
        if isinstance(self.voucher_end_date, datetime.datetime):
            voucher_end_date = self.voucher_end_date.isoformat()
        else:
            voucher_end_date = self.voucher_end_date

        voucher_code = self.voucher_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voucherTemplateId": voucher_template_id,
                "voucherEndDate": voucher_end_date,
            }
        )
        if voucher_code is not UNSET:
            field_dict["voucherCode"] = voucher_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        voucher_template_id = d.pop("voucherTemplateId")

        def _parse_voucher_end_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voucher_end_date_type_0 = isoparse(data)

                return voucher_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        voucher_end_date = _parse_voucher_end_date(d.pop("voucherEndDate"))

        voucher_code = d.pop("voucherCode", UNSET)

        voucher_purchase_data = cls(
            voucher_template_id=voucher_template_id,
            voucher_end_date=voucher_end_date,
            voucher_code=voucher_code,
        )

        voucher_purchase_data.additional_properties = d
        return voucher_purchase_data

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
