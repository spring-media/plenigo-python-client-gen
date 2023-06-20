from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.ledger_creation_custom_accountings_additional_property import (
        LedgerCreationCustomAccountingsAdditionalProperty,
    )


T = TypeVar("T", bound="LedgerCreationCustomAccountings")


@attr.s(auto_attribs=True)
class LedgerCreationCustomAccountings:
    """custom accountings of the ledger"""

    additional_properties: Dict[str, "LedgerCreationCustomAccountingsAdditionalProperty"] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ledger_creation_custom_accountings_additional_property import (
            LedgerCreationCustomAccountingsAdditionalProperty,
        )

        d = src_dict.copy()
        ledger_creation_custom_accountings = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = LedgerCreationCustomAccountingsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        ledger_creation_custom_accountings.additional_properties = additional_properties
        return ledger_creation_custom_accountings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "LedgerCreationCustomAccountingsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "LedgerCreationCustomAccountingsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
