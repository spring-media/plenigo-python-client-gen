from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ValidationError")


@attr.s(auto_attribs=True)
class ValidationError:
    """
    Attributes:
        field (str): field name with the error
        error (str): error description
        value (str): value of the field
    """

    field: str
    error: str
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field
        error = self.error
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "error": error,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field")

        error = d.pop("error")

        value = d.pop("value")

        validation_error = cls(
            field=field,
            error=error,
            value=value,
        )

        validation_error.additional_properties = d
        return validation_error

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
