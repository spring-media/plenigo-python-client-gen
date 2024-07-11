import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.subscription_accounting_period_time_span import SubscriptionAccountingPeriodTimeSpan
from ..models.subscription_cancellation_period_time_span import SubscriptionCancellationPeriodTimeSpan
from ..models.subscription_cancellation_type import SubscriptionCancellationType
from ..models.subscription_duration_period_time_span import SubscriptionDurationPeriodTimeSpan
from ..models.subscription_managed_by import SubscriptionManagedBy
from ..models.subscription_payment_method import SubscriptionPaymentMethod
from ..models.subscription_precursor_reason import SubscriptionPrecursorReason
from ..models.subscription_status import SubscriptionStatus
from ..models.subscription_subscription_type import SubscriptionSubscriptionType
from ..models.subscription_successor_reason import SubscriptionSuccessorReason
from ..models.subscription_term_time_span import SubscriptionTermTimeSpan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_details import PaymentMethodDetails
    from ..models.subscription_connected_offer_info import SubscriptionConnectedOfferInfo
    from ..models.subscription_item import SubscriptionItem
    from ..models.subscription_pause_at import SubscriptionPauseAt


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        subscription_id (int): unique id of the subscription in the context of a company
        invoice_customer_id (str): id of the customer the invoice belongs to
        delivery_customer_id (str): id of the customer the delivery belongs to (also includes digital products)
        term (int): term of the subscription
        term_time_span (SubscriptionTermTimeSpan): represents the time span that is represented by the term
        accounting_period (int): accounting period of the subscription
        accounting_period_time_span (SubscriptionAccountingPeriodTimeSpan): represents the time span that is represented
            by the accounting period
        cancellation_period (int): cancellation period of the subscription
        cancellation_period_time_span (SubscriptionCancellationPeriodTimeSpan): represents the time span that is
            represented by the cancellation period
        start_date (Union[None, datetime.datetime]): start date time of the subscription with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        currency (str): currency of the subscription formatted as <a href="https://en.wikipedia.org/wiki/ISO_4217"
            target="_blank">ISO 4217, alphabetic code</a>
        payment_method (SubscriptionPaymentMethod): payment method used to pay for the subscription (ZERO indicates a
            free subscription)
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        analog_invoice (Union[Unset, bool]): flag indicating if the subscription is a analog invoice
        external_system_id (Union[Unset, str]): if subscription was imported from another system this field contains the
            unique id of the other system
        chain_id (Union[Unset, int]): all subscriptions that are in one chain because of some rules or cross selling
            share a unique chain id in the context of a company that is identically with the first subscription within the
            chain
        plenigo_offer_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo offer id is
            provided here
        invoice_address_id (Union[Unset, int]): id of the invoice address that is associated with this subscription
        delivery_address_id (Union[Unset, int]): id of the delivery address that is associated with this subscription
        cancellation_type (Union[Unset, SubscriptionCancellationType]): represents the cancellation type of the
            subscription
        reference_start_date (Union[None, Unset, datetime.datetime]): reference start date time of the subscription with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        end_date (Union[None, Unset, datetime.datetime]): end date time of the subscription with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        cancellation_date (Union[None, Unset, datetime.datetime]): cancellation date time of the subscription with date-
            time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        status (Union[Unset, SubscriptionStatus]): current status of the subscription
        payment_method_id (Union[Unset, int]): id of the payment method that is associated with this subscription
        payment_method_details (Union[Unset, PaymentMethodDetails]):
        access_blocked (Union[Unset, bool]): flag indicating if subscription is blocked and delivery customer cannot
            access products related to subscription, for example because of payment failed
        first_booking_date (Union[None, Unset, datetime.date]): date the first booking was executed for this
            subscription with full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6"
            target="_blank">RFC 3339, section 5.6</a>, for example, 2017-07-21
        last_booking_date (Union[None, Unset, datetime.date]): date the last booking was executed for this subscription
            with full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6"
            target="_blank">RFC 3339, section 5.6</a>, for example, 2017-07-21
        next_booking_date (Union[None, Unset, datetime.date]): date the next booking is going to be executed for this
            subscription with full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6"
            target="_blank">RFC 3339, section 5.6</a>, for example, 2017-07-21
        precursor_id (Union[Unset, int]): if there is another subscription preceding this subscription the id of the
            preceding subscription is provided here
        precursor_reason (Union[Unset, SubscriptionPrecursorReason]): reason for changing the subscription from the
            precursor
        precursor_reason_detail (Union[Unset, str]): reason detail for changing the subscription from the precursor
        successor_id (Union[Unset, int]): if there is another subscription following up this subscription the id of the
            next subscription is provided here
        successor_reason (Union[Unset, SubscriptionSuccessorReason]): reason for changing the subscription to the
            successor
        successor_reason_detail (Union[Unset, str]): reason detail for changing the subscription to the successor
        external_billing (Union[Unset, bool]): indicates if payments are handled by plenigo or an external system
        customer_cancellation_blocked (Union[Unset, bool]): indicates if a subscription cannot be cancelled by a
            customer
        cancellation_reason_unique_id (Union[Unset, str]): if a subscription was cancelled and a cancellation reason was
            added the unique id of the cancellation reason is set here
        customer_cancellation_reason_id (Union[Unset, int]): id of the customer cancellation reason that is associated
            with this subscription
        duration_period (Union[Unset, int]): duration period of the subscription till it ends in the successor
            subscription
        duration_period_time_span (Union[Unset, SubscriptionDurationPeriodTimeSpan]): represents the time span that is
            represented by the duration period
        managed_external (Union[Unset, bool]): flag indicates if a subscription is not managed by plenigo
        managed_by (Union[Unset, SubscriptionManagedBy]): managed by of the given subscription.
        payment_tries_done (Union[Unset, int]): amount of payment tries done in the current accounting period
        subscription_type (Union[Unset, SubscriptionSubscriptionType]): represents the type of the subscription
        suppress_invoice_sending (Union[Unset, bool]): flag indicating if the subscription invoice sending is suppressed
        purchase_order_indicator (Union[Unset, str]): purchase order indicator to set
        connected_offer (Union[Unset, bool]): flag indicates if a subscription is a connected offer
        connected_offer_info (Union[Unset, SubscriptionConnectedOfferInfo]):
        finished_deliveries (Union[Unset, int]): the current amount of finished deliveries
        open_deliveries (Union[Unset, int]): the current amount of open deliveries
        deliveries (Union[Unset, int]): the amount of deliveries
        chargeable_deliveries (Union[Unset, int]): the amount of chargeable deliveries
        recurring_deliveries (Union[Unset, int]): the amount of recurring deliveries
        active_partners (Union[Unset, List[str]]): the active partners
        delivery_paused (Union[Unset, SubscriptionPauseAt]):
        paused (Union[Unset, SubscriptionPauseAt]):
        payment_paused (Union[Unset, SubscriptionPauseAt]):
        items (Union[Unset, List['SubscriptionItem']]):
    """

    subscription_id: int
    invoice_customer_id: str
    delivery_customer_id: str
    term: int
    term_time_span: SubscriptionTermTimeSpan
    accounting_period: int
    accounting_period_time_span: SubscriptionAccountingPeriodTimeSpan
    cancellation_period: int
    cancellation_period_time_span: SubscriptionCancellationPeriodTimeSpan
    start_date: Union[None, datetime.datetime]
    currency: str
    payment_method: SubscriptionPaymentMethod
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    analog_invoice: Union[Unset, bool] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    chain_id: Union[Unset, int] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    invoice_address_id: Union[Unset, int] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    cancellation_type: Union[Unset, SubscriptionCancellationType] = UNSET
    reference_start_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    cancellation_date: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, SubscriptionStatus] = UNSET
    payment_method_id: Union[Unset, int] = UNSET
    payment_method_details: Union[Unset, "PaymentMethodDetails"] = UNSET
    access_blocked: Union[Unset, bool] = UNSET
    first_booking_date: Union[None, Unset, datetime.date] = UNSET
    last_booking_date: Union[None, Unset, datetime.date] = UNSET
    next_booking_date: Union[None, Unset, datetime.date] = UNSET
    precursor_id: Union[Unset, int] = UNSET
    precursor_reason: Union[Unset, SubscriptionPrecursorReason] = UNSET
    precursor_reason_detail: Union[Unset, str] = UNSET
    successor_id: Union[Unset, int] = UNSET
    successor_reason: Union[Unset, SubscriptionSuccessorReason] = UNSET
    successor_reason_detail: Union[Unset, str] = UNSET
    external_billing: Union[Unset, bool] = UNSET
    customer_cancellation_blocked: Union[Unset, bool] = UNSET
    cancellation_reason_unique_id: Union[Unset, str] = UNSET
    customer_cancellation_reason_id: Union[Unset, int] = UNSET
    duration_period: Union[Unset, int] = UNSET
    duration_period_time_span: Union[Unset, SubscriptionDurationPeriodTimeSpan] = UNSET
    managed_external: Union[Unset, bool] = UNSET
    managed_by: Union[Unset, SubscriptionManagedBy] = UNSET
    payment_tries_done: Union[Unset, int] = UNSET
    subscription_type: Union[Unset, SubscriptionSubscriptionType] = UNSET
    suppress_invoice_sending: Union[Unset, bool] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    connected_offer: Union[Unset, bool] = UNSET
    connected_offer_info: Union[Unset, "SubscriptionConnectedOfferInfo"] = UNSET
    finished_deliveries: Union[Unset, int] = UNSET
    open_deliveries: Union[Unset, int] = UNSET
    deliveries: Union[Unset, int] = UNSET
    chargeable_deliveries: Union[Unset, int] = UNSET
    recurring_deliveries: Union[Unset, int] = UNSET
    active_partners: Union[Unset, List[str]] = UNSET
    delivery_paused: Union[Unset, "SubscriptionPauseAt"] = UNSET
    paused: Union[Unset, "SubscriptionPauseAt"] = UNSET
    payment_paused: Union[Unset, "SubscriptionPauseAt"] = UNSET
    items: Union[Unset, List["SubscriptionItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_id = self.subscription_id

        invoice_customer_id = self.invoice_customer_id

        delivery_customer_id = self.delivery_customer_id

        term = self.term

        term_time_span = self.term_time_span.value

        accounting_period = self.accounting_period

        accounting_period_time_span = self.accounting_period_time_span.value

        cancellation_period = self.cancellation_period

        cancellation_period_time_span = self.cancellation_period_time_span.value

        start_date: Union[None, str]
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        currency = self.currency

        payment_method = self.payment_method.value

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

        analog_invoice = self.analog_invoice

        external_system_id = self.external_system_id

        chain_id = self.chain_id

        plenigo_offer_id = self.plenigo_offer_id

        invoice_address_id = self.invoice_address_id

        delivery_address_id = self.delivery_address_id

        cancellation_type: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_type, Unset):
            cancellation_type = self.cancellation_type.value

        reference_start_date: Union[None, Unset, str]
        if isinstance(self.reference_start_date, Unset):
            reference_start_date = UNSET
        elif isinstance(self.reference_start_date, datetime.datetime):
            reference_start_date = self.reference_start_date.isoformat()
        else:
            reference_start_date = self.reference_start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        cancellation_date: Union[None, Unset, str]
        if isinstance(self.cancellation_date, Unset):
            cancellation_date = UNSET
        elif isinstance(self.cancellation_date, datetime.datetime):
            cancellation_date = self.cancellation_date.isoformat()
        else:
            cancellation_date = self.cancellation_date

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_method_id = self.payment_method_id

        payment_method_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_details, Unset):
            payment_method_details = self.payment_method_details.to_dict()

        access_blocked = self.access_blocked

        first_booking_date: Union[None, Unset, str]
        if isinstance(self.first_booking_date, Unset):
            first_booking_date = UNSET
        elif isinstance(self.first_booking_date, datetime.date):
            first_booking_date = self.first_booking_date.isoformat()
        else:
            first_booking_date = self.first_booking_date

        last_booking_date: Union[None, Unset, str]
        if isinstance(self.last_booking_date, Unset):
            last_booking_date = UNSET
        elif isinstance(self.last_booking_date, datetime.date):
            last_booking_date = self.last_booking_date.isoformat()
        else:
            last_booking_date = self.last_booking_date

        next_booking_date: Union[None, Unset, str]
        if isinstance(self.next_booking_date, Unset):
            next_booking_date = UNSET
        elif isinstance(self.next_booking_date, datetime.date):
            next_booking_date = self.next_booking_date.isoformat()
        else:
            next_booking_date = self.next_booking_date

        precursor_id = self.precursor_id

        precursor_reason: Union[Unset, str] = UNSET
        if not isinstance(self.precursor_reason, Unset):
            precursor_reason = self.precursor_reason.value

        precursor_reason_detail = self.precursor_reason_detail

        successor_id = self.successor_id

        successor_reason: Union[Unset, str] = UNSET
        if not isinstance(self.successor_reason, Unset):
            successor_reason = self.successor_reason.value

        successor_reason_detail = self.successor_reason_detail

        external_billing = self.external_billing

        customer_cancellation_blocked = self.customer_cancellation_blocked

        cancellation_reason_unique_id = self.cancellation_reason_unique_id

        customer_cancellation_reason_id = self.customer_cancellation_reason_id

        duration_period = self.duration_period

        duration_period_time_span: Union[Unset, str] = UNSET
        if not isinstance(self.duration_period_time_span, Unset):
            duration_period_time_span = self.duration_period_time_span.value

        managed_external = self.managed_external

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value

        payment_tries_done = self.payment_tries_done

        subscription_type: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_type, Unset):
            subscription_type = self.subscription_type.value

        suppress_invoice_sending = self.suppress_invoice_sending

        purchase_order_indicator = self.purchase_order_indicator

        connected_offer = self.connected_offer

        connected_offer_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connected_offer_info, Unset):
            connected_offer_info = self.connected_offer_info.to_dict()

        finished_deliveries = self.finished_deliveries

        open_deliveries = self.open_deliveries

        deliveries = self.deliveries

        chargeable_deliveries = self.chargeable_deliveries

        recurring_deliveries = self.recurring_deliveries

        active_partners: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_partners, Unset):
            active_partners = self.active_partners

        delivery_paused: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_paused, Unset):
            delivery_paused = self.delivery_paused.to_dict()

        paused: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paused, Unset):
            paused = self.paused.to_dict()

        payment_paused: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_paused, Unset):
            payment_paused = self.payment_paused.to_dict()

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "invoiceCustomerId": invoice_customer_id,
                "deliveryCustomerId": delivery_customer_id,
                "term": term,
                "termTimeSpan": term_time_span,
                "accountingPeriod": accounting_period,
                "accountingPeriodTimeSpan": accounting_period_time_span,
                "cancellationPeriod": cancellation_period,
                "cancellationPeriodTimeSpan": cancellation_period_time_span,
                "startDate": start_date,
                "currency": currency,
                "paymentMethod": payment_method,
            }
        )
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
        if analog_invoice is not UNSET:
            field_dict["analogInvoice"] = analog_invoice
        if external_system_id is not UNSET:
            field_dict["externalSystemId"] = external_system_id
        if chain_id is not UNSET:
            field_dict["chainId"] = chain_id
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if invoice_address_id is not UNSET:
            field_dict["invoiceAddressId"] = invoice_address_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id
        if cancellation_type is not UNSET:
            field_dict["cancellationType"] = cancellation_type
        if reference_start_date is not UNSET:
            field_dict["referenceStartDate"] = reference_start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if cancellation_date is not UNSET:
            field_dict["cancellationDate"] = cancellation_date
        if status is not UNSET:
            field_dict["status"] = status
        if payment_method_id is not UNSET:
            field_dict["paymentMethodId"] = payment_method_id
        if payment_method_details is not UNSET:
            field_dict["paymentMethodDetails"] = payment_method_details
        if access_blocked is not UNSET:
            field_dict["accessBlocked"] = access_blocked
        if first_booking_date is not UNSET:
            field_dict["firstBookingDate"] = first_booking_date
        if last_booking_date is not UNSET:
            field_dict["lastBookingDate"] = last_booking_date
        if next_booking_date is not UNSET:
            field_dict["nextBookingDate"] = next_booking_date
        if precursor_id is not UNSET:
            field_dict["precursorId"] = precursor_id
        if precursor_reason is not UNSET:
            field_dict["precursorReason"] = precursor_reason
        if precursor_reason_detail is not UNSET:
            field_dict["precursorReasonDetail"] = precursor_reason_detail
        if successor_id is not UNSET:
            field_dict["successorId"] = successor_id
        if successor_reason is not UNSET:
            field_dict["successorReason"] = successor_reason
        if successor_reason_detail is not UNSET:
            field_dict["successorReasonDetail"] = successor_reason_detail
        if external_billing is not UNSET:
            field_dict["externalBilling"] = external_billing
        if customer_cancellation_blocked is not UNSET:
            field_dict["customerCancellationBlocked"] = customer_cancellation_blocked
        if cancellation_reason_unique_id is not UNSET:
            field_dict["cancellationReasonUniqueId"] = cancellation_reason_unique_id
        if customer_cancellation_reason_id is not UNSET:
            field_dict["customerCancellationReasonId"] = customer_cancellation_reason_id
        if duration_period is not UNSET:
            field_dict["durationPeriod"] = duration_period
        if duration_period_time_span is not UNSET:
            field_dict["durationPeriodTimeSpan"] = duration_period_time_span
        if managed_external is not UNSET:
            field_dict["managedExternal"] = managed_external
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if payment_tries_done is not UNSET:
            field_dict["paymentTriesDone"] = payment_tries_done
        if subscription_type is not UNSET:
            field_dict["subscriptionType"] = subscription_type
        if suppress_invoice_sending is not UNSET:
            field_dict["suppressInvoiceSending"] = suppress_invoice_sending
        if purchase_order_indicator is not UNSET:
            field_dict["purchaseOrderIndicator"] = purchase_order_indicator
        if connected_offer is not UNSET:
            field_dict["connectedOffer"] = connected_offer
        if connected_offer_info is not UNSET:
            field_dict["connectedOfferInfo"] = connected_offer_info
        if finished_deliveries is not UNSET:
            field_dict["finishedDeliveries"] = finished_deliveries
        if open_deliveries is not UNSET:
            field_dict["openDeliveries"] = open_deliveries
        if deliveries is not UNSET:
            field_dict["deliveries"] = deliveries
        if chargeable_deliveries is not UNSET:
            field_dict["chargeableDeliveries"] = chargeable_deliveries
        if recurring_deliveries is not UNSET:
            field_dict["recurringDeliveries"] = recurring_deliveries
        if active_partners is not UNSET:
            field_dict["activePartners"] = active_partners
        if delivery_paused is not UNSET:
            field_dict["deliveryPaused"] = delivery_paused
        if paused is not UNSET:
            field_dict["paused"] = paused
        if payment_paused is not UNSET:
            field_dict["paymentPaused"] = payment_paused
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_details import PaymentMethodDetails
        from ..models.subscription_connected_offer_info import SubscriptionConnectedOfferInfo
        from ..models.subscription_item import SubscriptionItem
        from ..models.subscription_pause_at import SubscriptionPauseAt

        d = src_dict.copy()
        subscription_id = d.pop("subscriptionId")

        invoice_customer_id = d.pop("invoiceCustomerId")

        delivery_customer_id = d.pop("deliveryCustomerId")

        term = d.pop("term")

        term_time_span = SubscriptionTermTimeSpan(d.pop("termTimeSpan"))

        accounting_period = d.pop("accountingPeriod")

        accounting_period_time_span = SubscriptionAccountingPeriodTimeSpan(d.pop("accountingPeriodTimeSpan"))

        cancellation_period = d.pop("cancellationPeriod")

        cancellation_period_time_span = SubscriptionCancellationPeriodTimeSpan(d.pop("cancellationPeriodTimeSpan"))

        def _parse_start_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("startDate"))

        currency = d.pop("currency")

        payment_method = SubscriptionPaymentMethod(d.pop("paymentMethod"))

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

        analog_invoice = d.pop("analogInvoice", UNSET)

        external_system_id = d.pop("externalSystemId", UNSET)

        chain_id = d.pop("chainId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        invoice_address_id = d.pop("invoiceAddressId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        _cancellation_type = d.pop("cancellationType", UNSET)
        cancellation_type: Union[Unset, SubscriptionCancellationType]
        if isinstance(_cancellation_type, Unset):
            cancellation_type = UNSET
        else:
            cancellation_type = SubscriptionCancellationType(_cancellation_type)

        def _parse_reference_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_start_date_type_0 = isoparse(data)

                return reference_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        reference_start_date = _parse_reference_start_date(d.pop("referenceStartDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_cancellation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancellation_date_type_0 = isoparse(data)

                return cancellation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cancellation_date = _parse_cancellation_date(d.pop("cancellationDate", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubscriptionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubscriptionStatus(_status)

        payment_method_id = d.pop("paymentMethodId", UNSET)

        _payment_method_details = d.pop("paymentMethodDetails", UNSET)
        payment_method_details: Union[Unset, PaymentMethodDetails]
        if isinstance(_payment_method_details, Unset):
            payment_method_details = UNSET
        else:
            payment_method_details = PaymentMethodDetails.from_dict(_payment_method_details)

        access_blocked = d.pop("accessBlocked", UNSET)

        def _parse_first_booking_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_booking_date_type_0 = isoparse(data).date()

                return first_booking_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        first_booking_date = _parse_first_booking_date(d.pop("firstBookingDate", UNSET))

        def _parse_last_booking_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_booking_date_type_0 = isoparse(data).date()

                return last_booking_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        last_booking_date = _parse_last_booking_date(d.pop("lastBookingDate", UNSET))

        def _parse_next_booking_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_booking_date_type_0 = isoparse(data).date()

                return next_booking_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        next_booking_date = _parse_next_booking_date(d.pop("nextBookingDate", UNSET))

        precursor_id = d.pop("precursorId", UNSET)

        _precursor_reason = d.pop("precursorReason", UNSET)
        precursor_reason: Union[Unset, SubscriptionPrecursorReason]
        if isinstance(_precursor_reason, Unset):
            precursor_reason = UNSET
        else:
            precursor_reason = SubscriptionPrecursorReason(_precursor_reason)

        precursor_reason_detail = d.pop("precursorReasonDetail", UNSET)

        successor_id = d.pop("successorId", UNSET)

        _successor_reason = d.pop("successorReason", UNSET)
        successor_reason: Union[Unset, SubscriptionSuccessorReason]
        if isinstance(_successor_reason, Unset):
            successor_reason = UNSET
        else:
            successor_reason = SubscriptionSuccessorReason(_successor_reason)

        successor_reason_detail = d.pop("successorReasonDetail", UNSET)

        external_billing = d.pop("externalBilling", UNSET)

        customer_cancellation_blocked = d.pop("customerCancellationBlocked", UNSET)

        cancellation_reason_unique_id = d.pop("cancellationReasonUniqueId", UNSET)

        customer_cancellation_reason_id = d.pop("customerCancellationReasonId", UNSET)

        duration_period = d.pop("durationPeriod", UNSET)

        _duration_period_time_span = d.pop("durationPeriodTimeSpan", UNSET)
        duration_period_time_span: Union[Unset, SubscriptionDurationPeriodTimeSpan]
        if isinstance(_duration_period_time_span, Unset):
            duration_period_time_span = UNSET
        else:
            duration_period_time_span = SubscriptionDurationPeriodTimeSpan(_duration_period_time_span)

        managed_external = d.pop("managedExternal", UNSET)

        _managed_by = d.pop("managedBy", UNSET)
        managed_by: Union[Unset, SubscriptionManagedBy]
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = SubscriptionManagedBy(_managed_by)

        payment_tries_done = d.pop("paymentTriesDone", UNSET)

        _subscription_type = d.pop("subscriptionType", UNSET)
        subscription_type: Union[Unset, SubscriptionSubscriptionType]
        if isinstance(_subscription_type, Unset):
            subscription_type = UNSET
        else:
            subscription_type = SubscriptionSubscriptionType(_subscription_type)

        suppress_invoice_sending = d.pop("suppressInvoiceSending", UNSET)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        connected_offer = d.pop("connectedOffer", UNSET)

        _connected_offer_info = d.pop("connectedOfferInfo", UNSET)
        connected_offer_info: Union[Unset, SubscriptionConnectedOfferInfo]
        if isinstance(_connected_offer_info, Unset):
            connected_offer_info = UNSET
        else:
            connected_offer_info = SubscriptionConnectedOfferInfo.from_dict(_connected_offer_info)

        finished_deliveries = d.pop("finishedDeliveries", UNSET)

        open_deliveries = d.pop("openDeliveries", UNSET)

        deliveries = d.pop("deliveries", UNSET)

        chargeable_deliveries = d.pop("chargeableDeliveries", UNSET)

        recurring_deliveries = d.pop("recurringDeliveries", UNSET)

        active_partners = cast(List[str], d.pop("activePartners", UNSET))

        _delivery_paused = d.pop("deliveryPaused", UNSET)
        delivery_paused: Union[Unset, SubscriptionPauseAt]
        if isinstance(_delivery_paused, Unset):
            delivery_paused = UNSET
        else:
            delivery_paused = SubscriptionPauseAt.from_dict(_delivery_paused)

        _paused = d.pop("paused", UNSET)
        paused: Union[Unset, SubscriptionPauseAt]
        if isinstance(_paused, Unset):
            paused = UNSET
        else:
            paused = SubscriptionPauseAt.from_dict(_paused)

        _payment_paused = d.pop("paymentPaused", UNSET)
        payment_paused: Union[Unset, SubscriptionPauseAt]
        if isinstance(_payment_paused, Unset):
            payment_paused = UNSET
        else:
            payment_paused = SubscriptionPauseAt.from_dict(_payment_paused)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = SubscriptionItem.from_dict(items_item_data)

            items.append(items_item)

        subscription = cls(
            subscription_id=subscription_id,
            invoice_customer_id=invoice_customer_id,
            delivery_customer_id=delivery_customer_id,
            term=term,
            term_time_span=term_time_span,
            accounting_period=accounting_period,
            accounting_period_time_span=accounting_period_time_span,
            cancellation_period=cancellation_period,
            cancellation_period_time_span=cancellation_period_time_span,
            start_date=start_date,
            currency=currency,
            payment_method=payment_method,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            analog_invoice=analog_invoice,
            external_system_id=external_system_id,
            chain_id=chain_id,
            plenigo_offer_id=plenigo_offer_id,
            invoice_address_id=invoice_address_id,
            delivery_address_id=delivery_address_id,
            cancellation_type=cancellation_type,
            reference_start_date=reference_start_date,
            end_date=end_date,
            cancellation_date=cancellation_date,
            status=status,
            payment_method_id=payment_method_id,
            payment_method_details=payment_method_details,
            access_blocked=access_blocked,
            first_booking_date=first_booking_date,
            last_booking_date=last_booking_date,
            next_booking_date=next_booking_date,
            precursor_id=precursor_id,
            precursor_reason=precursor_reason,
            precursor_reason_detail=precursor_reason_detail,
            successor_id=successor_id,
            successor_reason=successor_reason,
            successor_reason_detail=successor_reason_detail,
            external_billing=external_billing,
            customer_cancellation_blocked=customer_cancellation_blocked,
            cancellation_reason_unique_id=cancellation_reason_unique_id,
            customer_cancellation_reason_id=customer_cancellation_reason_id,
            duration_period=duration_period,
            duration_period_time_span=duration_period_time_span,
            managed_external=managed_external,
            managed_by=managed_by,
            payment_tries_done=payment_tries_done,
            subscription_type=subscription_type,
            suppress_invoice_sending=suppress_invoice_sending,
            purchase_order_indicator=purchase_order_indicator,
            connected_offer=connected_offer,
            connected_offer_info=connected_offer_info,
            finished_deliveries=finished_deliveries,
            open_deliveries=open_deliveries,
            deliveries=deliveries,
            chargeable_deliveries=chargeable_deliveries,
            recurring_deliveries=recurring_deliveries,
            active_partners=active_partners,
            delivery_paused=delivery_paused,
            paused=paused,
            payment_paused=payment_paused,
            items=items,
        )

        subscription.additional_properties = d
        return subscription

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
