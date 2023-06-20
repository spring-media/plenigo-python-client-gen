from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.product_access_right_creation_additional_data_additional_property import (
        ProductAccessRightCreationAdditionalDataAdditionalProperty,
    )


T = TypeVar("T", bound="ProductAccessRightCreationAdditionalData")


@attr.s(auto_attribs=True)
class ProductAccessRightCreationAdditionalData:
    """ """

    additional_properties: Dict[str, "ProductAccessRightCreationAdditionalDataAdditionalProperty"] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_access_right_creation_additional_data_additional_property import (
            ProductAccessRightCreationAdditionalDataAdditionalProperty,
        )

        d = src_dict.copy()
        product_access_right_creation_additional_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProductAccessRightCreationAdditionalDataAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        product_access_right_creation_additional_data.additional_properties = additional_properties
        return product_access_right_creation_additional_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ProductAccessRightCreationAdditionalDataAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ProductAccessRightCreationAdditionalDataAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
