import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_payment_period_failure_reason import SubscriptionPaymentPeriodFailureReason
from ..models.subscription_payment_period_payment_method import SubscriptionPaymentPeriodPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPaymentPeriod")


@_attrs_define
class SubscriptionPaymentPeriod:
    """
    Attributes:
        subscription_id (int): unique id of the subscription in the context of a contract company
        customer_id (str): unique id of the customer
        start_time (Union[None, datetime.datetime]): start date time of the subscription with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        end_time (Union[None, datetime.datetime]): end date time of the subscription with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        success (Union[Unset, bool]): flag indicating if payment for subscription in period was successful
        access_blocked (Union[Unset, bool]): flag indicating if access is blocked in payment period
        access_blocked_in_period (Union[Unset, bool]): flag indicating if access was blocked during some period in
            payment period - this could be a reason for a later booking date
        booking_tries (Union[Unset, int]): tries done before booking period was successful or no more booking tries were
            done
        plenigo_transaction_id (Union[Unset, str]): unique plenigo transaction id used to communicate with payment
            provider
        payment_method (Union[Unset, SubscriptionPaymentPeriodPaymentMethod]): type of payment method
        failure_reason (Union[Unset, SubscriptionPaymentPeriodFailureReason]): initial reason for the failed payment
            periods
    """

    subscription_id: int
    customer_id: str
    start_time: Union[None, datetime.datetime]
    end_time: Union[None, datetime.datetime]
    success: Union[Unset, bool] = UNSET
    access_blocked: Union[Unset, bool] = UNSET
    access_blocked_in_period: Union[Unset, bool] = UNSET
    booking_tries: Union[Unset, int] = UNSET
    plenigo_transaction_id: Union[Unset, str] = UNSET
    payment_method: Union[Unset, SubscriptionPaymentPeriodPaymentMethod] = UNSET
    failure_reason: Union[Unset, SubscriptionPaymentPeriodFailureReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_id = self.subscription_id

        customer_id = self.customer_id

        start_time: Union[None, str]
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: Union[None, str]
        if isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        success = self.success

        access_blocked = self.access_blocked

        access_blocked_in_period = self.access_blocked_in_period

        booking_tries = self.booking_tries

        plenigo_transaction_id = self.plenigo_transaction_id

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        failure_reason: Union[Unset, str] = UNSET
        if not isinstance(self.failure_reason, Unset):
            failure_reason = self.failure_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "customerId": customer_id,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if access_blocked is not UNSET:
            field_dict["accessBlocked"] = access_blocked
        if access_blocked_in_period is not UNSET:
            field_dict["accessBlockedInPeriod"] = access_blocked_in_period
        if booking_tries is not UNSET:
            field_dict["bookingTries"] = booking_tries
        if plenigo_transaction_id is not UNSET:
            field_dict["plenigoTransactionId"] = plenigo_transaction_id
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_id = d.pop("subscriptionId")

        customer_id = d.pop("customerId")

        def _parse_start_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_1 = isoparse(data)

                return start_time_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("startTime"))

        def _parse_end_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_1 = isoparse(data)

                return end_time_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime"))

        success = d.pop("success", UNSET)

        access_blocked = d.pop("accessBlocked", UNSET)

        access_blocked_in_period = d.pop("accessBlockedInPeriod", UNSET)

        booking_tries = d.pop("bookingTries", UNSET)

        plenigo_transaction_id = d.pop("plenigoTransactionId", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, SubscriptionPaymentPeriodPaymentMethod]
        if isinstance(_payment_method, Unset) or not _payment_method:
            payment_method = UNSET
        else:
            payment_method = SubscriptionPaymentPeriodPaymentMethod(_payment_method)

        _failure_reason = d.pop("failureReason", UNSET)
        failure_reason: Union[Unset, SubscriptionPaymentPeriodFailureReason]
        if isinstance(_failure_reason, Unset) or not _failure_reason:
            failure_reason = UNSET
        else:
            failure_reason = SubscriptionPaymentPeriodFailureReason(_failure_reason)

        subscription_payment_period = cls(
            subscription_id=subscription_id,
            customer_id=customer_id,
            start_time=start_time,
            end_time=end_time,
            success=success,
            access_blocked=access_blocked,
            access_blocked_in_period=access_blocked_in_period,
            booking_tries=booking_tries,
            plenigo_transaction_id=plenigo_transaction_id,
            payment_method=payment_method,
            failure_reason=failure_reason,
        )

        subscription_payment_period.additional_properties = d
        return subscription_payment_period

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
