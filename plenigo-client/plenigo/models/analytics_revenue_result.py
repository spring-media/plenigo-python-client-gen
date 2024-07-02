from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_revenue import AnalyticsRevenue


T = TypeVar("T", bound="AnalyticsRevenueResult")


@_attrs_define
class AnalyticsRevenueResult:
    """
    Attributes:
        revenues (Union[Unset, List['AnalyticsRevenue']]):
    """

    revenues: Union[Unset, List["AnalyticsRevenue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        revenues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.revenues, Unset):
            revenues = []
            for revenues_item_data in self.revenues:
                revenues_item = revenues_item_data.to_dict()
                revenues.append(revenues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revenues is not UNSET:
            field_dict["revenues"] = revenues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytics_revenue import AnalyticsRevenue

        d = src_dict.copy()
        revenues = []
        _revenues = d.pop("revenues", UNSET)
        for revenues_item_data in _revenues or []:
            revenues_item = AnalyticsRevenue.from_dict(revenues_item_data)

            revenues.append(revenues_item)

        analytics_revenue_result = cls(
            revenues=revenues,
        )

        analytics_revenue_result.additional_properties = d
        return analytics_revenue_result

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
