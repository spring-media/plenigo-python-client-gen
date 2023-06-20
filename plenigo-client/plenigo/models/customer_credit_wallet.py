import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.customer_credit_wallet_credit_validity_timespan import CustomerCreditWalletCreditValidityTimespan
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerCreditWallet")


@attr.s(auto_attribs=True)
class CustomerCreditWallet:
    """
    Attributes:
        unique_id (Union[Unset, str]): unique id of the wallet for identification
        title (Union[Unset, str]): title of the customer wallet
        available_credit_count (Union[Unset, int]): available credit count to use
        credit_count_invalidation (Union[Unset, bool]): flag indicating if credit counts will be invalidated after a
            time if no active subscription is associated
        credit_validity_time (Union[Unset, int]): time credits are invalidated if credit count invalidation is active
        credit_validity_timespan (Union[Unset, CustomerCreditWalletCreditValidityTimespan]): time credit validity
            timespan
        credit_validity_time_start (Union[Unset, datetime.datetime]): date time the credit validity starts in date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        customer_credit_wallet_id (Union[Unset, int]): unique id of a customer credit wallet within a contract company
        customer_id (Union[Unset, str]): unique id of the customer the credit wallet belongs to
    """

    unique_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    available_credit_count: Union[Unset, int] = UNSET
    credit_count_invalidation: Union[Unset, bool] = UNSET
    credit_validity_time: Union[Unset, int] = UNSET
    credit_validity_timespan: Union[Unset, CustomerCreditWalletCreditValidityTimespan] = UNSET
    credit_validity_time_start: Union[Unset, datetime.datetime] = UNSET
    customer_credit_wallet_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_id = self.unique_id
        title = self.title
        available_credit_count = self.available_credit_count
        credit_count_invalidation = self.credit_count_invalidation
        credit_validity_time = self.credit_validity_time
        credit_validity_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.credit_validity_timespan, Unset):
            credit_validity_timespan = self.credit_validity_timespan.value

        credit_validity_time_start: Union[Unset, str] = UNSET
        if not isinstance(self.credit_validity_time_start, Unset):
            credit_validity_time_start = self.credit_validity_time_start.isoformat()

        customer_credit_wallet_id = self.customer_credit_wallet_id
        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if title is not UNSET:
            field_dict["title"] = title
        if available_credit_count is not UNSET:
            field_dict["availableCreditCount"] = available_credit_count
        if credit_count_invalidation is not UNSET:
            field_dict["creditCountInvalidation"] = credit_count_invalidation
        if credit_validity_time is not UNSET:
            field_dict["creditValidityTime"] = credit_validity_time
        if credit_validity_timespan is not UNSET:
            field_dict["creditValidityTimespan"] = credit_validity_timespan
        if credit_validity_time_start is not UNSET:
            field_dict["creditValidityTimeStart"] = credit_validity_time_start
        if customer_credit_wallet_id is not UNSET:
            field_dict["customerCreditWalletId"] = customer_credit_wallet_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_id = d.pop("uniqueId", UNSET)

        title = d.pop("title", UNSET)

        available_credit_count = d.pop("availableCreditCount", UNSET)

        credit_count_invalidation = d.pop("creditCountInvalidation", UNSET)

        credit_validity_time = d.pop("creditValidityTime", UNSET)

        _credit_validity_timespan = d.pop("creditValidityTimespan", UNSET)
        credit_validity_timespan: Union[Unset, CustomerCreditWalletCreditValidityTimespan]
        if isinstance(_credit_validity_timespan, Unset):
            credit_validity_timespan = UNSET
        else:
            credit_validity_timespan = CustomerCreditWalletCreditValidityTimespan(_credit_validity_timespan)

        _credit_validity_time_start = d.pop("creditValidityTimeStart", UNSET)
        credit_validity_time_start: Union[Unset, datetime.datetime]
        if isinstance(_credit_validity_time_start, Unset):
            credit_validity_time_start = UNSET
        else:
            credit_validity_time_start = isoparse(_credit_validity_time_start)

        customer_credit_wallet_id = d.pop("customerCreditWalletId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        customer_credit_wallet = cls(
            unique_id=unique_id,
            title=title,
            available_credit_count=available_credit_count,
            credit_count_invalidation=credit_count_invalidation,
            credit_validity_time=credit_validity_time,
            credit_validity_timespan=credit_validity_timespan,
            credit_validity_time_start=credit_validity_time_start,
            customer_credit_wallet_id=customer_credit_wallet_id,
            customer_id=customer_id,
        )

        customer_credit_wallet.additional_properties = d
        return customer_credit_wallet

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
