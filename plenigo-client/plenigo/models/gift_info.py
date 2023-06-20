from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftInfo")


@attr.s(auto_attribs=True)
class GiftInfo:
    """
    Attributes:
        notify_giftee (Union[Unset, bool]): flag indicating if giftee should be notified about the gift
        donor_text (Union[Unset, str]): personal text of the donor to the giftee
        giftee_email (Union[Unset, str]): email address of the giftee
    """

    notify_giftee: Union[Unset, bool] = UNSET
    donor_text: Union[Unset, str] = UNSET
    giftee_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notify_giftee = self.notify_giftee
        donor_text = self.donor_text
        giftee_email = self.giftee_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notify_giftee is not UNSET:
            field_dict["notifyGiftee"] = notify_giftee
        if donor_text is not UNSET:
            field_dict["donorText"] = donor_text
        if giftee_email is not UNSET:
            field_dict["gifteeEmail"] = giftee_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notify_giftee = d.pop("notifyGiftee", UNSET)

        donor_text = d.pop("donorText", UNSET)

        giftee_email = d.pop("gifteeEmail", UNSET)

        gift_info = cls(
            notify_giftee=notify_giftee,
            donor_text=donor_text,
            giftee_email=giftee_email,
        )

        gift_info.additional_properties = d
        return gift_info

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
