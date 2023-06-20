from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutOrderIdResult")


@attr.s(auto_attribs=True)
class CheckoutOrderIdResult:
    """
    Attributes:
        order_id (Union[Unset, int]): unique id of the order
    """

    order_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        checkout_order_id_result = cls(
            order_id=order_id,
        )

        checkout_order_id_result.additional_properties = d
        return checkout_order_id_result

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
