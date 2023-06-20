from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_data import AccessRightItemData


T = TypeVar("T", bound="AccessRightData")


@attr.s(auto_attribs=True)
class AccessRightData:
    """
    Attributes:
        customer_id (Union[Unset, str]): unique id of the customer the access right belongs to
        customer_blocked (Union[Unset, bool]): flag indicating if customer is blocked completely
        items (Union[Unset, List['AccessRightItemData']]):
    """

    customer_id: Union[Unset, str] = UNSET
    customer_blocked: Union[Unset, bool] = UNSET
    items: Union[Unset, List["AccessRightItemData"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        customer_blocked = self.customer_blocked
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_blocked is not UNSET:
            field_dict["customerBlocked"] = customer_blocked
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_right_item_data import AccessRightItemData

        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        customer_blocked = d.pop("customerBlocked", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = AccessRightItemData.from_dict(items_item_data)

            items.append(items_item)

        access_right_data = cls(
            customer_id=customer_id,
            customer_blocked=customer_blocked,
            items=items,
        )

        access_right_data.additional_properties = d
        return access_right_data

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
