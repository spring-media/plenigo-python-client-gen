from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_voucher import ApiVoucher


T = TypeVar("T", bound="ApiVoucherPage")


@_attrs_define
class ApiVoucherPage:
    """
    Attributes:
        starting_after_id (Union[Unset, int]): The ID to start retrieving vouchers after.
        items (Union[Unset, List['ApiVoucher']]): A list of voucher items.
    """

    starting_after_id: Union[Unset, int] = UNSET
    items: Union[Unset, List["ApiVoucher"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        starting_after_id = self.starting_after_id

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if starting_after_id is not UNSET:
            field_dict["startingAfterId"] = starting_after_id
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_voucher import ApiVoucher

        d = src_dict.copy()
        starting_after_id = d.pop("startingAfterId", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiVoucher.from_dict(items_item_data)

            items.append(items_item)

        api_voucher_page = cls(
            starting_after_id=starting_after_id,
            items=items,
        )

        api_voucher_page.additional_properties = d
        return api_voucher_page

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
