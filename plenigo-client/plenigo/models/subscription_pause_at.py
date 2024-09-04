import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_pause_at_pause_type import SubscriptionPauseAtPauseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPauseAt")


@_attrs_define
class SubscriptionPauseAt:
    """
    Attributes:
        start_pause_date (Union[None, datetime.date]): date subscription pause should be start with full-date notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21
        end_pause_date (Union[None, datetime.date]): date subscription pause should be end with full-date notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21
        pause_type (Union[Unset, SubscriptionPauseAtPauseType]): type of the pause
    """

    start_pause_date: Union[None, datetime.date]
    end_pause_date: Union[None, datetime.date]
    pause_type: Union[Unset, SubscriptionPauseAtPauseType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_pause_date: Union[None, str]
        if isinstance(self.start_pause_date, datetime.date):
            start_pause_date = self.start_pause_date.isoformat()
        else:
            start_pause_date = self.start_pause_date

        end_pause_date: Union[None, str]
        if isinstance(self.end_pause_date, datetime.date):
            end_pause_date = self.end_pause_date.isoformat()
        else:
            end_pause_date = self.end_pause_date

        pause_type: Union[Unset, str] = UNSET
        if not isinstance(self.pause_type, Unset):
            pause_type = self.pause_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startPauseDate": start_pause_date,
                "endPauseDate": end_pause_date,
            }
        )
        if pause_type is not UNSET:
            field_dict["pauseType"] = pause_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_start_pause_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_pause_date_type_0 = isoparse(data).date()

                return start_pause_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.date], data)

        start_pause_date = _parse_start_pause_date(d.pop("startPauseDate"))

        def _parse_end_pause_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_pause_date_type_0 = isoparse(data).date()

                return end_pause_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.date], data)

        end_pause_date = _parse_end_pause_date(d.pop("endPauseDate"))

        _pause_type = d.pop("pauseType", UNSET)
        pause_type: Union[Unset, SubscriptionPauseAtPauseType]
        if isinstance(_pause_type, Unset) or not _pause_type:
            pause_type = UNSET
        else:
            pause_type = SubscriptionPauseAtPauseType(_pause_type)

        subscription_pause_at = cls(
            start_pause_date=start_pause_date,
            end_pause_date=end_pause_date,
            pause_type=pause_type,
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
