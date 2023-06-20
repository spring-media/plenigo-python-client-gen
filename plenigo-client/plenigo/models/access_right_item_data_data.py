from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.access_right_item_data_data_additional_property import AccessRightItemDataDataAdditionalProperty


T = TypeVar("T", bound="AccessRightItemDataData")


@attr.s(auto_attribs=True)
class AccessRightItemDataData:
    """ """

    additional_properties: Dict[str, "AccessRightItemDataDataAdditionalProperty"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_right_item_data_data_additional_property import AccessRightItemDataDataAdditionalProperty

        d = src_dict.copy()
        access_right_item_data_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AccessRightItemDataDataAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        access_right_item_data_data.additional_properties = additional_properties
        return access_right_item_data_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AccessRightItemDataDataAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AccessRightItemDataDataAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
