from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_base_salutation import AddressBaseSalutation
from ..models.address_base_validation_status import AddressBaseValidationStatus
from ..models.customer_address_creation_type import CustomerAddressCreationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerAddressCreation")


@_attrs_define
class CustomerAddressCreation:
    """
    Attributes:
        type (CustomerAddressCreationType): address type
        business_address (Union[Unset, bool]): flag indicating if address represents a private or a business address
        salutation (Union[Unset, AddressBaseSalutation]): salutation to identify the correct designation of a customer
        title (Union[Unset, str]): title of the customer
        first_name (Union[Unset, str]): first name of the customer - first name and last name or company name are
            required
        last_name (Union[Unset, str]): last name of the customer - first name and last name or company name are required
        company_name (Union[Unset, str]): company name - first name and last name or company name are required
        additional_company_info (Union[Unset, str]): additional information belonging to the company
        street (Union[Unset, str]): street name
        street_number (Union[Unset, str]): street number
        additional_street_info (Union[Unset, str]): additional information describing address
        postbox (Union[Unset, str]): postbox id
        postcode (Union[Unset, str]): postcode
        city (Union[Unset, str]): city
        state (Union[Unset, str]): state
        country (Union[Unset, str]): country code formatted as <a
            href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>
        vat_number (Union[Unset, str]): VAT number of a member country of the European Union
        phone_number (Union[Unset, str]): phone number of the customer formatted as <a
            href="https://en.wikipedia.org/wiki/E.164" target="_blank">E.164</a>
        delivery_information (Union[Unset, str]): delivery information
        academic_title (Union[Unset, str]): academic title
        job_position (Union[Unset, str]): job position
        validation_status (Union[Unset, AddressBaseValidationStatus]): validation status of the address
        validation_hash (Union[Unset, str]): validation hash of a valid address
        preferred (Union[Unset, bool]): flag indicating if address is default selection for address type
    """

    type: CustomerAddressCreationType
    business_address: Union[Unset, bool] = UNSET
    salutation: Union[Unset, AddressBaseSalutation] = UNSET
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
    delivery_information: Union[Unset, str] = UNSET
    academic_title: Union[Unset, str] = UNSET
    job_position: Union[Unset, str] = UNSET
    validation_status: Union[Unset, AddressBaseValidationStatus] = UNSET
    validation_hash: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

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

        delivery_information = self.delivery_information

        academic_title = self.academic_title

        job_position = self.job_position

        validation_status: Union[Unset, str] = UNSET
        if not isinstance(self.validation_status, Unset):
            validation_status = self.validation_status.value

        validation_hash = self.validation_hash

        preferred = self.preferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
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
        if delivery_information is not UNSET:
            field_dict["deliveryInformation"] = delivery_information
        if academic_title is not UNSET:
            field_dict["academicTitle"] = academic_title
        if job_position is not UNSET:
            field_dict["jobPosition"] = job_position
        if validation_status is not UNSET:
            field_dict["validationStatus"] = validation_status
        if validation_hash is not UNSET:
            field_dict["validationHash"] = validation_hash
        if preferred is not UNSET:
            field_dict["preferred"] = preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CustomerAddressCreationType(d.pop("type"))

        business_address = d.pop("businessAddress", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, AddressBaseSalutation]
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = AddressBaseSalutation(_salutation)

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

        delivery_information = d.pop("deliveryInformation", UNSET)

        academic_title = d.pop("academicTitle", UNSET)

        job_position = d.pop("jobPosition", UNSET)

        _validation_status = d.pop("validationStatus", UNSET)
        validation_status: Union[Unset, AddressBaseValidationStatus]
        if isinstance(_validation_status, Unset):
            validation_status = UNSET
        else:
            validation_status = AddressBaseValidationStatus(_validation_status)

        validation_hash = d.pop("validationHash", UNSET)

        preferred = d.pop("preferred", UNSET)

        customer_address_creation = cls(
            type=type,
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
            delivery_information=delivery_information,
            academic_title=academic_title,
            job_position=job_position,
            validation_status=validation_status,
            validation_hash=validation_hash,
            preferred=preferred,
        )

        customer_address_creation.additional_properties = d
        return customer_address_creation

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
