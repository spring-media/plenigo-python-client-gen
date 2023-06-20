import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.app_store_subscription_status import AppStoreSubscriptionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStoreSubscription")


@attr.s(auto_attribs=True)
class AppStoreSubscription:
    """
    Attributes:
        app_store_subscription_id (Union[Unset, int]): unique identifier for the app store subscription
        changed_date (Union[Unset, datetime.datetime]): date the transaction was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        chain_id (Union[Unset, int]): all subscriptions that are in one chain because of some rules or cross selling
            share a unique chain id in the context of a company that is identically with the first subscription within the
            chain
        external_system_id (Union[Unset, str]): subscription id from app store
        customer_id (Union[Unset, str]): id of the customer the subscription belongs to
        start_date (Union[Unset, datetime.datetime]): date time the subscription started with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        end_date (Union[Unset, datetime.datetime]): date time the subscription ended with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        cancellation_date (Union[Unset, datetime.datetime]): date time the subscription was cancelled with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        status (Union[Unset, AppStoreSubscriptionStatus]): date time the order was created with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        access_right_unique_id (Union[Unset, str]): unique id of the used access right
    """

    app_store_subscription_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    chain_id: Union[Unset, int] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    cancellation_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, AppStoreSubscriptionStatus] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_store_subscription_id = self.app_store_subscription_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        chain_id = self.chain_id
        external_system_id = self.external_system_id
        customer_id = self.customer_id
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        cancellation_date: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_date, Unset):
            cancellation_date = self.cancellation_date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        access_right_unique_id = self.access_right_unique_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_store_subscription_id is not UNSET:
            field_dict["appStoreSubscriptionId"] = app_store_subscription_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if chain_id is not UNSET:
            field_dict["chainId"] = chain_id
        if external_system_id is not UNSET:
            field_dict["externalSystemId"] = external_system_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if cancellation_date is not UNSET:
            field_dict["cancellationDate"] = cancellation_date
        if status is not UNSET:
            field_dict["status"] = status
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_store_subscription_id = d.pop("appStoreSubscriptionId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        chain_id = d.pop("chainId", UNSET)

        external_system_id = d.pop("externalSystemId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _cancellation_date = d.pop("cancellationDate", UNSET)
        cancellation_date: Union[Unset, datetime.datetime]
        if isinstance(_cancellation_date, Unset):
            cancellation_date = UNSET
        else:
            cancellation_date = isoparse(_cancellation_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppStoreSubscriptionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppStoreSubscriptionStatus(_status)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        app_store_subscription = cls(
            app_store_subscription_id=app_store_subscription_id,
            changed_date=changed_date,
            chain_id=chain_id,
            external_system_id=external_system_id,
            customer_id=customer_id,
            start_date=start_date,
            end_date=end_date,
            cancellation_date=cancellation_date,
            status=status,
            access_right_unique_id=access_right_unique_id,
        )

        app_store_subscription.additional_properties = d
        return app_store_subscription

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
