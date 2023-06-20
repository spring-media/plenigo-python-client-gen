from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceCountrySegmentCreation")


@attr.s(auto_attribs=True)
class PriceCountrySegmentCreation:
    """
    Attributes:
        title (str): title of the price country segment
        countries (List[str]): array of country codes formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        priority (Union[Unset, int]): priority of the price country segment - the lower the priority the higher the rank
            of the price segment
        description (Union[Unset, str]): internal description of the price country segment
    """

    title: str
    countries: List[str]
    priority: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        countries = self.countries

        priority = self.priority
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "countries": countries,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        countries = cast(List[str], d.pop("countries"))

        priority = d.pop("priority", UNSET)

        description = d.pop("description", UNSET)

        price_country_segment_creation = cls(
            title=title,
            countries=countries,
            priority=priority,
            description=description,
        )

        price_country_segment_creation.additional_properties = d
        return price_country_segment_creation

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
