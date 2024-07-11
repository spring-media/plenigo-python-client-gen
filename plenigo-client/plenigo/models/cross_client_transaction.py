import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.cross_client_transaction_paid_status import CrossClientTransactionPaidStatus
from ..models.cross_client_transaction_payment_method import CrossClientTransactionPaymentMethod
from ..models.cross_client_transaction_type import CrossClientTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossClientTransaction")


@_attrs_define
class CrossClientTransaction:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        cross_client_transaction_id (Union[Unset, int]): unique id of the cross client transaction
        source_company_id (Union[Unset, str]): source company id
        connected_company_id (Union[Unset, str]): connected company id
        order_id (Union[Unset, int]): unique id of the order in the context of a company
        subscription_id (Union[Unset, int]): unique id of the subscription in the context of a company
        invoice_id (Union[Unset, int]): unique id of the invoice in the context of a company
        type (Union[Unset, CrossClientTransactionType]): type of the transaction
        paid_status (Union[Unset, CrossClientTransactionPaidStatus]): paid status update
        payment_method (Union[Unset, CrossClientTransactionPaymentMethod]): payment method used to pay for the order
            (ZERO indicates a free subscription)
        amount (Union[Unset, float]): amount to pay
        currency (Union[Unset, str]): currency of the order formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO 4217, alphabetic code</a>
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    cross_client_transaction_id: Union[Unset, int] = UNSET
    source_company_id: Union[Unset, str] = UNSET
    connected_company_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    subscription_id: Union[Unset, int] = UNSET
    invoice_id: Union[Unset, int] = UNSET
    type: Union[Unset, CrossClientTransactionType] = UNSET
    paid_status: Union[Unset, CrossClientTransactionPaidStatus] = UNSET
    payment_method: Union[Unset, CrossClientTransactionPaymentMethod] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        cross_client_transaction_id = self.cross_client_transaction_id

        source_company_id = self.source_company_id

        connected_company_id = self.connected_company_id

        order_id = self.order_id

        subscription_id = self.subscription_id

        invoice_id = self.invoice_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        paid_status: Union[Unset, str] = UNSET
        if not isinstance(self.paid_status, Unset):
            paid_status = self.paid_status.value

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        amount = self.amount

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if cross_client_transaction_id is not UNSET:
            field_dict["crossClientTransactionId"] = cross_client_transaction_id
        if source_company_id is not UNSET:
            field_dict["sourceCompanyId"] = source_company_id
        if connected_company_id is not UNSET:
            field_dict["connectedCompanyId"] = connected_company_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if type is not UNSET:
            field_dict["type"] = type
        if paid_status is not UNSET:
            field_dict["paidStatus"] = paid_status
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset):
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        cross_client_transaction_id = d.pop("crossClientTransactionId", UNSET)

        source_company_id = d.pop("sourceCompanyId", UNSET)

        connected_company_id = d.pop("connectedCompanyId", UNSET)

        order_id = d.pop("orderId", UNSET)

        subscription_id = d.pop("subscriptionId", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CrossClientTransactionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CrossClientTransactionType(_type)

        _paid_status = d.pop("paidStatus", UNSET)
        paid_status: Union[Unset, CrossClientTransactionPaidStatus]
        if isinstance(_paid_status, Unset):
            paid_status = UNSET
        else:
            paid_status = CrossClientTransactionPaidStatus(_paid_status)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, CrossClientTransactionPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = CrossClientTransactionPaymentMethod(_payment_method)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        cross_client_transaction = cls(
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            cross_client_transaction_id=cross_client_transaction_id,
            source_company_id=source_company_id,
            connected_company_id=connected_company_id,
            order_id=order_id,
            subscription_id=subscription_id,
            invoice_id=invoice_id,
            type=type,
            paid_status=paid_status,
            payment_method=payment_method,
            amount=amount,
            currency=currency,
        )

        cross_client_transaction.additional_properties = d
        return cross_client_transaction

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
