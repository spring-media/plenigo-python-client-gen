import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.opt_in_status import OptInStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptIn")


@attr.s(auto_attribs=True)
class OptIn:
    """
    Attributes:
        opt_in_id (Union[Unset, int]): technical id of the opt in for relation to the merchant backend opt in id
        unique_id (Union[Unset, str]): unique id of the last active opt in
        changed_date (Union[Unset, datetime.datetime]): date time the opt in was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        status (Union[Unset, OptInStatus]): status of the opt in
    """

    opt_in_id: Union[Unset, int] = UNSET
    unique_id: Union[Unset, str] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, OptInStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opt_in_id = self.opt_in_id
        unique_id = self.unique_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opt_in_id is not UNSET:
            field_dict["optInId"] = opt_in_id
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        opt_in_id = d.pop("optInId", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OptInStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OptInStatus(_status)

        opt_in = cls(
            opt_in_id=opt_in_id,
            unique_id=unique_id,
            changed_date=changed_date,
            status=status,
        )

        opt_in.additional_properties = d
        return opt_in

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
