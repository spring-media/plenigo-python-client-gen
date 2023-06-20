import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.refund_payment_method import RefundPaymentMethod
from ..models.refund_payment_provider import RefundPaymentProvider
from ..models.refund_status import RefundStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refund_status_change import RefundStatusChange


T = TypeVar("T", bound="Refund")


@attr.s(auto_attribs=True)
class Refund:
    """
    Attributes:
        refund_id (int): unique id of the refund also used for pagination
        changed_date (datetime.datetime): date the refund was changed with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        customer_id (str): unique id of the customer the refund is related to
        amount (float): amount of the refund
        currency (str): currency of the refund formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (RefundPaymentMethod): payment method used
        status (RefundStatus): status of the refund
        payment_provider (Union[Unset, RefundPaymentProvider]): payment provider used for refund execution
        cancellation_invoice_id (Union[Unset, int]): unique id of the cancellation also used for pagination
        transaction_id (Union[Unset, str]): unique id of the transaction also used for pagination
        psp_transaction_id (Union[Unset, str]): id of the payment service provider if one was provided
        status_history (Union[Unset, List['RefundStatusChange']]):
    """

    refund_id: int
    changed_date: datetime.datetime
    customer_id: str
    amount: float
    currency: str
    payment_method: RefundPaymentMethod
    status: RefundStatus
    payment_provider: Union[Unset, RefundPaymentProvider] = UNSET
    cancellation_invoice_id: Union[Unset, int] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    psp_transaction_id: Union[Unset, str] = UNSET
    status_history: Union[Unset, List["RefundStatusChange"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refund_id = self.refund_id
        changed_date = self.changed_date.isoformat()

        customer_id = self.customer_id
        amount = self.amount
        currency = self.currency
        payment_method = self.payment_method.value

        status = self.status.value

        payment_provider: Union[Unset, str] = UNSET
        if not isinstance(self.payment_provider, Unset):
            payment_provider = self.payment_provider.value

        cancellation_invoice_id = self.cancellation_invoice_id
        transaction_id = self.transaction_id
        psp_transaction_id = self.psp_transaction_id
        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for status_history_item_data in self.status_history:
                status_history_item = status_history_item_data.to_dict()

                status_history.append(status_history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refundId": refund_id,
                "changedDate": changed_date,
                "customerId": customer_id,
                "amount": amount,
                "currency": currency,
                "paymentMethod": payment_method,
                "status": status,
            }
        )
        if payment_provider is not UNSET:
            field_dict["paymentProvider"] = payment_provider
        if cancellation_invoice_id is not UNSET:
            field_dict["cancellationInvoiceId"] = cancellation_invoice_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if psp_transaction_id is not UNSET:
            field_dict["pspTransactionId"] = psp_transaction_id
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.refund_status_change import RefundStatusChange

        d = src_dict.copy()
        refund_id = d.pop("refundId")

        changed_date = isoparse(d.pop("changedDate"))

        customer_id = d.pop("customerId")

        amount = d.pop("amount")

        currency = d.pop("currency")

        payment_method = RefundPaymentMethod(d.pop("paymentMethod"))

        status = RefundStatus(d.pop("status"))

        _payment_provider = d.pop("paymentProvider", UNSET)
        payment_provider: Union[Unset, RefundPaymentProvider]
        if isinstance(_payment_provider, Unset):
            payment_provider = UNSET
        else:
            payment_provider = RefundPaymentProvider(_payment_provider)

        cancellation_invoice_id = d.pop("cancellationInvoiceId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        psp_transaction_id = d.pop("pspTransactionId", UNSET)

        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for status_history_item_data in _status_history or []:
            status_history_item = RefundStatusChange.from_dict(status_history_item_data)

            status_history.append(status_history_item)

        refund = cls(
            refund_id=refund_id,
            changed_date=changed_date,
            customer_id=customer_id,
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            status=status,
            payment_provider=payment_provider,
            cancellation_invoice_id=cancellation_invoice_id,
            transaction_id=transaction_id,
            psp_transaction_id=psp_transaction_id,
            status_history=status_history,
        )

        refund.additional_properties = d
        return refund

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
