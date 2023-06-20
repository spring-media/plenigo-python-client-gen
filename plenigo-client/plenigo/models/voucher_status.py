from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voucher_status_status import VoucherStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherStatus")


@attr.s(auto_attribs=True)
class VoucherStatus:
    """
    Attributes:
        plenigo_offer_id (Union[Unset, str]): offer id the voucher code is for
        custom_data (Union[Unset, str]): free text field
        status (Union[Unset, VoucherStatusStatus]): the status of the voucher
    """

    plenigo_offer_id: Union[Unset, str] = UNSET
    custom_data: Union[Unset, str] = UNSET
    status: Union[Unset, VoucherStatusStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plenigo_offer_id = self.plenigo_offer_id
        custom_data = self.custom_data
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        custom_data = d.pop("customData", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, VoucherStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VoucherStatusStatus(_status)

        voucher_status = cls(
            plenigo_offer_id=plenigo_offer_id,
            custom_data=custom_data,
            status=status,
        )

        voucher_status.additional_properties = d
        return voucher_status

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
