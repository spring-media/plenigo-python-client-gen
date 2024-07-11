from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GooglePlayStorePurchaseAdditionElement")


@_attrs_define
class GooglePlayStorePurchaseAdditionElement:
    """
    Attributes:
        product_id (Union[Unset, str]): the purchased ID (for example, 'monthly001').
        subscription (Union[Unset, bool]): flag indicating if purchase is a subscription or a single product purchase
        purchase_token (Union[Unset, str]): token provided to the customer's device when the purchase was done
    """

    product_id: Union[Unset, str] = UNSET
    subscription: Union[Unset, bool] = UNSET
    purchase_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        subscription = self.subscription

        purchase_token = self.purchase_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if purchase_token is not UNSET:
            field_dict["purchaseToken"] = purchase_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("productId", UNSET)

        subscription = d.pop("subscription", UNSET)

        purchase_token = d.pop("purchaseToken", UNSET)

        google_play_store_purchase_addition_element = cls(
            product_id=product_id,
            subscription=subscription,
            purchase_token=purchase_token,
        )

        google_play_store_purchase_addition_element.additional_properties = d
        return google_play_store_purchase_addition_element

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
