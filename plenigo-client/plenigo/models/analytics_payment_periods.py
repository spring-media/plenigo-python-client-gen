import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.analytics_payment_periods_failure_reason import AnalyticsPaymentPeriodsFailureReason
from ..models.analytics_payment_periods_payment_method import AnalyticsPaymentPeriodsPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsPaymentPeriods")


@attr.s(auto_attribs=True)
class AnalyticsPaymentPeriods:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]): time the count is related to with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        amount (Union[Unset, int]): amount of elements for the specified time
        payment_method (Union[Unset, AnalyticsPaymentPeriodsPaymentMethod]): type of payment method
        success (Union[Unset, bool]): flag indicating if transaction was a success or a failure
        failure_reason (Union[Unset, AnalyticsPaymentPeriodsFailureReason]): initial reason for the failed payment
            periods
    """

    time: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, int] = UNSET
    payment_method: Union[Unset, AnalyticsPaymentPeriodsPaymentMethod] = UNSET
    success: Union[Unset, bool] = UNSET
    failure_reason: Union[Unset, AnalyticsPaymentPeriodsFailureReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        amount = self.amount
        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        success = self.success
        failure_reason: Union[Unset, str] = UNSET
        if not isinstance(self.failure_reason, Unset):
            failure_reason = self.failure_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if success is not UNSET:
            field_dict["success"] = success
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        amount = d.pop("amount", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, AnalyticsPaymentPeriodsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = AnalyticsPaymentPeriodsPaymentMethod(_payment_method)

        success = d.pop("success", UNSET)

        _failure_reason = d.pop("failureReason", UNSET)
        failure_reason: Union[Unset, AnalyticsPaymentPeriodsFailureReason]
        if isinstance(_failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = AnalyticsPaymentPeriodsFailureReason(_failure_reason)

        analytics_payment_periods = cls(
            time=time,
            amount=amount,
            payment_method=payment_method,
            success=success,
            failure_reason=failure_reason,
        )

        analytics_payment_periods.additional_properties = d
        return analytics_payment_periods

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
