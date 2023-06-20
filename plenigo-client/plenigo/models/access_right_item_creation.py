import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_creation_data import AccessRightItemCreationData


T = TypeVar("T", bound="AccessRightItemCreation")


@attr.s(auto_attribs=True)
class AccessRightItemCreation:
    """
    Attributes:
        life_time_start (Union[Unset, datetime.datetime]): date the access right will start with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        life_time_end (Union[Unset, datetime.datetime]): date the access right will end with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        access_time_start (Union[Unset, datetime.datetime]): time the access right will start with time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 17:32:28
        access_time_end (Union[Unset, datetime.datetime]): time the access right will end with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        max_cache_date (Union[Unset, datetime.datetime]): max cache date with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        data (Union[Unset, AccessRightItemCreationData]):
        blocked (Union[Unset, bool]): flag indicating if access is blocked
    """

    life_time_start: Union[Unset, datetime.datetime] = UNSET
    life_time_end: Union[Unset, datetime.datetime] = UNSET
    access_time_start: Union[Unset, datetime.datetime] = UNSET
    access_time_end: Union[Unset, datetime.datetime] = UNSET
    max_cache_date: Union[Unset, datetime.datetime] = UNSET
    data: Union[Unset, "AccessRightItemCreationData"] = UNSET
    blocked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        life_time_start: Union[Unset, str] = UNSET
        if not isinstance(self.life_time_start, Unset):
            life_time_start = self.life_time_start.isoformat()

        life_time_end: Union[Unset, str] = UNSET
        if not isinstance(self.life_time_end, Unset):
            life_time_end = self.life_time_end.isoformat()

        access_time_start: Union[Unset, str] = UNSET
        if not isinstance(self.access_time_start, Unset):
            access_time_start = self.access_time_start.isoformat()

        access_time_end: Union[Unset, str] = UNSET
        if not isinstance(self.access_time_end, Unset):
            access_time_end = self.access_time_end.isoformat()

        max_cache_date: Union[Unset, str] = UNSET
        if not isinstance(self.max_cache_date, Unset):
            max_cache_date = self.max_cache_date.isoformat()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        blocked = self.blocked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if life_time_start is not UNSET:
            field_dict["lifeTimeStart"] = life_time_start
        if life_time_end is not UNSET:
            field_dict["lifeTimeEnd"] = life_time_end
        if access_time_start is not UNSET:
            field_dict["accessTimeStart"] = access_time_start
        if access_time_end is not UNSET:
            field_dict["accessTimeEnd"] = access_time_end
        if max_cache_date is not UNSET:
            field_dict["maxCacheDate"] = max_cache_date
        if data is not UNSET:
            field_dict["data"] = data
        if blocked is not UNSET:
            field_dict["blocked"] = blocked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_right_item_creation_data import AccessRightItemCreationData

        d = src_dict.copy()
        _life_time_start = d.pop("lifeTimeStart", UNSET)
        life_time_start: Union[Unset, datetime.datetime]
        if isinstance(_life_time_start, Unset):
            life_time_start = UNSET
        else:
            life_time_start = isoparse(_life_time_start)

        _life_time_end = d.pop("lifeTimeEnd", UNSET)
        life_time_end: Union[Unset, datetime.datetime]
        if isinstance(_life_time_end, Unset):
            life_time_end = UNSET
        else:
            life_time_end = isoparse(_life_time_end)

        _access_time_start = d.pop("accessTimeStart", UNSET)
        access_time_start: Union[Unset, datetime.datetime]
        if isinstance(_access_time_start, Unset):
            access_time_start = UNSET
        else:
            access_time_start = isoparse(_access_time_start)

        _access_time_end = d.pop("accessTimeEnd", UNSET)
        access_time_end: Union[Unset, datetime.datetime]
        if isinstance(_access_time_end, Unset):
            access_time_end = UNSET
        else:
            access_time_end = isoparse(_access_time_end)

        _max_cache_date = d.pop("maxCacheDate", UNSET)
        max_cache_date: Union[Unset, datetime.datetime]
        if isinstance(_max_cache_date, Unset):
            max_cache_date = UNSET
        else:
            max_cache_date = isoparse(_max_cache_date)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AccessRightItemCreationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AccessRightItemCreationData.from_dict(_data)

        blocked = d.pop("blocked", UNSET)

        access_right_item_creation = cls(
            life_time_start=life_time_start,
            life_time_end=life_time_end,
            access_time_start=access_time_start,
            access_time_end=access_time_end,
            max_cache_date=max_cache_date,
            data=data,
            blocked=blocked,
        )

        access_right_item_creation.additional_properties = d
        return access_right_item_creation

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
