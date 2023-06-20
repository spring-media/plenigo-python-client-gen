from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_tag_creation_category import ProductTagCreationCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductTagCreation")


@attr.s(auto_attribs=True)
class ProductTagCreation:
    """
    Attributes:
        category (ProductTagCreationCategory): category that reflects the usage of the tag
        name (Union[Unset, str]): a name that is unique in combination with a category
        description (Union[Unset, str]): internal description of the product tag
    """

    category: ProductTagCreationCategory
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.value

        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = ProductTagCreationCategory(d.pop("category"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        product_tag_creation = cls(
            category=category,
            name=name,
            description=description,
        )

        product_tag_creation.additional_properties = d
        return product_tag_creation

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
