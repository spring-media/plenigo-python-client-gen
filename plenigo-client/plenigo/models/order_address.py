import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.order_address_salutation import OrderAddressSalutation
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderAddress")


@_attrs_define
class OrderAddress:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        business_address (Union[Unset, bool]): flag indicating if address represents a private or a business address
        salutation (Union[Unset, OrderAddressSalutation]): salutation to identify the correct designation of a customer
        title (Union[Unset, str]): title of the order
        first_name (Union[Unset, str]): first name of the customer - first name and last name or company name are
            required
        last_name (Union[Unset, str]): last name of the customer - first name and last name or company name are required
        company_name (Union[Unset, str]): company name - first name and last name or company name are required
        additional_company_info (Union[Unset, str]): additional information belonging to the company
        street (Union[Unset, str]): street name
        street_number (Union[Unset, str]): street number
        additional_street_info (Union[Unset, str]): additional information describing address
        postbox (Union[Unset, str]): postbox id
        postcode (Union[Unset, str]): post code
        city (Union[Unset, str]): city
        state (Union[Unset, str]): state
        country (Union[Unset, str]): country code formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        vat_number (Union[Unset, str]): VAT number of a member country of the European Union
        phone_number (Union[Unset, str]): phone number of the customer formatted as <a
            href="https://en.wikipedia.org/wiki/E.164" target="_blank">E.164</a>
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    business_address: Union[Unset, bool] = UNSET
    salutation: Union[Unset, OrderAddressSalutation] = UNSET
    title: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    additional_company_info: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    additional_street_info: Union[Unset, str] = UNSET
    postbox: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    vat_number: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        business_address = self.business_address

        salutation: Union[Unset, str] = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.value

        title = self.title

        first_name = self.first_name

        last_name = self.last_name

        company_name = self.company_name

        additional_company_info = self.additional_company_info

        street = self.street

        street_number = self.street_number

        additional_street_info = self.additional_street_info

        postbox = self.postbox

        postcode = self.postcode

        city = self.city

        state = self.state

        country = self.country

        vat_number = self.vat_number

        phone_number = self.phone_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if business_address is not UNSET:
            field_dict["businessAddress"] = business_address
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if title is not UNSET:
            field_dict["title"] = title
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if additional_company_info is not UNSET:
            field_dict["additionalCompanyInfo"] = additional_company_info
        if street is not UNSET:
            field_dict["street"] = street
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if additional_street_info is not UNSET:
            field_dict["additionalStreetInfo"] = additional_street_info
        if postbox is not UNSET:
            field_dict["postbox"] = postbox
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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
                created_date_type_0 = isoparse(data)

                return created_date_type_0
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
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        business_address = d.pop("businessAddress", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, OrderAddressSalutation]
        if isinstance(_salutation, Unset) or not _salutation:
            salutation = UNSET
        else:
            salutation = OrderAddressSalutation(_salutation)

        title = d.pop("title", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        company_name = d.pop("companyName", UNSET)

        additional_company_info = d.pop("additionalCompanyInfo", UNSET)

        street = d.pop("street", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        additional_street_info = d.pop("additionalStreetInfo", UNSET)

        postbox = d.pop("postbox", UNSET)

        postcode = d.pop("postcode", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        order_address = cls(
            created_date=created_date,
            changed_date=changed_date,
            business_address=business_address,
            salutation=salutation,
            title=title,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            additional_company_info=additional_company_info,
            street=street,
            street_number=street_number,
            additional_street_info=additional_street_info,
            postbox=postbox,
            postcode=postcode,
            city=city,
            state=state,
            country=country,
            vat_number=vat_number,
            phone_number=phone_number,
        )

        order_address.additional_properties = d
        return order_address

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
