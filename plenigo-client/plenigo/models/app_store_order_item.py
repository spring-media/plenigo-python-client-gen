import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_store_response import AmazonAppStoreResponse
    from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
    from ..models.google_play_product_purchase import GooglePlayProductPurchase
    from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase


T = TypeVar("T", bound="AppStoreOrderItem")


@attr.s(auto_attribs=True)
class AppStoreOrderItem:
    """
    Attributes:
        position (Union[Unset, datetime.datetime]): date time the order was created with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        delivery_customer_id (Union[Unset, str]): id of the customer the delivery belongs to (also includes digital
            products)
        product_id (Union[Unset, str]): product id
        app_store_subscription_id (Union[Unset, int]): unique identifier for the app store subscription that is
            associated with this item
        access_right_unique_id (Union[Unset, str]): unique id of the access right this order item grants access to
        additional_store_item_data (Union['AmazonAppStoreResponse', 'AppleAppStoreReceiptItem',
            'GooglePlayProductPurchase', 'GooglePlaySubscriptionPurchase', Unset]): contains the app receipt data
    """

    position: Union[Unset, datetime.datetime] = UNSET
    delivery_customer_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    app_store_subscription_id: Union[Unset, int] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    additional_store_item_data: Union[
        "AmazonAppStoreResponse",
        "AppleAppStoreReceiptItem",
        "GooglePlayProductPurchase",
        "GooglePlaySubscriptionPurchase",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.isoformat()

        delivery_customer_id = self.delivery_customer_id
        product_id = self.product_id
        app_store_subscription_id = self.app_store_subscription_id
        access_right_unique_id = self.access_right_unique_id
        additional_store_item_data: Union[Dict[str, Any], Unset]
        if isinstance(self.additional_store_item_data, Unset):
            additional_store_item_data = UNSET

        elif isinstance(self.additional_store_item_data, AppleAppStoreReceiptItem):
            additional_store_item_data = UNSET
            if not isinstance(self.additional_store_item_data, Unset):
                additional_store_item_data = self.additional_store_item_data.to_dict()

        elif isinstance(self.additional_store_item_data, GooglePlaySubscriptionPurchase):
            additional_store_item_data = UNSET
            if not isinstance(self.additional_store_item_data, Unset):
                additional_store_item_data = self.additional_store_item_data.to_dict()

        elif isinstance(self.additional_store_item_data, GooglePlayProductPurchase):
            additional_store_item_data = UNSET
            if not isinstance(self.additional_store_item_data, Unset):
                additional_store_item_data = self.additional_store_item_data.to_dict()

        else:
            additional_store_item_data = UNSET
            if not isinstance(self.additional_store_item_data, Unset):
                additional_store_item_data = self.additional_store_item_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if delivery_customer_id is not UNSET:
            field_dict["deliveryCustomerId"] = delivery_customer_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if app_store_subscription_id is not UNSET:
            field_dict["appStoreSubscriptionId"] = app_store_subscription_id
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id
        if additional_store_item_data is not UNSET:
            field_dict["additionalStoreItemData"] = additional_store_item_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_app_store_response import AmazonAppStoreResponse
        from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        d = src_dict.copy()
        _position = d.pop("position", UNSET)
        position: Union[Unset, datetime.datetime]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = isoparse(_position)

        delivery_customer_id = d.pop("deliveryCustomerId", UNSET)

        product_id = d.pop("productId", UNSET)

        app_store_subscription_id = d.pop("appStoreSubscriptionId", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        def _parse_additional_store_item_data(
            data: object,
        ) -> Union[
            "AmazonAppStoreResponse",
            "AppleAppStoreReceiptItem",
            "GooglePlayProductPurchase",
            "GooglePlaySubscriptionPurchase",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_item_data_type_0 = data
                additional_store_item_data_type_0: Union[Unset, AppleAppStoreReceiptItem]
                if isinstance(_additional_store_item_data_type_0, Unset):
                    additional_store_item_data_type_0 = UNSET
                else:
                    additional_store_item_data_type_0 = AppleAppStoreReceiptItem.from_dict(
                        _additional_store_item_data_type_0
                    )

                return additional_store_item_data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_item_data_type_1 = data
                additional_store_item_data_type_1: Union[Unset, GooglePlaySubscriptionPurchase]
                if isinstance(_additional_store_item_data_type_1, Unset):
                    additional_store_item_data_type_1 = UNSET
                else:
                    additional_store_item_data_type_1 = GooglePlaySubscriptionPurchase.from_dict(
                        _additional_store_item_data_type_1
                    )

                return additional_store_item_data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_item_data_type_2 = data
                additional_store_item_data_type_2: Union[Unset, GooglePlayProductPurchase]
                if isinstance(_additional_store_item_data_type_2, Unset):
                    additional_store_item_data_type_2 = UNSET
                else:
                    additional_store_item_data_type_2 = GooglePlayProductPurchase.from_dict(
                        _additional_store_item_data_type_2
                    )

                return additional_store_item_data_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _additional_store_item_data_type_3 = data
            additional_store_item_data_type_3: Union[Unset, AmazonAppStoreResponse]
            if isinstance(_additional_store_item_data_type_3, Unset):
                additional_store_item_data_type_3 = UNSET
            else:
                additional_store_item_data_type_3 = AmazonAppStoreResponse.from_dict(_additional_store_item_data_type_3)

            return additional_store_item_data_type_3

        additional_store_item_data = _parse_additional_store_item_data(d.pop("additionalStoreItemData", UNSET))

        app_store_order_item = cls(
            position=position,
            delivery_customer_id=delivery_customer_id,
            product_id=product_id,
            app_store_subscription_id=app_store_subscription_id,
            access_right_unique_id=access_right_unique_id,
            additional_store_item_data=additional_store_item_data,
        )

        app_store_order_item.additional_properties = d
        return app_store_order_item

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
