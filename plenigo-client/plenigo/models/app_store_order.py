import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.app_store_order_store_type import AppStoreOrderStoreType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_store_response import AmazonAppStoreResponse
    from ..models.app_store_order_item import AppStoreOrderItem
    from ..models.apple_app_store_receipt import AppleAppStoreReceipt
    from ..models.google_play_product_purchase import GooglePlayProductPurchase
    from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase


T = TypeVar("T", bound="AppStoreOrder")


@attr.s(auto_attribs=True)
class AppStoreOrder:
    """
    Attributes:
        app_store_order_id (Union[Unset, int]): unique identifier for the app store order
        changed_date (Union[Unset, datetime.datetime]): date the transaction was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        order_date (Union[Unset, datetime.datetime]): date time the order was created with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        customer_id (Union[Unset, str]): id of the customer the order belongs to
        store_type (Union[Unset, AppStoreOrderStoreType]): type of store
        additional_store_data (Union['AmazonAppStoreResponse', 'AppleAppStoreReceipt', 'GooglePlayProductPurchase',
            'GooglePlaySubscriptionPurchase', Unset]): additional data of the app store
        items (Union[Unset, List['AppStoreOrderItem']]):
    """

    app_store_order_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    order_date: Union[Unset, datetime.datetime] = UNSET
    customer_id: Union[Unset, str] = UNSET
    store_type: Union[Unset, AppStoreOrderStoreType] = UNSET
    additional_store_data: Union[
        "AmazonAppStoreResponse",
        "AppleAppStoreReceipt",
        "GooglePlayProductPurchase",
        "GooglePlaySubscriptionPurchase",
        Unset,
    ] = UNSET
    items: Union[Unset, List["AppStoreOrderItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.apple_app_store_receipt import AppleAppStoreReceipt
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        app_store_order_id = self.app_store_order_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        order_date: Union[Unset, str] = UNSET
        if not isinstance(self.order_date, Unset):
            order_date = self.order_date.isoformat()

        customer_id = self.customer_id
        store_type: Union[Unset, str] = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type.value

        additional_store_data: Union[Dict[str, Any], Unset]
        if isinstance(self.additional_store_data, Unset):
            additional_store_data = UNSET

        elif isinstance(self.additional_store_data, AppleAppStoreReceipt):
            additional_store_data = UNSET
            if not isinstance(self.additional_store_data, Unset):
                additional_store_data = self.additional_store_data.to_dict()

        elif isinstance(self.additional_store_data, GooglePlaySubscriptionPurchase):
            additional_store_data = UNSET
            if not isinstance(self.additional_store_data, Unset):
                additional_store_data = self.additional_store_data.to_dict()

        elif isinstance(self.additional_store_data, GooglePlayProductPurchase):
            additional_store_data = UNSET
            if not isinstance(self.additional_store_data, Unset):
                additional_store_data = self.additional_store_data.to_dict()

        else:
            additional_store_data = UNSET
            if not isinstance(self.additional_store_data, Unset):
                additional_store_data = self.additional_store_data.to_dict()

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_store_order_id is not UNSET:
            field_dict["appStoreOrderId"] = app_store_order_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if additional_store_data is not UNSET:
            field_dict["additionalStoreData"] = additional_store_data
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_app_store_response import AmazonAppStoreResponse
        from ..models.app_store_order_item import AppStoreOrderItem
        from ..models.apple_app_store_receipt import AppleAppStoreReceipt
        from ..models.google_play_product_purchase import GooglePlayProductPurchase
        from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase

        d = src_dict.copy()
        app_store_order_id = d.pop("appStoreOrderId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        _order_date = d.pop("orderDate", UNSET)
        order_date: Union[Unset, datetime.datetime]
        if isinstance(_order_date, Unset):
            order_date = UNSET
        else:
            order_date = isoparse(_order_date)

        customer_id = d.pop("customerId", UNSET)

        _store_type = d.pop("storeType", UNSET)
        store_type: Union[Unset, AppStoreOrderStoreType]
        if isinstance(_store_type, Unset):
            store_type = UNSET
        else:
            store_type = AppStoreOrderStoreType(_store_type)

        def _parse_additional_store_data(
            data: object,
        ) -> Union[
            "AmazonAppStoreResponse",
            "AppleAppStoreReceipt",
            "GooglePlayProductPurchase",
            "GooglePlaySubscriptionPurchase",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_data_type_0 = data
                additional_store_data_type_0: Union[Unset, AppleAppStoreReceipt]
                if isinstance(_additional_store_data_type_0, Unset):
                    additional_store_data_type_0 = UNSET
                else:
                    additional_store_data_type_0 = AppleAppStoreReceipt.from_dict(_additional_store_data_type_0)

                return additional_store_data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_data_type_1 = data
                additional_store_data_type_1: Union[Unset, GooglePlaySubscriptionPurchase]
                if isinstance(_additional_store_data_type_1, Unset):
                    additional_store_data_type_1 = UNSET
                else:
                    additional_store_data_type_1 = GooglePlaySubscriptionPurchase.from_dict(
                        _additional_store_data_type_1
                    )

                return additional_store_data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_store_data_type_2 = data
                additional_store_data_type_2: Union[Unset, GooglePlayProductPurchase]
                if isinstance(_additional_store_data_type_2, Unset):
                    additional_store_data_type_2 = UNSET
                else:
                    additional_store_data_type_2 = GooglePlayProductPurchase.from_dict(_additional_store_data_type_2)

                return additional_store_data_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _additional_store_data_type_3 = data
            additional_store_data_type_3: Union[Unset, AmazonAppStoreResponse]
            if isinstance(_additional_store_data_type_3, Unset):
                additional_store_data_type_3 = UNSET
            else:
                additional_store_data_type_3 = AmazonAppStoreResponse.from_dict(_additional_store_data_type_3)

            return additional_store_data_type_3

        additional_store_data = _parse_additional_store_data(d.pop("additionalStoreData", UNSET))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = AppStoreOrderItem.from_dict(items_item_data)

            items.append(items_item)

        app_store_order = cls(
            app_store_order_id=app_store_order_id,
            changed_date=changed_date,
            order_date=order_date,
            customer_id=customer_id,
            store_type=store_type,
            additional_store_data=additional_store_data,
            items=items,
        )

        app_store_order.additional_properties = d
        return app_store_order

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
