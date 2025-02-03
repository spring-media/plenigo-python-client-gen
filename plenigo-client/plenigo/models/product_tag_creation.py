from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_tag_creation_category import ProductTagCreationCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductTagCreation")


@_attrs_define
class ProductTagCreation:
    """
    Attributes:
        name (str): a name that is unique in combination with a category
        category (ProductTagCreationCategory): category that reflects the usage of the tag
        description (Union[Unset, str]): internal description of the product tag
    """

    name: str
    category: ProductTagCreationCategory
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        category = self.category.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "category": category,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        category = ProductTagCreationCategory(d.pop("category"))

        description = d.pop("description", UNSET)

        product_tag_creation = cls(
            name=name,
            category=category,
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
