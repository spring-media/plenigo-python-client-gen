import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsRevenue")


@attr.s(auto_attribs=True)
class AnalyticsRevenue:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]): time the count is related to with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        sum_ (Union[Unset, float]): sum of revenues
        currency (Union[Unset, str]): currency of the subscription formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO 4217, alphabetic code</a>
    """

    time: Union[Unset, datetime.datetime] = UNSET
    sum_: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        sum_ = self.sum_
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        sum_ = d.pop("sum", UNSET)

        currency = d.pop("currency", UNSET)

        analytics_revenue = cls(
            time=time,
            sum_=sum_,
            currency=currency,
        )

        analytics_revenue.additional_properties = d
        return analytics_revenue

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
