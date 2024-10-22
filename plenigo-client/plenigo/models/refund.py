import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.refund_payment_method import RefundPaymentMethod
from ..models.refund_payment_provider import RefundPaymentProvider
from ..models.refund_status import RefundStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schemas_status_history import SchemasStatusHistory


T = TypeVar("T", bound="Refund")


@_attrs_define
class Refund:
    """
    Attributes:
        refund_id (int): unique id of the refund also used for pagination
        customer_id (str): unique id of the customer the refund is related to
        amount (float): amount of the refund
        currency (str): currency of the refund formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (RefundPaymentMethod): payment method used
        status (RefundStatus): status of the refund
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        payment_provider (Union[Unset, RefundPaymentProvider]): payment provider used for refund execution
        cancellation_invoice_id (Union[Unset, int]): unique id of the cancellation also used for pagination
        transaction_id (Union[Unset, str]): unique id of the transaction also used for pagination
        psp_transaction_id (Union[Unset, str]): id of the payment service provider if one was provided
        status_history (Union[Unset, List['SchemasStatusHistory']]):
    """

    refund_id: int
    customer_id: str
    amount: float
    currency: str
    payment_method: RefundPaymentMethod
    status: RefundStatus
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    payment_provider: Union[Unset, RefundPaymentProvider] = UNSET
    cancellation_invoice_id: Union[Unset, int] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    psp_transaction_id: Union[Unset, str] = UNSET
    status_history: Union[Unset, List["SchemasStatusHistory"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refund_id = self.refund_id

        customer_id = self.customer_id

        amount = self.amount

        currency = self.currency

        payment_method = self.payment_method.value

        status = self.status.value

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

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
                "customerId": customer_id,
                "amount": amount,
                "currency": currency,
                "paymentMethod": payment_method,
                "status": status,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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
        from ..models.schemas_status_history import SchemasStatusHistory

        d = src_dict.copy()
        refund_id = d.pop("refundId")

        customer_id = d.pop("customerId")

        amount = d.pop("amount")

        currency = d.pop("currency")

        payment_method = RefundPaymentMethod(d.pop("paymentMethod"))

        status = RefundStatus(d.pop("status"))

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_1 = isoparse(data)

                return created_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        _payment_provider = d.pop("paymentProvider", UNSET)
        payment_provider: Union[Unset, RefundPaymentProvider]
        if isinstance(_payment_provider, Unset) or not _payment_provider:
            payment_provider = UNSET
        else:
            payment_provider = RefundPaymentProvider(_payment_provider)

        cancellation_invoice_id = d.pop("cancellationInvoiceId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        psp_transaction_id = d.pop("pspTransactionId", UNSET)

        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for status_history_item_data in _status_history or []:
            status_history_item = SchemasStatusHistory.from_dict(status_history_item_data)

            status_history.append(status_history_item)

        refund = cls(
            refund_id=refund_id,
            customer_id=customer_id,
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            status=status,
            created_date=created_date,
            changed_date=changed_date,
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
