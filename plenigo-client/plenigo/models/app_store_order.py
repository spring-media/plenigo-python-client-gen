import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.app_store_order_store_type import AppStoreOrderStoreType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_order_item import AppStoreOrderItem
    from ..models.apple_app_store_receipt import AppleAppStoreReceipt
    from ..models.google_play_product_purchase import GooglePlayProductPurchase
    from ..models.google_play_subscription_purchase import GooglePlaySubscriptionPurchase


T = TypeVar("T", bound="AppStoreOrder")


@_attrs_define
class AppStoreOrder:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): type of created by
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): type of changed by
        app_store_order_id (Union[Unset, int]): unique identifier for the app store order
        order_date (Union[None, Unset, datetime.datetime]): date time the order was created with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        customer_id (Union[Unset, str]): id of the customer the order belongs to
        store_type (Union[Unset, AppStoreOrderStoreType]): type of store
        additional_store_data (Union['AppleAppStoreReceipt', 'GooglePlayProductPurchase',
            'GooglePlaySubscriptionPurchase', Unset]): additional data of the app store
        items (Union[Unset, List['AppStoreOrderItem']]):
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    app_store_order_id: Union[Unset, int] = UNSET
    order_date: Union[None, Unset, datetime.datetime] = UNSET
    customer_id: Union[Unset, str] = UNSET
    store_type: Union[Unset, AppStoreOrderStoreType] = UNSET
    additional_store_data: Union[
        "AppleAppStoreReceipt", "GooglePlayProductPurchase", "GooglePlaySubscriptionPurchase", Unset
    ] = UNSET
    items: Union[Unset, List["AppStoreOrderItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.apple_app_store_receipt import AppleAppStoreReceipt
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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        app_store_order_id = self.app_store_order_id

        order_date: Union[None, Unset, str]
        if isinstance(self.order_date, Unset) or self.order_date is None:
            order_date = UNSET
        elif isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date

        customer_id = self.customer_id

        store_type: Union[Unset, str] = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type.value

        additional_store_data: Union[Dict[str, Any], Unset]
        if isinstance(self.additional_store_data, Unset) or self.additional_store_data is None:
            additional_store_data = UNSET
        elif isinstance(self.additional_store_data, AppleAppStoreReceipt):
            additional_store_data = self.additional_store_data.to_dict()
        elif isinstance(self.additional_store_data, GooglePlaySubscriptionPurchase):
            additional_store_data = self.additional_store_data.to_dict()
        else:
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
        if app_store_order_id is not UNSET:
            field_dict["appStoreOrderId"] = app_store_order_id
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
        from ..models.app_store_order_item import AppStoreOrderItem
        from ..models.apple_app_store_receipt import AppleAppStoreReceipt
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

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        app_store_order_id = d.pop("appStoreOrderId", UNSET)

        def _parse_order_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                order_date_type_1 = isoparse(data)

                return order_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        order_date = _parse_order_date(d.pop("orderDate", UNSET))

        customer_id = d.pop("customerId", UNSET)

        _store_type = d.pop("storeType", UNSET)
        store_type: Union[Unset, AppStoreOrderStoreType]
        if isinstance(_store_type, Unset) or not _store_type:
            store_type = UNSET
        else:
            store_type = AppStoreOrderStoreType(_store_type)

        def _parse_additional_store_data(
            data: object,
        ) -> Union["AppleAppStoreReceipt", "GooglePlayProductPurchase", "GooglePlaySubscriptionPurchase", Unset]:
            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as AppleAppStoreReceipt
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_store_data_type_0 = AppleAppStoreReceipt.from_dict(data)

                return additional_store_data_type_0
            except:  # noqa: E722
                pass

            # Try to parse the data as GooglePlaySubscriptionPurchase
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_store_data_type_1 = GooglePlaySubscriptionPurchase.from_dict(data)

                return additional_store_data_type_1
            except:  # noqa: E722
                pass

            # In order to parse the one remaining property in the union,
            # data must be a dict
            if not isinstance(data, dict):
                raise TypeError()

            # Finally, parse the data as GooglePlayProductPurchase
            additional_store_data_type_2 = GooglePlayProductPurchase.from_dict(data)

            return additional_store_data_type_2

        additional_store_data = _parse_additional_store_data(d.pop("additionalStoreData", UNSET))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = AppStoreOrderItem.from_dict(items_item_data)

            items.append(items_item)

        app_store_order = cls(
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            app_store_order_id=app_store_order_id,
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
