import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tax_code_creation_country_type import TaxCodeCreationCountryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxCode")


@_attrs_define
class TaxCode:
    """
    Attributes:
        country_type (TaxCodeCreationCountryType): type of the country
        countries (List[str]): array of country codes formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        tax (float): tax percentage operated on this order item
        analog_tag (str): tag for the analog tax code
        digital_tag (str): tag for the digital tax code
        tax_code_id (int): unique id of the tax code in the context of a company
        description (Union[Unset, str]): description of the tax code
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
    """

    country_type: TaxCodeCreationCountryType
    countries: List[str]
    tax: float
    analog_tag: str
    digital_tag: str
    tax_code_id: int
    description: Union[Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country_type = self.country_type.value

        countries = self.countries

        tax = self.tax

        analog_tag = self.analog_tag

        digital_tag = self.digital_tag

        tax_code_id = self.tax_code_id

        description = self.description

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryType": country_type,
                "countries": countries,
                "tax": tax,
                "analogTag": analog_tag,
                "digitalTag": digital_tag,
                "taxCodeId": tax_code_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_type = TaxCodeCreationCountryType(d.pop("countryType"))

        countries = cast(List[str], d.pop("countries"))

        tax = d.pop("tax")

        analog_tag = d.pop("analogTag")

        digital_tag = d.pop("digitalTag")

        tax_code_id = d.pop("taxCodeId")

        description = d.pop("description", UNSET)

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_1 = isoparse(data)

                return created_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        tax_code = cls(
            country_type=country_type,
            countries=countries,
            tax=tax,
            analog_tag=analog_tag,
            digital_tag=digital_tag,
            tax_code_id=tax_code_id,
            description=description,
            created_date=created_date,
            changed_date=changed_date,
        )

        tax_code.additional_properties = d
        return tax_code

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
