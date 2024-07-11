from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_group_result_types import AnalyticsGroupResultTypes


T = TypeVar("T", bound="AnalyticsGroupResult")


@_attrs_define
class AnalyticsGroupResult:
    """
    Attributes:
        types (Union[Unset, AnalyticsGroupResultTypes]):
    """

    types: Union[Unset, "AnalyticsGroupResultTypes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.types, Unset):
            types = self.types.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytics_group_result_types import AnalyticsGroupResultTypes

        d = src_dict.copy()
        _types = d.pop("types", UNSET)
        types: Union[Unset, AnalyticsGroupResultTypes]
        if isinstance(_types, Unset):
            types = UNSET
        else:
            types = AnalyticsGroupResultTypes.from_dict(_types)

        analytics_group_result = cls(
            types=types,
        )

        analytics_group_result.additional_properties = d
        return analytics_group_result

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
