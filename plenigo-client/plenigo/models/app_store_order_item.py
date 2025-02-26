import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
    from ..models.google_play_product_purchase import GooglePlayProductPurchase
    from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase


T = TypeVar("T", bound="AppStoreOrderItem")


@_attrs_define
class AppStoreOrderItem:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        position (Union[Unset, int]): position of the app store order item inside the app store order - creates a unique
            app store order item id in combination with the appStoreOrderId
        delivery_customer_id (Union[Unset, str]): id of the customer the delivery belongs to (also includes digital
            products)
        product_id (Union[Unset, str]): product id
        app_store_subscription_id (Union[Unset, int]): unique identifier for the app store subscription that is
            associated with this item
        access_right_unique_id (Union[Unset, str]): unique id of the access right this order item grants access to
        additional_store_item_data (Union['AppleAppStoreReceiptItem', 'GooglePlayProductPurchase',
            'GooglePlaySubscriptionPurchase', Unset]): contains the app receipt data
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    position: Union[Unset, int] = UNSET
    delivery_customer_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    app_store_subscription_id: Union[Unset, int] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    additional_store_item_data: Union[
        "AppleAppStoreReceiptItem", "GooglePlayProductPurchase", "GooglePlaySubscriptionPurchase", Unset
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

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

        position = self.position

        delivery_customer_id = self.delivery_customer_id

        product_id = self.product_id

        app_store_subscription_id = self.app_store_subscription_id

        access_right_unique_id = self.access_right_unique_id

        additional_store_item_data: Union[Unset, dict[str, Any]]
        if isinstance(self.additional_store_item_data, Unset) or self.additional_store_item_data is None:
            additional_store_item_data = UNSET
        elif isinstance(self.additional_store_item_data, AppleAppStoreReceiptItem):
            additional_store_item_data = self.additional_store_item_data.to_dict()
        elif isinstance(self.additional_store_item_data, GooglePlaySubscriptionPurchase):
            additional_store_item_data = self.additional_store_item_data.to_dict()
        else:
            additional_store_item_data = self.additional_store_item_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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
        from ..models.apple_app_store_receipt_item import AppleAppStoreReceiptItem
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        d = src_dict.copy()

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

        position = d.pop("position", UNSET)

        delivery_customer_id = d.pop("deliveryCustomerId", UNSET)

        product_id = d.pop("productId", UNSET)

        app_store_subscription_id = d.pop("appStoreSubscriptionId", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        def _parse_additional_store_item_data(
            data: object
        ) -> Union["AppleAppStoreReceiptItem", "GooglePlayProductPurchase", "GooglePlaySubscriptionPurchase", Unset]:
            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as AppleAppStoreReceiptItem
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_store_item_data_type_0 = AppleAppStoreReceiptItem.from_dict(data)

                return additional_store_item_data_type_0
            except:  # noqa: E722
                pass

            # Try to parse the data as GooglePlaySubscriptionPurchase
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_store_item_data_type_1 = GooglePlaySubscriptionPurchase.from_dict(data)

                return additional_store_item_data_type_1
            except:  # noqa: E722
                pass

            # In order to parse the one remaining property in the union,
            # data must be a dict
            if not isinstance(data, dict):
                raise TypeError()

            # Finally, parse the data as GooglePlayProductPurchase
            additional_store_item_data_type_2 = GooglePlayProductPurchase.from_dict(data)

            return additional_store_item_data_type_2

        additional_store_item_data = _parse_additional_store_item_data(d.pop("additionalStoreItemData", UNSET))

        app_store_order_item = cls(
            created_date=created_date,
            changed_date=changed_date,
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
