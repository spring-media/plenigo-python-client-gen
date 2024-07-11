from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_purchase_detail import AppStorePurchaseDetail


T = TypeVar("T", bound="AppStorePurchase")


@_attrs_define
class AppStorePurchase:
    """
    Attributes:
        customer_id (Union[Unset, str]): id of the customer purchase is associated with - only set if purchase is
            already associated
        token (Union[Unset, str]): token that uniquely identifies this purchase and is used for further API requests
        has_orders (Union[Unset, bool]): flag indicating if purchase has orders
        orders (Union[Unset, List['AppStorePurchaseDetail']]):
    """

    customer_id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    has_orders: Union[Unset, bool] = UNSET
    orders: Union[Unset, List["AppStorePurchaseDetail"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        token = self.token

        has_orders = self.has_orders

        orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if token is not UNSET:
            field_dict["token"] = token
        if has_orders is not UNSET:
            field_dict["hasOrders"] = has_orders
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_store_purchase_detail import AppStorePurchaseDetail

        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        token = d.pop("token", UNSET)

        has_orders = d.pop("hasOrders", UNSET)

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = AppStorePurchaseDetail.from_dict(orders_item_data)

            orders.append(orders_item)

        app_store_purchase = cls(
            customer_id=customer_id,
            token=token,
            has_orders=has_orders,
            orders=orders,
        )

        app_store_purchase.additional_properties = d
        return app_store_purchase

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
