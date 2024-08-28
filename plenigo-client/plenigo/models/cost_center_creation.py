from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostCenterCreation")


@_attrs_define
class CostCenterCreation:
    """
    Attributes:
        cost_center (Union[Unset, str]): Cost center value of the cost center
        purchase_number (Union[Unset, str]): Purchase number to use
        description (Union[Unset, str]): description of the cost center
        short_description (Union[Unset, str]): short description of the cost center
    """

    cost_center: Union[Unset, str] = UNSET
    purchase_number: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    short_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        purchase_number = self.purchase_number

        description = self.description

        short_description = self.short_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if purchase_number is not UNSET:
            field_dict["purchaseNumber"] = purchase_number
        if description is not UNSET:
            field_dict["description"] = description
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center = d.pop("costCenter", UNSET)

        purchase_number = d.pop("purchaseNumber", UNSET)

        description = d.pop("description", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        cost_center_creation = cls(
            cost_center=cost_center,
            purchase_number=purchase_number,
            description=description,
            short_description=short_description,
        )

        cost_center_creation.additional_properties = d
        return cost_center_creation

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
