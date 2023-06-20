from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmazonAppStorePurchaseAddition")


@attr.s(auto_attribs=True)
class AmazonAppStorePurchaseAddition:
    """
    Attributes:
        user_id (Union[Unset, str]): Amazon user id
        receipt_ids (Union[Unset, List[str]]):
    """

    user_id: Union[Unset, str] = UNSET
    receipt_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        receipt_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.receipt_ids, Unset):
            receipt_ids = self.receipt_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if receipt_ids is not UNSET:
            field_dict["receiptIds"] = receipt_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        receipt_ids = cast(List[str], d.pop("receiptIds", UNSET))

        amazon_app_store_purchase_addition = cls(
            user_id=user_id,
            receipt_ids=receipt_ids,
        )

        amazon_app_store_purchase_addition.additional_properties = d
        return amazon_app_store_purchase_addition

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
