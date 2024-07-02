from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceIssueBase")


@_attrs_define
class PriceIssueBase:
    """
    Attributes:
        title (str): title of the price issue
        leaf_id (Union[Unset, int]): id of the tree leaf this price issue should be associated with
        description (Union[Unset, str]): Internal description of the price issue
    """

    title: str
    leaf_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        leaf_id = self.leaf_id

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if leaf_id is not UNSET:
            field_dict["leafId"] = leaf_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        leaf_id = d.pop("leafId", UNSET)

        description = d.pop("description", UNSET)

        price_issue_base = cls(
            title=title,
            leaf_id=leaf_id,
            description=description,
        )

        price_issue_base.additional_properties = d
        return price_issue_base

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
