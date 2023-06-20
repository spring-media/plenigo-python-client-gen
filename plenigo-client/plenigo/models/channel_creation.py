from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelCreation")


@attr.s(auto_attribs=True)
class ChannelCreation:
    """
    Attributes:
        channel_name (Union[Unset, str]): name of the channel
        custom_data (Union[Unset, str]): free text field
        voucher_amount (Union[Unset, int]): represents the amount of vouchers to create for this channel
    """

    channel_name: Union[Unset, str] = UNSET
    custom_data: Union[Unset, str] = UNSET
    voucher_amount: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_name = self.channel_name
        custom_data = self.custom_data
        voucher_amount = self.voucher_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if voucher_amount is not UNSET:
            field_dict["voucherAmount"] = voucher_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_name = d.pop("channelName", UNSET)

        custom_data = d.pop("customData", UNSET)

        voucher_amount = d.pop("voucherAmount", UNSET)

        channel_creation = cls(
            channel_name=channel_name,
            custom_data=custom_data,
            voucher_amount=voucher_amount,
        )

        channel_creation.additional_properties = d
        return channel_creation

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
