import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_payment_action import TransactionPaymentAction
from ..models.transaction_payment_method import TransactionPaymentMethod
from ..models.transaction_payment_provider import TransactionPaymentProvider
from ..models.transaction_payment_status import TransactionPaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        transaction_id (int): unique id of the transaction also used for pagination
        plenigo_transaction_id (str): unique plenigo transaction id used to communicate with payment provider
        amount (float): amount of the transaction
        currency (str): currency of the transaction formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_provider (TransactionPaymentProvider): payment provider used for transaction execution
        payment_method (TransactionPaymentMethod): payment method used
        payment_action (TransactionPaymentAction): payment action executed
        payment_status (TransactionPaymentStatus): status of the transaction
        customer_id (str): unique id of the customer the transaction is related to
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        transaction_date (Union[None, Unset, datetime.datetime]): date the transaction was done with date-time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21T17:32:28Z
        fulfillment_date (Union[None, Unset, datetime.datetime]): date the transaction was fulfilled with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        psp_transaction_id (Union[Unset, str]): id of the payment service provider if one was provided
        description (Union[Unset, str]): description describing the transaction reason
        error_code (Union[Unset, str]): error code for transaction failure
        error_message (Union[Unset, str]): description of the error
    """

    transaction_id: int
    plenigo_transaction_id: str
    amount: float
    currency: str
    payment_provider: TransactionPaymentProvider
    payment_method: TransactionPaymentMethod
    payment_action: TransactionPaymentAction
    payment_status: TransactionPaymentStatus
    customer_id: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    transaction_date: Union[None, Unset, datetime.datetime] = UNSET
    fulfillment_date: Union[None, Unset, datetime.datetime] = UNSET
    psp_transaction_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    error_code: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id

        plenigo_transaction_id = self.plenigo_transaction_id

        amount = self.amount

        currency = self.currency

        payment_provider = self.payment_provider.value

        payment_method = self.payment_method.value

        payment_action = self.payment_action.value

        payment_status = self.payment_status.value

        customer_id = self.customer_id

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

        transaction_date: Union[None, Unset, str]
        if isinstance(self.transaction_date, Unset) or self.transaction_date is None:
            transaction_date = UNSET
        elif isinstance(self.transaction_date, datetime.datetime):
            transaction_date = self.transaction_date.isoformat()
        else:
            transaction_date = self.transaction_date

        fulfillment_date: Union[None, Unset, str]
        if isinstance(self.fulfillment_date, Unset) or self.fulfillment_date is None:
            fulfillment_date = UNSET
        elif isinstance(self.fulfillment_date, datetime.datetime):
            fulfillment_date = self.fulfillment_date.isoformat()
        else:
            fulfillment_date = self.fulfillment_date

        psp_transaction_id = self.psp_transaction_id

        description = self.description

        error_code = self.error_code

        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactionId": transaction_id,
                "plenigoTransactionId": plenigo_transaction_id,
                "amount": amount,
                "currency": currency,
                "paymentProvider": payment_provider,
                "paymentMethod": payment_method,
                "paymentAction": payment_action,
                "paymentStatus": payment_status,
                "customerId": customer_id,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if fulfillment_date is not UNSET:
            field_dict["fulfillmentDate"] = fulfillment_date
        if psp_transaction_id is not UNSET:
            field_dict["pspTransactionId"] = psp_transaction_id
        if description is not UNSET:
            field_dict["description"] = description
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transactionId")

        plenigo_transaction_id = d.pop("plenigoTransactionId")

        amount = d.pop("amount")

        currency = d.pop("currency")

        payment_provider = TransactionPaymentProvider(d.pop("paymentProvider"))

        payment_method = TransactionPaymentMethod(d.pop("paymentMethod"))

        payment_action = TransactionPaymentAction(d.pop("paymentAction"))

        payment_status = TransactionPaymentStatus(d.pop("paymentStatus"))

        customer_id = d.pop("customerId")

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
                created_date_type_0 = isoparse(data)

                return created_date_type_0
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
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        def _parse_transaction_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                transaction_date_type_0 = isoparse(data)

                return transaction_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        transaction_date = _parse_transaction_date(d.pop("transactionDate", UNSET))

        def _parse_fulfillment_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                fulfillment_date_type_0 = isoparse(data)

                return fulfillment_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        fulfillment_date = _parse_fulfillment_date(d.pop("fulfillmentDate", UNSET))

        psp_transaction_id = d.pop("pspTransactionId", UNSET)

        description = d.pop("description", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        transaction = cls(
            transaction_id=transaction_id,
            plenigo_transaction_id=plenigo_transaction_id,
            amount=amount,
            currency=currency,
            payment_provider=payment_provider,
            payment_method=payment_method,
            payment_action=payment_action,
            payment_status=payment_status,
            customer_id=customer_id,
            created_date=created_date,
            changed_date=changed_date,
            transaction_date=transaction_date,
            fulfillment_date=fulfillment_date,
            psp_transaction_id=psp_transaction_id,
            description=description,
            error_code=error_code,
            error_message=error_message,
        )

        transaction.additional_properties = d
        return transaction

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
