import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_creation_data import AccessRightItemCreationData


T = TypeVar("T", bound="AccessRightItemCreation")


@_attrs_define
class AccessRightItemCreation:
    """
    Attributes:
        life_time_start (Union[None, Unset, datetime.datetime]): date the access right will start with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        life_time_end (Union[None, Unset, datetime.datetime]): date the access right will end with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        access_time_start (Union[None, Unset, datetime.datetime]): time the access right will start with time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 17:32:28
        access_time_end (Union[None, Unset, datetime.datetime]): time the access right will end with time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 17:32:28
        max_cache_date (Union[None, Unset, datetime.datetime]): max cache date with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        data (Union[Unset, AccessRightItemCreationData]):
        blocked (Union[Unset, bool]): flag indicating if access is blocked
    """

    life_time_start: Union[None, Unset, datetime.datetime] = UNSET
    life_time_end: Union[None, Unset, datetime.datetime] = UNSET
    access_time_start: Union[None, Unset, datetime.datetime] = UNSET
    access_time_end: Union[None, Unset, datetime.datetime] = UNSET
    max_cache_date: Union[None, Unset, datetime.datetime] = UNSET
    data: Union[Unset, "AccessRightItemCreationData"] = UNSET
    blocked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        life_time_start: Union[None, Unset, str]
        if isinstance(self.life_time_start, Unset) or self.life_time_start is None:
            life_time_start = UNSET
        elif isinstance(self.life_time_start, datetime.datetime):
            life_time_start = self.life_time_start.isoformat()
        else:
            life_time_start = self.life_time_start

        life_time_end: Union[None, Unset, str]
        if isinstance(self.life_time_end, Unset) or self.life_time_end is None:
            life_time_end = UNSET
        elif isinstance(self.life_time_end, datetime.datetime):
            life_time_end = self.life_time_end.isoformat()
        else:
            life_time_end = self.life_time_end

        access_time_start: Union[None, Unset, str]
        if isinstance(self.access_time_start, Unset) or self.access_time_start is None:
            access_time_start = UNSET
        elif isinstance(self.access_time_start, datetime.datetime):
            access_time_start = self.access_time_start.isoformat()
        else:
            access_time_start = self.access_time_start

        access_time_end: Union[None, Unset, str]
        if isinstance(self.access_time_end, Unset) or self.access_time_end is None:
            access_time_end = UNSET
        elif isinstance(self.access_time_end, datetime.datetime):
            access_time_end = self.access_time_end.isoformat()
        else:
            access_time_end = self.access_time_end

        max_cache_date: Union[None, Unset, str]
        if isinstance(self.max_cache_date, Unset) or self.max_cache_date is None:
            max_cache_date = UNSET
        elif isinstance(self.max_cache_date, datetime.datetime):
            max_cache_date = self.max_cache_date.isoformat()
        else:
            max_cache_date = self.max_cache_date

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

        def _parse_life_time_start(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                life_time_start_type_1 = isoparse(data)

                return life_time_start_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        life_time_start = _parse_life_time_start(d.pop("lifeTimeStart", UNSET))

        def _parse_life_time_end(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                life_time_end_type_1 = isoparse(data)

                return life_time_end_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        life_time_end = _parse_life_time_end(d.pop("lifeTimeEnd", UNSET))

        def _parse_access_time_start(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_time_start_type_1 = isoparse(data)

                return access_time_start_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        access_time_start = _parse_access_time_start(d.pop("accessTimeStart", UNSET))

        def _parse_access_time_end(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_time_end_type_1 = isoparse(data)

                return access_time_end_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        access_time_end = _parse_access_time_end(d.pop("accessTimeEnd", UNSET))

        def _parse_max_cache_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_cache_date_type_1 = isoparse(data)

                return max_cache_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        max_cache_date = _parse_max_cache_date(d.pop("maxCacheDate", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, AccessRightItemCreationData]
        if isinstance(_data, Unset) or not _data:
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
