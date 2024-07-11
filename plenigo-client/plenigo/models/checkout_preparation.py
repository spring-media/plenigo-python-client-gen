import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.checkout_preparation_allowed_payment_methods_item import CheckoutPreparationAllowedPaymentMethodsItem
from ..models.checkout_preparation_force_payment_method import CheckoutPreparationForcePaymentMethod
from ..models.checkout_preparation_gift_option import CheckoutPreparationGiftOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_order_data import AdditionalOrderData
    from ..models.checkout_address_settings import CheckoutAddressSettings
    from ..models.checkout_offer import CheckoutOffer
    from ..models.connected_offer_request import ConnectedOfferRequest


T = TypeVar("T", bound="CheckoutPreparation")


@_attrs_define
class CheckoutPreparation:
    """
    Attributes:
        customer_ip_address (str): ip address of the customer
        customer_id (Union[Unset, str]): unique id of the customer the checkout is for
        customer_session (Union[Unset, str]): active customer session - if a customer id is provided the customer id
            overrules the session
        invoice_address_id (Union[Unset, int]): unique id of the invoice address to use
        delivery_address_id (Union[Unset, int]): unique id of the delivery address to use
        show_net_prices (Union[Unset, bool]): flag indicating if net prices should be shown during checkout
        payment_only (Union[Unset, bool]): flag indicating that the checkout should only show payment information
        force_payment_method (Union[Unset, CheckoutPreparationForcePaymentMethod]): force checkout to use a specific
            payment method
        basket_id (Union[Unset, str]): unique id of the plenigo basket
        allow_multiple_purchases (Union[Unset, bool]): flag indicating if product can be bought multiple times - a user
            will be able to pay the same product twice
        start_with_voucher_input (Union[Unset, bool]): flag indicating if checkout process should start with a voucher
            input field - this field is only a hint for the visual representation
            and if you don't use the plenigo iFrame checkout the logic must be implemented on your side
        hide_voucher_input (Union[Unset, bool]): flag indicating if checkout process should hide the voucher input field
            - this field is only a hint for the visual representation
            and if you don't use the plenigo iFrame checkout the logic must be implemented on your side
        allowed_payment_methods (Union[Unset, List[CheckoutPreparationAllowedPaymentMethodsItem]]): possibility for
            additional restrictions of payment methods - only payment methods provided here and configured in the backend
            are allowed during checkout
        language (Union[Unset, str]): language to use during checkout - two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a>
        debug_mode (Union[Unset, bool]): flag indicating if debug information should be shown during purchase process
        subscription_start_date (Union[None, Unset, datetime.datetime]): optional start date of subscriptions with date
            notation as defined for example, 2017-07-21
        address_settings (Union[Unset, CheckoutAddressSettings]):
        gift_option (Union[Unset, CheckoutPreparationGiftOption]): flag that controls if the checkout should be run as a
            gift checkout, should show a gift checkout box or hide it - the default value is
            HIDE_GIFT_OPTION
        additional_data (Union[Unset, AdditionalOrderData]):
        voucher_code (Union[Unset, str]): voucher code - if voucher code is provided no items must be provided
        items (Union[Unset, List['CheckoutOffer']]): offers that should be sold via checkout
        connected_offer_items (Union[Unset, List['ConnectedOfferRequest']]): connected offers that should be sold via
            checkout
    """

    customer_ip_address: str
    customer_id: Union[Unset, str] = UNSET
    customer_session: Union[Unset, str] = UNSET
    invoice_address_id: Union[Unset, int] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    show_net_prices: Union[Unset, bool] = UNSET
    payment_only: Union[Unset, bool] = UNSET
    force_payment_method: Union[Unset, CheckoutPreparationForcePaymentMethod] = UNSET
    basket_id: Union[Unset, str] = UNSET
    allow_multiple_purchases: Union[Unset, bool] = UNSET
    start_with_voucher_input: Union[Unset, bool] = UNSET
    hide_voucher_input: Union[Unset, bool] = UNSET
    allowed_payment_methods: Union[Unset, List[CheckoutPreparationAllowedPaymentMethodsItem]] = UNSET
    language: Union[Unset, str] = UNSET
    debug_mode: Union[Unset, bool] = UNSET
    subscription_start_date: Union[None, Unset, datetime.datetime] = UNSET
    address_settings: Union[Unset, "CheckoutAddressSettings"] = UNSET
    gift_option: Union[Unset, CheckoutPreparationGiftOption] = UNSET
    additional_data: Union[Unset, "AdditionalOrderData"] = UNSET
    voucher_code: Union[Unset, str] = UNSET
    items: Union[Unset, List["CheckoutOffer"]] = UNSET
    connected_offer_items: Union[Unset, List["ConnectedOfferRequest"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_ip_address = self.customer_ip_address

        customer_id = self.customer_id

        customer_session = self.customer_session

        invoice_address_id = self.invoice_address_id

        delivery_address_id = self.delivery_address_id

        show_net_prices = self.show_net_prices

        payment_only = self.payment_only

        force_payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.force_payment_method, Unset):
            force_payment_method = self.force_payment_method.value

        basket_id = self.basket_id

        allow_multiple_purchases = self.allow_multiple_purchases

        start_with_voucher_input = self.start_with_voucher_input

        hide_voucher_input = self.hide_voucher_input

        allowed_payment_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_payment_methods, Unset):
            allowed_payment_methods = []
            for allowed_payment_methods_item_data in self.allowed_payment_methods:
                allowed_payment_methods_item = allowed_payment_methods_item_data.value
                allowed_payment_methods.append(allowed_payment_methods_item)

        language = self.language

        debug_mode = self.debug_mode

        subscription_start_date: Union[None, Unset, str]
        if isinstance(self.subscription_start_date, Unset):
            subscription_start_date = UNSET
        elif isinstance(self.subscription_start_date, datetime.datetime):
            subscription_start_date = self.subscription_start_date.isoformat()
        else:
            subscription_start_date = self.subscription_start_date

        address_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_settings, Unset):
            address_settings = self.address_settings.to_dict()

        gift_option: Union[Unset, str] = UNSET
        if not isinstance(self.gift_option, Unset):
            gift_option = self.gift_option.value

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        voucher_code = self.voucher_code

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        connected_offer_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.connected_offer_items, Unset):
            connected_offer_items = []
            for connected_offer_items_item_data in self.connected_offer_items:
                connected_offer_items_item = connected_offer_items_item_data.to_dict()
                connected_offer_items.append(connected_offer_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerIpAddress": customer_ip_address,
            }
        )
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_session is not UNSET:
            field_dict["customerSession"] = customer_session
        if invoice_address_id is not UNSET:
            field_dict["invoiceAddressId"] = invoice_address_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id
        if show_net_prices is not UNSET:
            field_dict["showNetPrices"] = show_net_prices
        if payment_only is not UNSET:
            field_dict["paymentOnly"] = payment_only
        if force_payment_method is not UNSET:
            field_dict["forcePaymentMethod"] = force_payment_method
        if basket_id is not UNSET:
            field_dict["basketId"] = basket_id
        if allow_multiple_purchases is not UNSET:
            field_dict["allowMultiplePurchases"] = allow_multiple_purchases
        if start_with_voucher_input is not UNSET:
            field_dict["startWithVoucherInput"] = start_with_voucher_input
        if hide_voucher_input is not UNSET:
            field_dict["hideVoucherInput"] = hide_voucher_input
        if allowed_payment_methods is not UNSET:
            field_dict["allowedPaymentMethods"] = allowed_payment_methods
        if language is not UNSET:
            field_dict["language"] = language
        if debug_mode is not UNSET:
            field_dict["debugMode"] = debug_mode
        if subscription_start_date is not UNSET:
            field_dict["subscriptionStartDate"] = subscription_start_date
        if address_settings is not UNSET:
            field_dict["addressSettings"] = address_settings
        if gift_option is not UNSET:
            field_dict["giftOption"] = gift_option
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if voucher_code is not UNSET:
            field_dict["voucherCode"] = voucher_code
        if items is not UNSET:
            field_dict["items"] = items
        if connected_offer_items is not UNSET:
            field_dict["connectedOfferItems"] = connected_offer_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_order_data import AdditionalOrderData
        from ..models.checkout_address_settings import CheckoutAddressSettings
        from ..models.checkout_offer import CheckoutOffer
        from ..models.connected_offer_request import ConnectedOfferRequest

        d = src_dict.copy()
        customer_ip_address = d.pop("customerIpAddress")

        customer_id = d.pop("customerId", UNSET)

        customer_session = d.pop("customerSession", UNSET)

        invoice_address_id = d.pop("invoiceAddressId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        show_net_prices = d.pop("showNetPrices", UNSET)

        payment_only = d.pop("paymentOnly", UNSET)

        _force_payment_method = d.pop("forcePaymentMethod", UNSET)
        force_payment_method: Union[Unset, CheckoutPreparationForcePaymentMethod]
        if isinstance(_force_payment_method, Unset):
            force_payment_method = UNSET
        else:
            force_payment_method = CheckoutPreparationForcePaymentMethod(_force_payment_method)

        basket_id = d.pop("basketId", UNSET)

        allow_multiple_purchases = d.pop("allowMultiplePurchases", UNSET)

        start_with_voucher_input = d.pop("startWithVoucherInput", UNSET)

        hide_voucher_input = d.pop("hideVoucherInput", UNSET)

        allowed_payment_methods = []
        _allowed_payment_methods = d.pop("allowedPaymentMethods", UNSET)
        for allowed_payment_methods_item_data in _allowed_payment_methods or []:
            allowed_payment_methods_item = CheckoutPreparationAllowedPaymentMethodsItem(
                allowed_payment_methods_item_data
            )

            allowed_payment_methods.append(allowed_payment_methods_item)

        language = d.pop("language", UNSET)

        debug_mode = d.pop("debugMode", UNSET)

        def _parse_subscription_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_start_date_type_0 = isoparse(data)

                return subscription_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        subscription_start_date = _parse_subscription_start_date(d.pop("subscriptionStartDate", UNSET))

        _address_settings = d.pop("addressSettings", UNSET)
        address_settings: Union[Unset, CheckoutAddressSettings]
        if isinstance(_address_settings, Unset):
            address_settings = UNSET
        else:
            address_settings = CheckoutAddressSettings.from_dict(_address_settings)

        _gift_option = d.pop("giftOption", UNSET)
        gift_option: Union[Unset, CheckoutPreparationGiftOption]
        if isinstance(_gift_option, Unset):
            gift_option = UNSET
        else:
            gift_option = CheckoutPreparationGiftOption(_gift_option)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, AdditionalOrderData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = AdditionalOrderData.from_dict(_additional_data)

        voucher_code = d.pop("voucherCode", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CheckoutOffer.from_dict(items_item_data)

            items.append(items_item)

        connected_offer_items = []
        _connected_offer_items = d.pop("connectedOfferItems", UNSET)
        for connected_offer_items_item_data in _connected_offer_items or []:
            connected_offer_items_item = ConnectedOfferRequest.from_dict(connected_offer_items_item_data)

            connected_offer_items.append(connected_offer_items_item)

        checkout_preparation = cls(
            customer_ip_address=customer_ip_address,
            customer_id=customer_id,
            customer_session=customer_session,
            invoice_address_id=invoice_address_id,
            delivery_address_id=delivery_address_id,
            show_net_prices=show_net_prices,
            payment_only=payment_only,
            force_payment_method=force_payment_method,
            basket_id=basket_id,
            allow_multiple_purchases=allow_multiple_purchases,
            start_with_voucher_input=start_with_voucher_input,
            hide_voucher_input=hide_voucher_input,
            allowed_payment_methods=allowed_payment_methods,
            language=language,
            debug_mode=debug_mode,
            subscription_start_date=subscription_start_date,
            address_settings=address_settings,
            gift_option=gift_option,
            additional_data=additional_data,
            voucher_code=voucher_code,
            items=items,
            connected_offer_items=connected_offer_items,
        )

        checkout_preparation.additional_properties = d
        return checkout_preparation

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
