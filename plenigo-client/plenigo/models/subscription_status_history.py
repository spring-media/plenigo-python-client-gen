import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_status_history_new_status import SubscriptionStatusHistoryNewStatus
from ..models.subscription_status_history_old_status import SubscriptionStatusHistoryOldStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionStatusHistory")


@_attrs_define
class SubscriptionStatusHistory:
    """
    Attributes:
        status_change_id (Union[Unset, int]): unique id of the subscription status in the context of a contract company
        customer_id (Union[Unset, str]): unique id of the customer
        start_time (Union[None, Unset, datetime.datetime]): time the status started with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        end_time (Union[None, Unset, datetime.datetime]): time this status ended with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        chain_id (Union[Unset, int]): all subscriptions that are in one chain because of some rules or cross selling
            share a unique chain id in the context of a contract company that is identically with the first subscription
            within the chain
        old_status (Union[Unset, SubscriptionStatusHistoryOldStatus]): old status
        new_status (Union[Unset, SubscriptionStatusHistoryNewStatus]): current status
    """

    status_change_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, str] = UNSET
    start_time: Union[None, Unset, datetime.datetime] = UNSET
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    chain_id: Union[Unset, int] = UNSET
    old_status: Union[Unset, SubscriptionStatusHistoryOldStatus] = UNSET
    new_status: Union[Unset, SubscriptionStatusHistoryNewStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_change_id = self.status_change_id

        customer_id = self.customer_id

        start_time: Union[None, Unset, str]
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        chain_id = self.chain_id

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
        if chain_id is not UNSET:
            field_dict["chainId"] = chain_id
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

        def _parse_start_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        chain_id = d.pop("chainId", UNSET)

        _old_status = d.pop("oldStatus", UNSET)
        old_status: Union[Unset, SubscriptionStatusHistoryOldStatus]
        if isinstance(_old_status, Unset):
            old_status = UNSET
        else:
            old_status = SubscriptionStatusHistoryOldStatus(_old_status)

        _new_status = d.pop("newStatus", UNSET)
        new_status: Union[Unset, SubscriptionStatusHistoryNewStatus]
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = SubscriptionStatusHistoryNewStatus(_new_status)

        subscription_status_history = cls(
            status_change_id=status_change_id,
            customer_id=customer_id,
            start_time=start_time,
            end_time=end_time,
            chain_id=chain_id,
            old_status=old_status,
            new_status=new_status,
        )

        subscription_status_history.additional_properties = d
        return subscription_status_history

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
