from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.analytics_group_result_types_additional_property import AnalyticsGroupResultTypesAdditionalProperty


T = TypeVar("T", bound="AnalyticsGroupResultTypes")


@attr.s(auto_attribs=True)
class AnalyticsGroupResultTypes:
    """ """

    additional_properties: Dict[str, "AnalyticsGroupResultTypesAdditionalProperty"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytics_group_result_types_additional_property import (
            AnalyticsGroupResultTypesAdditionalProperty,
        )

        d = src_dict.copy()
        analytics_group_result_types = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AnalyticsGroupResultTypesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        analytics_group_result_types.additional_properties = additional_properties
        return analytics_group_result_types

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AnalyticsGroupResultTypesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AnalyticsGroupResultTypesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
