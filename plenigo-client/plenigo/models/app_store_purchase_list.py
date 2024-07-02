from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_purchase import AppStorePurchase


T = TypeVar("T", bound="AppStorePurchaseList")


@_attrs_define
class AppStorePurchaseList:
    """
    Attributes:
        purchases (Union[Unset, List['AppStorePurchase']]):
    """

    purchases: Union[Unset, List["AppStorePurchase"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchases, Unset):
            purchases = []
            for purchases_item_data in self.purchases:
                purchases_item = purchases_item_data.to_dict()
                purchases.append(purchases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchases is not UNSET:
            field_dict["purchases"] = purchases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_store_purchase import AppStorePurchase

        d = src_dict.copy()
        purchases = []
        _purchases = d.pop("purchases", UNSET)
        for purchases_item_data in _purchases or []:
            purchases_item = AppStorePurchase.from_dict(purchases_item_data)

            purchases.append(purchases_item)

        app_store_purchase_list = cls(
            purchases=purchases,
        )

        app_store_purchase_list.additional_properties = d
        return app_store_purchase_list

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
