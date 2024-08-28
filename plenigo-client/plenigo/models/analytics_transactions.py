import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.analytics_transactions_payment_action import AnalyticsTransactionsPaymentAction
from ..models.analytics_transactions_payment_method import AnalyticsTransactionsPaymentMethod
from ..models.analytics_transactions_payment_status import AnalyticsTransactionsPaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsTransactions")


@_attrs_define
class AnalyticsTransactions:
    """
    Attributes:
        time (Union[None, Unset, datetime.datetime]): time the count is related to with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        amount (Union[Unset, int]): amount of elements for the specified time
        payment_method (Union[Unset, AnalyticsTransactionsPaymentMethod]): type of payment method
        payment_action (Union[Unset, AnalyticsTransactionsPaymentAction]): type of payment action
        payment_status (Union[Unset, AnalyticsTransactionsPaymentStatus]): state of the transaction
    """

    time: Union[None, Unset, datetime.datetime] = UNSET
    amount: Union[Unset, int] = UNSET
    payment_method: Union[Unset, AnalyticsTransactionsPaymentMethod] = UNSET
    payment_action: Union[Unset, AnalyticsTransactionsPaymentAction] = UNSET
    payment_status: Union[Unset, AnalyticsTransactionsPaymentStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[None, Unset, str]
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        amount = self.amount

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        payment_action: Union[Unset, str] = UNSET
        if not isinstance(self.payment_action, Unset):
            payment_action = self.payment_action.value

        payment_status: Union[Unset, str] = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_action is not UNSET:
            field_dict["paymentAction"] = payment_action
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = isoparse(data)

                return time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        time = _parse_time(d.pop("time", UNSET))

        amount = d.pop("amount", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, AnalyticsTransactionsPaymentMethod]
        if isinstance(_payment_method, Unset) or not _payment_method:
            payment_method = UNSET
        else:
            payment_method = AnalyticsTransactionsPaymentMethod(_payment_method)

        _payment_action = d.pop("paymentAction", UNSET)
        payment_action: Union[Unset, AnalyticsTransactionsPaymentAction]
        if isinstance(_payment_action, Unset) or not _payment_action:
            payment_action = UNSET
        else:
            payment_action = AnalyticsTransactionsPaymentAction(_payment_action)

        _payment_status = d.pop("paymentStatus", UNSET)
        payment_status: Union[Unset, AnalyticsTransactionsPaymentStatus]
        if isinstance(_payment_status, Unset) or not _payment_status:
            payment_status = UNSET
        else:
            payment_status = AnalyticsTransactionsPaymentStatus(_payment_status)

        analytics_transactions = cls(
            time=time,
            amount=amount,
            payment_method=payment_method,
            payment_action=payment_action,
            payment_status=payment_status,
        )

        analytics_transactions.additional_properties = d
        return analytics_transactions

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
