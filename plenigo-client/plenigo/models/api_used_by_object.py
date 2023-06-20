from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiUsedByObject")


@attr.s(auto_attribs=True)
class ApiUsedByObject:
    """
    Attributes:
        id (int): id of the object related
        internal_title (str): if the product is based on a plenigo offer the product title for internal usage is
            provided here
    """

    id: int
    internal_title: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        internal_title = self.internal_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "internalTitle": internal_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        internal_title = d.pop("internalTitle")

        api_used_by_object = cls(
            id=id,
            internal_title=internal_title,
        )

        api_used_by_object.additional_properties = d
        return api_used_by_object

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
