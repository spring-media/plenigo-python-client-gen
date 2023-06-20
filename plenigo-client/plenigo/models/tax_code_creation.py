from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.tax_code_creation_country_type import TaxCodeCreationCountryType

T = TypeVar("T", bound="TaxCodeCreation")


@attr.s(auto_attribs=True)
class TaxCodeCreation:
    """
    Attributes:
        country_type (TaxCodeCreationCountryType): type of the country
        countries (List[str]): array of country codes formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        tax (float): tax percentage operated on this order item
        analog_tag (str): tag for the analog tax code
        digital_tag (str): tag for the digital tax code
    """

    country_type: TaxCodeCreationCountryType
    countries: List[str]
    tax: float
    analog_tag: str
    digital_tag: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country_type = self.country_type.value

        countries = self.countries

        tax = self.tax
        analog_tag = self.analog_tag
        digital_tag = self.digital_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryType": country_type,
                "countries": countries,
                "tax": tax,
                "analogTag": analog_tag,
                "digitalTag": digital_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_type = TaxCodeCreationCountryType(d.pop("countryType"))

        countries = cast(List[str], d.pop("countries"))

        tax = d.pop("tax")

        analog_tag = d.pop("analogTag")

        digital_tag = d.pop("digitalTag")

        tax_code_creation = cls(
            country_type=country_type,
            countries=countries,
            tax=tax,
            analog_tag=analog_tag,
            digital_tag=digital_tag,
        )

        tax_code_creation.additional_properties = d
        return tax_code_creation

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
