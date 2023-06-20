import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="EventListDatesCreation")


@attr.s(auto_attribs=True)
class EventListDatesCreation:
    """
    Attributes:
        title (str): title of the event list date
        event_date (datetime.datetime): date this event date can no longer be processed with full-date notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21
        unique_id (str): unique id of the event list date for identification
        credit_value (int): credit values used by this event
    """

    title: str
    event_date: datetime.datetime
    unique_id: str
    credit_value: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        event_date = self.event_date.isoformat()

        unique_id = self.unique_id
        credit_value = self.credit_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "eventDate": event_date,
                "uniqueId": unique_id,
                "creditValue": credit_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        event_date = isoparse(d.pop("eventDate"))

        unique_id = d.pop("uniqueId")

        credit_value = d.pop("creditValue")

        event_list_dates_creation = cls(
            title=title,
            event_date=event_date,
            unique_id=unique_id,
            credit_value=credit_value,
        )

        event_list_dates_creation.additional_properties = d
        return event_list_dates_creation

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
