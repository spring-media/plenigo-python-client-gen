from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sort_tree_leaf_type import SortTreeLeafType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortTreeLeaf")


@attr.s(auto_attribs=True)
class SortTreeLeaf:
    """
    Attributes:
        name (str): name of the sort tree leaf
        leaf_id (int): unique id of the sort tree leaf
        type (Union[Unset, SortTreeLeafType]): type sort tree leaf is associated with
        parent_leaf_id (Union[Unset, int]): id of the parent sort tree leaf this leaf is below
    """

    name: str
    leaf_id: int
    type: Union[Unset, SortTreeLeafType] = UNSET
    parent_leaf_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        leaf_id = self.leaf_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        parent_leaf_id = self.parent_leaf_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "leafId": leaf_id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if parent_leaf_id is not UNSET:
            field_dict["parentLeafId"] = parent_leaf_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        leaf_id = d.pop("leafId")

        _type = d.pop("type", UNSET)
        type: Union[Unset, SortTreeLeafType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SortTreeLeafType(_type)

        parent_leaf_id = d.pop("parentLeafId", UNSET)

        sort_tree_leaf = cls(
            name=name,
            leaf_id=leaf_id,
            type=type,
            parent_leaf_id=parent_leaf_id,
        )

        sort_tree_leaf.additional_properties = d
        return sort_tree_leaf

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
