from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraduatedPricePerUserSegment")


@_attrs_define
class GraduatedPricePerUserSegment:
    """
    Attributes:
        to_user_count (int): to user count of the segment
        price_issue_id (int): price issue id of the segment
    """

    to_user_count: int
    price_issue_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        to_user_count = self.to_user_count

        price_issue_id = self.price_issue_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toUserCount": to_user_count,
                "priceIssueId": price_issue_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to_user_count = d.pop("toUserCount")

        price_issue_id = d.pop("priceIssueId")

        graduated_price_per_user_segment = cls(
            to_user_count=to_user_count,
            price_issue_id=price_issue_id,
        )

        graduated_price_per_user_segment.additional_properties = d
        return graduated_price_per_user_segment

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
