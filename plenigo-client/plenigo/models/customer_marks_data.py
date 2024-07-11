from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_marks_data_tags import CustomerMarksDataTags


T = TypeVar("T", bound="CustomerMarksData")


@_attrs_define
class CustomerMarksData:
    """
    Attributes:
        customer_id (str): unique id of the customer
        tags (Union[Unset, CustomerMarksDataTags]):
    """

    customer_id: str
    tags: Union[Unset, "CustomerMarksDataTags"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_marks_data_tags import CustomerMarksDataTags

        d = src_dict.copy()
        customer_id = d.pop("customerId")

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, CustomerMarksDataTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = CustomerMarksDataTags.from_dict(_tags)

        customer_marks_data = cls(
            customer_id=customer_id,
            tags=tags,
        )

        customer_marks_data.additional_properties = d
        return customer_marks_data

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
