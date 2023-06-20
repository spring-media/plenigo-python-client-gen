from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GooglePlaySubscriptionPurchase")


@attr.s(auto_attribs=True)
class GooglePlaySubscriptionPurchase:
    """
    Attributes:
        auto_renewing (Union[Unset, bool]): whether the subscription will automatically be renewed when it reaches its
            current expiry time
        auto_resume_time_millis (Union[Unset, int]): time at which the subscription will be automatically resumed, in
            milliseconds since the Epoch - only present if the user has requested to pause the subscription
        cancel_reason (Union[Unset, int]): the reason why a subscription was canceled or is not auto-renewing
        cancel_survey_reason (Union[Unset, int]): information provided by the user when they complete the subscription
            cancellation flow (cancellation reason survey)
        user_input_cancel_reason (Union[Unset, str]): customized input cancel reason from the user. Only present when
            cancelReason is 0
        country_code (Union[Unset, str]): ISO 3166-1 alpha-2 billing country/region code of the user at the time the
            subscription was granted
        developer_payload (Union[Unset, str]): developer-specified string that contains supplemental information about
            an order
        expiry_time_millis (Union[Unset, int]): time at which the subscription will expire, in milliseconds since the
            Epoch
        kind (Union[Unset, str]): kind represents a subscriptionPurchase object in the androidpublisher service
        linked_purchase_token (Union[Unset, str]): purchase token of the originating purchase if this subscription is
            one of the following - 0. Re-signup of a canceled but non-lapsed subscription 1. Upgrade/downgrade from a
            previous subscription
        order_id (Union[Unset, str]): order id of the latest recurring order associated with the purchase of the
            subscription
        payment_state (Union[Unset, int]): payment state of the subscription
        price_amount_micros (Union[Unset, int]): price of the subscription, not including tax
        price_currency_code (Union[Unset, str]): ISO 4217 currency code for the subscription price
        profile_id (Union[Unset, str]): Google profile id of the user when the subscription was purchased
        profile_name (Union[Unset, str]): profile name of the user when the subscription was purchased
        purchase_type (Union[Unset, int]): type of purchase of the subscription - this field is only set if this
            purchase was not made using the standard in-app billing flow
        start_time_millis (Union[Unset, int]): time at which the subscription was granted, in milliseconds since the
            Epoch
        user_cancellation_time_millis (Union[Unset, int]): time at which the subscription was canceled by the user, in
            milliseconds since the epoch
    """

    auto_renewing: Union[Unset, bool] = UNSET
    auto_resume_time_millis: Union[Unset, int] = UNSET
    cancel_reason: Union[Unset, int] = UNSET
    cancel_survey_reason: Union[Unset, int] = UNSET
    user_input_cancel_reason: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    developer_payload: Union[Unset, str] = UNSET
    expiry_time_millis: Union[Unset, int] = UNSET
    kind: Union[Unset, str] = UNSET
    linked_purchase_token: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    payment_state: Union[Unset, int] = UNSET
    price_amount_micros: Union[Unset, int] = UNSET
    price_currency_code: Union[Unset, str] = UNSET
    profile_id: Union[Unset, str] = UNSET
    profile_name: Union[Unset, str] = UNSET
    purchase_type: Union[Unset, int] = UNSET
    start_time_millis: Union[Unset, int] = UNSET
    user_cancellation_time_millis: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_renewing = self.auto_renewing
        auto_resume_time_millis = self.auto_resume_time_millis
        cancel_reason = self.cancel_reason
        cancel_survey_reason = self.cancel_survey_reason
        user_input_cancel_reason = self.user_input_cancel_reason
        country_code = self.country_code
        developer_payload = self.developer_payload
        expiry_time_millis = self.expiry_time_millis
        kind = self.kind
        linked_purchase_token = self.linked_purchase_token
        order_id = self.order_id
        payment_state = self.payment_state
        price_amount_micros = self.price_amount_micros
        price_currency_code = self.price_currency_code
        profile_id = self.profile_id
        profile_name = self.profile_name
        purchase_type = self.purchase_type
        start_time_millis = self.start_time_millis
        user_cancellation_time_millis = self.user_cancellation_time_millis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_renewing is not UNSET:
            field_dict["autoRenewing"] = auto_renewing
        if auto_resume_time_millis is not UNSET:
            field_dict["autoResumeTimeMillis"] = auto_resume_time_millis
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if cancel_survey_reason is not UNSET:
            field_dict["cancelSurveyReason"] = cancel_survey_reason
        if user_input_cancel_reason is not UNSET:
            field_dict["userInputCancelReason"] = user_input_cancel_reason
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if developer_payload is not UNSET:
            field_dict["developerPayload"] = developer_payload
        if expiry_time_millis is not UNSET:
            field_dict["expiryTimeMillis"] = expiry_time_millis
        if kind is not UNSET:
            field_dict["kind"] = kind
        if linked_purchase_token is not UNSET:
            field_dict["linkedPurchaseToken"] = linked_purchase_token
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if payment_state is not UNSET:
            field_dict["paymentState"] = payment_state
        if price_amount_micros is not UNSET:
            field_dict["priceAmountMicros"] = price_amount_micros
        if price_currency_code is not UNSET:
            field_dict["priceCurrencyCode"] = price_currency_code
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if purchase_type is not UNSET:
            field_dict["purchaseType"] = purchase_type
        if start_time_millis is not UNSET:
            field_dict["startTimeMillis"] = start_time_millis
        if user_cancellation_time_millis is not UNSET:
            field_dict["userCancellationTimeMillis"] = user_cancellation_time_millis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_renewing = d.pop("autoRenewing", UNSET)

        auto_resume_time_millis = d.pop("autoResumeTimeMillis", UNSET)

        cancel_reason = d.pop("cancelReason", UNSET)

        cancel_survey_reason = d.pop("cancelSurveyReason", UNSET)

        user_input_cancel_reason = d.pop("userInputCancelReason", UNSET)

        country_code = d.pop("countryCode", UNSET)

        developer_payload = d.pop("developerPayload", UNSET)

        expiry_time_millis = d.pop("expiryTimeMillis", UNSET)

        kind = d.pop("kind", UNSET)

        linked_purchase_token = d.pop("linkedPurchaseToken", UNSET)

        order_id = d.pop("orderId", UNSET)

        payment_state = d.pop("paymentState", UNSET)

        price_amount_micros = d.pop("priceAmountMicros", UNSET)

        price_currency_code = d.pop("priceCurrencyCode", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        purchase_type = d.pop("purchaseType", UNSET)

        start_time_millis = d.pop("startTimeMillis", UNSET)

        user_cancellation_time_millis = d.pop("userCancellationTimeMillis", UNSET)

        google_play_subscription_purchase = cls(
            auto_renewing=auto_renewing,
            auto_resume_time_millis=auto_resume_time_millis,
            cancel_reason=cancel_reason,
            cancel_survey_reason=cancel_survey_reason,
            user_input_cancel_reason=user_input_cancel_reason,
            country_code=country_code,
            developer_payload=developer_payload,
            expiry_time_millis=expiry_time_millis,
            kind=kind,
            linked_purchase_token=linked_purchase_token,
            order_id=order_id,
            payment_state=payment_state,
            price_amount_micros=price_amount_micros,
            price_currency_code=price_currency_code,
            profile_id=profile_id,
            profile_name=profile_name,
            purchase_type=purchase_type,
            start_time_millis=start_time_millis,
            user_cancellation_time_millis=user_cancellation_time_millis,
        )

        google_play_subscription_purchase.additional_properties = d
        return google_play_subscription_purchase

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
