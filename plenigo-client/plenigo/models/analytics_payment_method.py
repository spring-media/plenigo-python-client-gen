import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.analytics_payment_method_payment_method import AnalyticsPaymentMethodPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsPaymentMethod")


@_attrs_define
class AnalyticsPaymentMethod:
    """
    Attributes:
        time (Union[None, Unset, datetime.datetime]): time the count is related to with date-time notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        payment_method (Union[Unset, AnalyticsPaymentMethodPaymentMethod]): type of payment method
        amount (Union[Unset, int]): amount of elements for the specified time
    """

    time: Union[None, Unset, datetime.datetime] = UNSET
    payment_method: Union[Unset, AnalyticsPaymentMethodPaymentMethod] = UNSET
    amount: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[None, Unset, str]
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if amount is not UNSET:
            field_dict["amount"] = amount

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

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, AnalyticsPaymentMethodPaymentMethod]
        if isinstance(_payment_method, Unset) or not _payment_method:
            payment_method = UNSET
        else:
            payment_method = AnalyticsPaymentMethodPaymentMethod(_payment_method)

        amount = d.pop("amount", UNSET)

        analytics_payment_method = cls(
            time=time,
            payment_method=payment_method,
            amount=amount,
        )

        analytics_payment_method.additional_properties = d
        return analytics_payment_method

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
