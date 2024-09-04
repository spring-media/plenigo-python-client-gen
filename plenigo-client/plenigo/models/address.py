import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.address_base_salutation import AddressBaseSalutation
from ..models.address_base_validation_status import AddressBaseValidationStatus
from ..models.address_creation_type import AddressCreationType
from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        type (AddressCreationType): address type
        customer_id (str): unique id of the customer the address belongs to
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
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        address_id (Union[Unset, int]): unique id of the address in the context of a company
    """

    type: AddressCreationType
    customer_id: str
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
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    address_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        customer_id = self.customer_id

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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        address_id = self.address_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "customerId": customer_id,
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if address_id is not UNSET:
            field_dict["addressId"] = address_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AddressCreationType(d.pop("type"))

        customer_id = d.pop("customerId")

        business_address = d.pop("businessAddress", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, AddressBaseSalutation]
        if isinstance(_salutation, Unset) or not _salutation:
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
        if isinstance(_validation_status, Unset) or not _validation_status:
            validation_status = UNSET
        else:
            validation_status = AddressBaseValidationStatus(_validation_status)

        validation_hash = d.pop("validationHash", UNSET)

        preferred = d.pop("preferred", UNSET)

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

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        address_id = d.pop("addressId", UNSET)

        address = cls(
            type=type,
            customer_id=customer_id,
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
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            address_id=address_id,
        )

        address.additional_properties = d
        return address

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
