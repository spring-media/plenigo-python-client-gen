from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostCenterCreation")


@attr.s(auto_attribs=True)
class CostCenterCreation:
    """
    Attributes:
        cost_center (str): Cost center value of the cost center
        description (Union[Unset, str]): description of the cost center
        short_description (Union[Unset, str]): short description of the cost center
    """

    cost_center: str
    description: Union[Unset, str] = UNSET
    short_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center
        description = self.description
        short_description = self.short_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costCenter": cost_center,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center = d.pop("costCenter")

        description = d.pop("description", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        cost_center_creation = cls(
            cost_center=cost_center,
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
