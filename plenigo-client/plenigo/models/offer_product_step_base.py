from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferProductStepBase")


@_attrs_define
class OfferProductStepBase:
    """
    Attributes:
        position (int): position inside the product
        product_contract_id (Union[Unset, int]): id of the product contract associated with this step
    """

    position: int
    product_contract_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        product_contract_id = self.product_contract_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )
        if product_contract_id is not UNSET:
            field_dict["productContractId"] = product_contract_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        product_contract_id = d.pop("productContractId", UNSET)

        offer_product_step_base = cls(
            position=position,
            product_contract_id=product_contract_id,
        )

        offer_product_step_base.additional_properties = d
        return offer_product_step_base

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
