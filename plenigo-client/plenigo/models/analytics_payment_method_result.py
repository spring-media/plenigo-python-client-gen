from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_payment_method import AnalyticsPaymentMethod


T = TypeVar("T", bound="AnalyticsPaymentMethodResult")


@_attrs_define
class AnalyticsPaymentMethodResult:
    """
    Attributes:
        counts (Union[Unset, List['AnalyticsPaymentMethod']]):
    """

    counts: Union[Unset, List["AnalyticsPaymentMethod"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = []
            for counts_item_data in self.counts:
                counts_item = counts_item_data.to_dict()
                counts.append(counts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytics_payment_method import AnalyticsPaymentMethod

        d = src_dict.copy()
        counts = []
        _counts = d.pop("counts", UNSET)
        for counts_item_data in _counts or []:
            counts_item = AnalyticsPaymentMethod.from_dict(counts_item_data)

            counts.append(counts_item)

        analytics_payment_method_result = cls(
            counts=counts,
        )

        analytics_payment_method_result.additional_properties = d
        return analytics_payment_method_result

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
