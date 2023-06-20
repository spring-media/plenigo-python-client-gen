from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_access_right_creation_additional_data import ProductAccessRightCreationAdditionalData


T = TypeVar("T", bound="ProductAccessRightCreation")


@attr.s(auto_attribs=True)
class ProductAccessRightCreation:
    """
    Attributes:
        title (str): title of the access right
        unique_id (str): unique id of the access right within in the company
        description (Union[Unset, str]): internal description of the access right
        additional_data (Union[Unset, ProductAccessRightCreationAdditionalData]):
    """

    title: str
    unique_id: str
    description: Union[Unset, str] = UNSET
    additional_data: Union[Unset, "ProductAccessRightCreationAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        unique_id = self.unique_id
        description = self.description
        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "uniqueId": unique_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_access_right_creation_additional_data import ProductAccessRightCreationAdditionalData

        d = src_dict.copy()
        title = d.pop("title")

        unique_id = d.pop("uniqueId")

        description = d.pop("description", UNSET)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, ProductAccessRightCreationAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = ProductAccessRightCreationAdditionalData.from_dict(_additional_data)

        product_access_right_creation = cls(
            title=title,
            unique_id=unique_id,
            description=description,
            additional_data=additional_data,
        )

        product_access_right_creation.additional_properties = d
        return product_access_right_creation

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
