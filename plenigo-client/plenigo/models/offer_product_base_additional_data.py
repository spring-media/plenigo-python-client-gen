from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.offer_product_base_additional_data_additional_property import (
        OfferProductBaseAdditionalDataAdditionalProperty,
    )


T = TypeVar("T", bound="OfferProductBaseAdditionalData")


@attr.s(auto_attribs=True)
class OfferProductBaseAdditionalData:
    """ """

    additional_properties: Dict[str, "OfferProductBaseAdditionalDataAdditionalProperty"] = attr.ib(
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
        from ..models.offer_product_base_additional_data_additional_property import (
            OfferProductBaseAdditionalDataAdditionalProperty,
        )

        d = src_dict.copy()
        offer_product_base_additional_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OfferProductBaseAdditionalDataAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        offer_product_base_additional_data.additional_properties = additional_properties
        return offer_product_base_additional_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "OfferProductBaseAdditionalDataAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "OfferProductBaseAdditionalDataAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
