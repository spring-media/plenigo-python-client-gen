from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSearchResultBase")


@_attrs_define
class ApiSearchResultBase:
    """
    Attributes:
        ending_before_id (Union[Unset, str]): A cursor for use in pagination. endingBefore is an object ID that defines
            your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar,
            your subsequent call can include endingBefore=obj_bar in order to fetch the previous page of the list.
        starting_after_id (Union[Unset, str]): A cursor for use in pagination. startingAfter is an object ID that
            defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with
            obj_foo, your subsequent call can include startingAfter=obj_foo in order to fetch the next result set.
    """

    ending_before_id: Union[Unset, str] = UNSET
    starting_after_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ending_before_id = self.ending_before_id

        starting_after_id = self.starting_after_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ending_before_id is not UNSET:
            field_dict["endingBeforeId"] = ending_before_id
        if starting_after_id is not UNSET:
            field_dict["startingAfterId"] = starting_after_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ending_before_id = d.pop("endingBeforeId", UNSET)

        starting_after_id = d.pop("startingAfterId", UNSET)

        api_search_result_base = cls(
            ending_before_id=ending_before_id,
            starting_after_id=starting_after_id,
        )

        api_search_result_base.additional_properties = d
        return api_search_result_base

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
