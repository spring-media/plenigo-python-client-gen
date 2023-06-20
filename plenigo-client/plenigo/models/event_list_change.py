from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventListChange")


@attr.s(auto_attribs=True)
class EventListChange:
    """
    Attributes:
        title (str): title of the event list
        description (Union[Unset, str]): description of the event list
        unique_id (Union[Unset, str]): unique id of the event list for identification
        enabled (Union[Unset, bool]): flag indicating if event list is active
    """

    title: str
    description: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        unique_id = self.unique_id
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_list_change = cls(
            title=title,
            description=description,
            unique_id=unique_id,
            enabled=enabled,
        )

        event_list_change.additional_properties = d
        return event_list_change

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
