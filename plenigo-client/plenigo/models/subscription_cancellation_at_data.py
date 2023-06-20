import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionCancellationAtData")


@attr.s(auto_attribs=True)
class SubscriptionCancellationAtData:
    """
    Attributes:
        cancellation_date (Union[Unset, datetime.date]): date subscription should end with full-date notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21
    """

    cancellation_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cancellation_date: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_date, Unset):
            cancellation_date = self.cancellation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancellation_date is not UNSET:
            field_dict["cancellationDate"] = cancellation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _cancellation_date = d.pop("cancellationDate", UNSET)
        cancellation_date: Union[Unset, datetime.date]
        if isinstance(_cancellation_date, Unset):
            cancellation_date = UNSET
        else:
            cancellation_date = isoparse(_cancellation_date).date()

        subscription_cancellation_at_data = cls(
            cancellation_date=cancellation_date,
        )

        subscription_cancellation_at_data.additional_properties = d
        return subscription_cancellation_at_data

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
