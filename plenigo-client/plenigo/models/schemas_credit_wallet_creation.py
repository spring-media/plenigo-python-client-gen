from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemasCreditWalletCreation")


@_attrs_define
class SchemasCreditWalletCreation:
    """
    Attributes:
        unique_id (Union[Unset, str]): unique id of the wallet for identification
        credit_count (Union[Unset, int]): credit count to create wallet with
        customer_id (Union[Unset, str]): unique id of the customer the credit wallet belongs to
    """

    unique_id: Union[Unset, str] = UNSET
    credit_count: Union[Unset, int] = UNSET
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_id = self.unique_id

        credit_count = self.credit_count

        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_id = d.pop("uniqueId", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        customer_id = d.pop("customerId", UNSET)

        schemas_credit_wallet_creation = cls(
            unique_id=unique_id,
            credit_count=credit_count,
            customer_id=customer_id,
        )

        schemas_credit_wallet_creation.additional_properties = d
        return schemas_credit_wallet_creation

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
