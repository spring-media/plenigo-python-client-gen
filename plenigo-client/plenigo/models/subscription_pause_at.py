import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SubscriptionPauseAt")


@attr.s(auto_attribs=True)
class SubscriptionPauseAt:
    """
    Attributes:
        start_pause_date (datetime.date): date subscription pause should be start with full-date notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21
        end_pause_date (datetime.date): date subscription pause should be end with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
    """

    start_pause_date: datetime.date
    end_pause_date: datetime.date
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_pause_date = self.start_pause_date.isoformat()
        end_pause_date = self.end_pause_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startPauseDate": start_pause_date,
                "endPauseDate": end_pause_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_pause_date = isoparse(d.pop("startPauseDate")).date()

        end_pause_date = isoparse(d.pop("endPauseDate")).date()

        subscription_pause_at = cls(
            start_pause_date=start_pause_date,
            end_pause_date=end_pause_date,
        )

        subscription_pause_at.additional_properties = d
        return subscription_pause_at

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
