from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_data_selection_values import AdditionalDataSelectionValues


T = TypeVar("T", bound="AdditionalDataSelection")


@attr.s(auto_attribs=True)
class AdditionalDataSelection:
    """
    Attributes:
        title (str): title that identfies the selection itself
        identifier (Any): identifier used as additional data keys
        values (AdditionalDataSelectionValues):
        description (Union[Unset, Any]): description provided to the merchant user for the addtional data selection
        category (Union[Unset, Any]): free field to be able to categorize the data selections
        enabled (Union[Unset, bool]): flag indicating if selection is active
    """

    title: str
    identifier: Any
    values: "AdditionalDataSelectionValues"
    description: Union[Unset, Any] = UNSET
    category: Union[Unset, Any] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        identifier = self.identifier
        values = self.values.to_dict()

        description = self.description
        category = self.category
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "identifier": identifier,
                "values": values,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_data_selection_values import AdditionalDataSelectionValues

        d = src_dict.copy()
        title = d.pop("title")

        identifier = d.pop("identifier")

        values = AdditionalDataSelectionValues.from_dict(d.pop("values"))

        description = d.pop("description", UNSET)

        category = d.pop("category", UNSET)

        enabled = d.pop("enabled", UNSET)

        additional_data_selection = cls(
            title=title,
            identifier=identifier,
            values=values,
            description=description,
            category=category,
            enabled=enabled,
        )

        additional_data_selection.additional_properties = d
        return additional_data_selection

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
