from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_data_selection import AdditionalDataSelection


T = TypeVar("T", bound="AdditionalDataSelectionList")


@_attrs_define
class AdditionalDataSelectionList:
    """
    Attributes:
        additions (Union[Unset, List['AdditionalDataSelection']]):
    """

    additions: Union[Unset, List["AdditionalDataSelection"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additions, Unset):
            additions = []
            for additions_item_data in self.additions:
                additions_item = additions_item_data.to_dict()
                additions.append(additions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_data_selection import AdditionalDataSelection

        d = src_dict.copy()
        additions = []
        _additions = d.pop("additions", UNSET)
        for additions_item_data in _additions or []:
            additions_item = AdditionalDataSelection.from_dict(additions_item_data)

            additions.append(additions_item)

        additional_data_selection_list = cls(
            additions=additions,
        )

        additional_data_selection_list.additional_properties = d
        return additional_data_selection_list

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
