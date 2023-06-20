import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.customer_status_new_status import CustomerStatusNewStatus
from ..models.customer_status_old_status import CustomerStatusOldStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerStatus")


@attr.s(auto_attribs=True)
class CustomerStatus:
    """
    Attributes:
        status_change_id (Union[Unset, int]): unique id of the customer status in the context of a contract company
        customer_id (Union[Unset, str]): unique id of the customer
        start_time (Union[Unset, datetime.datetime]): time the status started with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        end_time (Union[Unset, datetime.datetime]): time this status ended with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        old_status (Union[Unset, CustomerStatusOldStatus]): old status
        new_status (Union[Unset, CustomerStatusNewStatus]): current status
    """

    status_change_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    old_status: Union[Unset, CustomerStatusOldStatus] = UNSET
    new_status: Union[Unset, CustomerStatusNewStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_change_id = self.status_change_id
        customer_id = self.customer_id
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        old_status: Union[Unset, str] = UNSET
        if not isinstance(self.old_status, Unset):
            old_status = self.old_status.value

        new_status: Union[Unset, str] = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_change_id is not UNSET:
            field_dict["statusChangeId"] = status_change_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if old_status is not UNSET:
            field_dict["oldStatus"] = old_status
        if new_status is not UNSET:
            field_dict["newStatus"] = new_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_change_id = d.pop("statusChangeId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _old_status = d.pop("oldStatus", UNSET)
        old_status: Union[Unset, CustomerStatusOldStatus]
        if isinstance(_old_status, Unset):
            old_status = UNSET
        else:
            old_status = CustomerStatusOldStatus(_old_status)

        _new_status = d.pop("newStatus", UNSET)
        new_status: Union[Unset, CustomerStatusNewStatus]
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = CustomerStatusNewStatus(_new_status)

        customer_status = cls(
            status_change_id=status_change_id,
            customer_id=customer_id,
            start_time=start_time,
            end_time=end_time,
            old_status=old_status,
            new_status=new_status,
        )

        customer_status.additional_properties = d
        return customer_status

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
