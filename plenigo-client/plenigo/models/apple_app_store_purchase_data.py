from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apple_app_store_transaction import AppleAppStoreTransaction


T = TypeVar("T", bound="AppleAppStorePurchaseData")


@_attrs_define
class AppleAppStorePurchaseData:
    """
    Attributes:
        transactions (Union[Unset, List['AppleAppStoreTransaction']]):
    """

    transactions: Union[Unset, List["AppleAppStoreTransaction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apple_app_store_transaction import AppleAppStoreTransaction

        d = src_dict.copy()
        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = AppleAppStoreTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        apple_app_store_purchase_data = cls(
            transactions=transactions,
        )

        apple_app_store_purchase_data.additional_properties = d
        return apple_app_store_purchase_data

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
