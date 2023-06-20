from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiUsedByOffer")


@attr.s(auto_attribs=True)
class ApiUsedByOffer:
    """
    Attributes:
        plenigo_offer_id (str): if the product is based on a plenigo offer the plenigo offer id is provided here
        internal_title (str): if the product is based on a plenigo offer the product title for internal usage is
            provided here
    """

    plenigo_offer_id: str
    internal_title: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plenigo_offer_id = self.plenigo_offer_id
        internal_title = self.internal_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plenigoOfferId": plenigo_offer_id,
                "internalTitle": internal_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plenigo_offer_id = d.pop("plenigoOfferId")

        internal_title = d.pop("internalTitle")

        api_used_by_offer = cls(
            plenigo_offer_id=plenigo_offer_id,
            internal_title=internal_title,
        )

        api_used_by_offer.additional_properties = d
        return api_used_by_offer

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
