from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_import import OrderImport


T = TypeVar("T", bound="OrderImports")


@_attrs_define
class OrderImports:
    """
    Attributes:
        purchase (Union[Unset, bool]): flag indicating if import should be handled as a purchase
        suppress_mail (Union[Unset, bool]): flag indicating if the sending of mails should be suppressed
        items (Union[Unset, List['OrderImport']]):
    """

    purchase: Union[Unset, bool] = UNSET
    suppress_mail: Union[Unset, bool] = UNSET
    items: Union[Unset, List["OrderImport"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase = self.purchase

        suppress_mail = self.suppress_mail

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase is not UNSET:
            field_dict["purchase"] = purchase
        if suppress_mail is not UNSET:
            field_dict["suppressMail"] = suppress_mail
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_import import OrderImport

        d = src_dict.copy()
        purchase = d.pop("purchase", UNSET)

        suppress_mail = d.pop("suppressMail", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = OrderImport.from_dict(items_item_data)

            items.append(items_item)

        order_imports = cls(
            purchase=purchase,
            suppress_mail=suppress_mail,
            items=items,
        )

        order_imports.additional_properties = d
        return order_imports

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
